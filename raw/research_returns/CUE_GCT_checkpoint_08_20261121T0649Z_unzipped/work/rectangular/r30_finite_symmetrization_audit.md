# Checked alternative route: finite symmetrization on the ordered product cone

This is a supporting audit, not an additional manuscript theorem and not required by R30's nonconstant-spectrum proof. Purity independently checked the claim during the R30 investigation.

Let Z be the affine cone over the ordered Segre-Veronese times auxiliary flag embedding. The linear multiplication map Phi sends its decomposable vectors to polynomial products, outer powers, and the same auxiliary factor. Every nonzero cone vector has a nonzero projective decomposable representative, and a product of nonzero polynomials is nonzero; hence Phi^{-1}(0) consists only of the cone vertex.

If S is the standard graded coordinate ring of Z and R its degree-one image subring, this gives rad(R_+ S)=S_+. The quotient S/(R_+ S) is finite-dimensional. Choose homogeneous lifts of a basis of that quotient. Inducting on degree expresses every homogeneous element of S as an R-linear combination of these finitely many lifts: above their largest degree, reduce into R_+ S using the degree-one generators, then apply the induction to the lower-degree factors. Thus S is finite over R and Phi is finite.

An equivariant finite morphism sends a closed group orbit to its group orbit and is closed, so it transfers closedness of the ordered Fourier orbit to the polynomial product orbit. This gives the k=m prescribed-spectrum statement with polystability even for constant spectra. It does not remove the complex product torus or imply padding stability; R30 instead ensures nonconstant spectra and uses compact stabilizers at the full balanced tensor.

No published source beyond the already cited invariant-theory framework is imported through this audit, and no computational test is claimed.
