# Independent whole-proof review: THETA3-B22

Reviewer: GPT-6 Astra Pro, /root/theta_032; inherited effort label not exposed.
Date: 2026-11-21.

I read the entire saved paper_B22.tex and reconstructed its proof. The result passes at its stated normalization and arithmetic-data scope.

The even-null bound is the product of the one-dimensional inequality
\(\sum_{m\in\mathbf Z}r^{m^2}\le(1+r)/(1-r)\), with the zero term removed. The odd coset substitution gives exactly \(4\pi i\), not \(2\pi i\). With \(q=e_j\), \(N>2\), and \(m\ne0\), the bounds \(N\|m\|/2\le\|q+Nm\|\le3N\|m\|/2\) give \(6\pi N\|u\|\sum\|m\|e^{-a\|m\|^2}\). Splitting \(\|m\|\le\sum_k|m_k|\) and using the one-dimensional weighted geometric sum gives exactly the coefficient \(12\pi gN\|u\|\) in (B22e). Both level-selection inequalities eventually hold because the tails tend to zero along the allowed multiples. The nonzero leading term and its half-size lower bound are correct.

The algebraic normalization is also consistent. Dividing the algebraic theta map by its nonzero even reference value makes the new comparison scalar \(\upsilon E_N\). The two vectors \(u^w,u^z\) have identical coordinate vectors but are in different variable spaces; \(z=Nw\) gives \(c_N\ell(u^w)=N\upsilon H_N\). The algebraic normalization \(\ell(v)=1\) therefore yields exactly \(c_Np_N/N=\upsilon H_N\). Transporting that algebraic generator and the same Betti generator through the fixed repeated CM factor gives one \(p_N\) for both copies. This does not require the other copy's own reference jet to equal one.

I checked the final field-norm bound against (B19k). Its two selected complex embeddings contribute \(D^2|b|^2\), and the other \(d-2\) embeddings contribute at most \((DM)^{d-2}\). Hence the denominator is \(D^dM^{d-2}\), exactly as written. The Haar factor changes from \(v_H\) to \(v_H^{1/2}\) for an orthonormal test vector as recorded in B19.

The limitation is accurately retained: normalizing by the algebraic even value and odd derivative can enlarge denominators and other conjugates. The proof removes the unspecified absolute analytic period factor only after moving these costs into the actual algebraic arrays. It proves neither a uniform height estimate nor saturation at a specified prime.

No new external theorem is required for the Gaussian argument. The CM finite-Heisenberg and first-jet comparison inputs are those separately source-checked in B19 and B21; this review does not claim a fresh transitive source audit.
