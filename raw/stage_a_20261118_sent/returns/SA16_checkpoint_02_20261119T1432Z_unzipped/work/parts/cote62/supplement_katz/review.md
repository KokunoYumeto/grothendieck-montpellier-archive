# Independent review of the cote 63 Hodge argument

Reviewer: GPT-6 Astra Pro, effort inherited/unspecified, run SA16-2026-11-19-cote62. Date: 19 November 2026. This supplement reviews the parent's `work/parts/cote63/hodge_proof.md`, not manuscript images. It also supplies the requested follow-up search for C-SA16-845 / MP-SA16-266. The cote 62 core counts are unchanged.

## Zero locus: the proof passes

The proof of C-SA16-844 is complete once the classical weight-two modular transformation and Fourier expansion of E₂* are taken as inputs. Its estimates work on the whole closed fundamental domain, including the circular boundary. No numerical grid or unproved transcendence statement is needed.

Write τ=x+iy, r=exp(−2πy), θ=2πx. The first sine term in Im E₂* has coefficient −24r. The remaining terms have absolute value at most 24|sin θ| times the sum of n³rⁿ for n≥2. The rational generating function is increasing for r≥0 and its ratio to r is below 21/20 at r=1/200. Thus its tail is below r/20, and cannot cancel the first term. The sign argument therefore excludes every x except 0 and ±1/2.

At x=0, every term of the y derivative of E₂* is positive. At x=1/2, the absolute value of the Fourier part of the derivative is bounded by 48πr times the same rational factor. The function y²exp(−2πy) decreases for y≥√3/2 because its logarithmic derivative is 2/y−2π<0. Its boundary value is below 3/800. Multiplying by π²<10 gives the stated upper bound 189/100<3, so the derivative remains positive. The involutions fixing i and ρ force zeros there because their weight-two factors are not one. These are the only orbits.

`check_review.py` independently executes the rational exponential lower bound and both tail bounds. The fact that the x=0 part of the fundamental domain actually starts at y=1 only makes the monotonicity argument stronger.

## General conjugation matrix: one sign was corrected

The original version wrote the lower-right entry as −ā. With β=−2iρ and c=(aā−1)/β, direct multiplication gives

\[
\begin{pmatrix}a&c\\\beta&-\bar a\end{pmatrix}
\overline{\begin{pmatrix}a&c\\\beta&-\bar a\end{pmatrix}}
-I=
\begin{pmatrix}0&-2ac\\2\beta\bar a&0\end{pmatrix}.
\]

That version was invalid for general a. The correct lower-right entry is +ā:

\[
M=\begin{pmatrix}a&(a\bar a-1)/\beta\\\beta&\bar a\end{pmatrix},
\qquad M\bar M=I,\qquad\det M=1.
\]

The parent repaired the program, proof and reading alternative and added assertions for both identities. The original failed residual is retained at `work/outputs/c63_hodge_initial_matrix_error.json`. This supplement independently reproduces the rejected and corrected residuals.

The scalar identity remains 4ρσ=|a|²−1, since σ=c/(2i). Consequently the square-lattice example and the actual τ=3i bound counterexample are unaffected. This was a defect in the checking argument, not evidence about the handwritten sign.

## Phase: the formula passes with the declared frame

For arbitrary first period w, the real-structure coefficient is

\[
a=-\frac{\bar w}{w}\frac{\pi y}{3}E_2^*(\tau).
\]

Changing the differential by a scalar c changes a by c̄/c. If the coefficient discriminant in this frame is D and c¹²=D, the normalized sixth power has the phase of a⁶/D. Write D=KΔ(τ)/w¹², where K is the positive real normalization constant. Then

\[
\frac{a^6}{D}=\frac{|w|^{12}}K
\left(\frac{\pi y}{3}\right)^6
\frac{E_2^*(\tau)^6}{\Delta(\tau)}.
\]

