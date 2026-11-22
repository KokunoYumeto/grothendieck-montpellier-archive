# MA-MO-016: polar-retaining actual source completion

The complete written proof is in `polar_source_completion.tex`, equations MA-MO.250–265. The scope is the rational trivial compact type with the actual source place set `{infinity}`, all polynomial weights s≥0, and 0<a<1/2.

## What is constructed

The two source sections are actual even Schwartz functions `(1−2πt²)e^(−πt²)` and `2πt²e^(−πt²)`. Their `(value at zero, additive integral)` vectors are the standard basis. The common smooth sum is exactly E⊕C² in these section coordinates; the positive source image is exactly I⊕C², where I=Theta(U0). Thus W=HΣ⊕C² and W+=J⊕C² retain the inherited HΣ norm on diagonal vectors and retain the polar coordinates as actual source sections. They embed injectively into locally L² pairs. A different actual source section changes these coordinates only by a bounded finite column in I and, if needed, an invertible 2×2 matrix.

The source dilation rho_tau f(t)=e^(−tau/2)f(e^(−tau)t) gives simultaneous logarithmic translation of both theta coordinates. Its two moments scale by e^(−tau/2), e^(tau/2). The section discrepancy is the theta image of a source with both moments zero, hence an I-valued cocycle. This proves a bounded strongly continuous representation and the actual equivariant exact sequences 0→J→W+→C²→0 and 0→W+→W→HΣ/J→0. The second quotient is isometric in the displayed direct-sum norm. No invariant splitting of the polar sequence is claimed.

In the analytic regimes already proved in MO010–011, the continuous cutoff moments split each ideal input into K plus two fixed smooth ideal corrections. The MO010 trace-class K→J map and four finite actual source columns then give the original smoothed source action Cg(P+−P−):W+→W as a trace-class map. This is a map between two named Hilbert spaces. It is not assigned an endomorphism trace.

## Exact remaining scope

The original negative projection itself extends boundedly to W: p−(u,c)=u+Σ c_j r_j, where r_j=(1−phi)(s_j)_0+phi(s_j)_1∈E. On W+ the outgoing quotient defect is exactly −Σ c_j[Cg r_j]. It has rank at most two, and the completed positive image is invariant under this smoothed source column exactly when both Cg r_j belong to J. No such membership is asserted.

The original common-space matrix is still smooth-defined on E⊕C². Its bounded action on off-ideal diagonal directions in HΣ is not established. Keeping this remaining negative-column problem separate is essential; the existence of a trace-class positive source column does not produce a full common-space endomorphism or a relative trace.

## Checks actually performed

The author independently derived the source coordinates, translation cocycle, Hilbert quotient, exact negative projection, finite-column extension and outgoing quotient formula, then read the entire written proof and final scope. Two purely typographic artifacts were corrected before the final pass: a display was split for width, and a stray `+` before “a relative trace” was removed. No mathematical claim changed.

The complete source map definitions and their proofs in Meyer’s supplied `main.tex`, lines 3790–4055, were freshly read, covering `sec:summation`, `lem:Hilm_p_embed`, the actual p+/i+ composition, p−/P−, Poisson summation and `lem:Poisson_sumpm`. The displayed source-domain proofs of MO007 and the analytic/moment prerequisites MO010–011 were reread as used. No new reading of the inherited cote 1 scans is claimed.

The printed local Fourier anticommutation mentioned by the root is not used: this proof uses only the original p+/i+ composition and the separately verified additive formula D i+f=i+Lf for f∈U0.

Status at author completion: proved and complete post-writing author reading passed; independent root and peer readings requested separately. No outside author was contacted.

Subsequent review status: the root and input_audit both reported complete independent written-proof passes. Input_audit also freshly checked the primary source maps and Poisson-sum proof. Their separately saved review events retain the actual reviewer provenance. The later MA-MO-018 constructs the complementary column under an explicit zero-free right half-plane; it does not enlarge the unconditional/generic scope of this theorem.