The first factor is positive, proving the parent's phase formula. Weight twelve in numerator and denominator makes it modular invariant. It is real analytic away from the two zero orbits. The μ₁₂ ambiguity is killed by the sixth power. This review establishes neither a holomorphic expression in j nor an extension through the zeros.

## Katz's algebraicity converse: exact formulation and searched fate

The relevant condition is a line in **algebraic de Rham cohomology defined over an algebraic number field** which becomes H⁰,¹ after complex comparison. With an algebraic differential and second-kind basis fixed, it is equivalent to algebraicity of the corresponding shift coefficient. It is not the condition that a line has algebraic coordinates in a Betti basis.

Katz's published paper identifies this line in Lemma 1.3.6 and proves the CM direction in Lemma 4.0.7. Question 4.0.8, printed page 501, is exactly the converse under simultaneous algebraicity of g₂, g₃ and his real-analytic S. Its eigenprojector proof in the CM case was read. [Katz1976, exact URL and locators in the supplementary bibliography.]

Daniel Bertrand's 3 April 1978 exposition reformulates the question in §6, Conjecture 3, printed page 36-10: away from the elliptic exceptions, simultaneous algebraicity of j and the indicated real-analytic modular function should force CM. This is a conjecture there, not a theorem. [Bertrand1978]

Waldschmidt's 2004 survey, printed page 277, explicitly asks whether G₂* must be transcendental for a non-CM lattice with algebraic g₂ and g₃. It points to Bertrand's nonholomorphic analogue of Schneider. Its dated discussion is evidence of the question's continuation, not a certificate of its status in 2026. [Waldschmidt2004]

Spence's published 2018 paper defines χ*=1728E₂*E₄E₆/(E₄³−E₆²) and proves finiteness of maximal special subvarieties in Theorem 5.8. Its Ax–Lindemann theorem concerns positive-dimensional algebraic arcs. Neither statement says that every individual algebraic pair (j,χ*) comes from CM. Thus this related modern theorem does not close Katz's converse. [Spence2018, pp745–746 and776–777]

The exact MathOverflow question from February 2010 remains without an answer in the page retrieved on the audit date. It is a search-status lead, not mathematical proof. The Bouillot thesis chapter identified by search could not be opened despite web and local attempts; no substantive conclusion is attributed to it. [MOHodgeCM2010; BouillotUnverified]

**Searched fate as of 19 November 2026:** the CM implication is established; no verified resolution of the exact converse was identified in the primary sources and targeted searches recorded here. Retain the converse as an unresolved or uncertified question, with medium confidence about exhaustive current status. A search failure alone does not establish that a problem remains globally open.

## A misleading recent “solution” and the precise error

A prominent UQ page gives an affirmative answer attributed to GPT-5. The retrieved page explicitly says that human verification is still needed and lists no human review. Its argument changes the rational structure from de Rham to Betti and then invokes a broad Hodge criterion without the necessary hypotheses. It supplies no exact theorem or proof bridging that change. It is not adopted as literature establishing a solution. [UQGeneratedAnswer2025, provenance only]

There is an elementary check on the overbroad abstract criterion in that answer. Put τ=i∛2. The polarized weight-one Hodge structure with lines generated by (1,τ) and (1,τ̄) has its splitting over Q̄. Yet its associated complex torus has no CM: a noninteger endomorphism λ=m+nτ would imply nτ²+(m−q)τ−p=0 for some integers m,n,p,q, whereas τ has degree six. This example refutes the stated abstract Hodge criterion. It is **not** a counterexample to Katz, because the torus is not assumed to have an algebraic j-invariant. The irreducibility check is saved in `check_review.py`.

## Source and event retention

The supplement contains 15 exact search/retrieval batches with manually authored outcomes, a scoped bibliography and independent review events keyed to the parent's claim IDs. Raw third-party response bodies are retained only in `external_cache/cote62/katz/`. Numerical and symbolic verification are not inferred from source titles. No new research direction was developed.
