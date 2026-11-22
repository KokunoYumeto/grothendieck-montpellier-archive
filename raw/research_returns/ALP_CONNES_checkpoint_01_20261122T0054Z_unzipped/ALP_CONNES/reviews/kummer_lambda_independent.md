# Independent reviewer report: kummer_lambda.tex

Reviewer: /root/sites_twistor, GPT-6 Astra Pro; inherited effort, not separately observable.
Scope: whole-file reading of the proofs AC-K01–AC-K08 and the surrounding classification/phase/gate paragraphs. This is an independent reviewer’s targeted proof check, not a Lean verification or a separately invented proof of every theorem.

## Outcome

The new finite-host construction, maximal-order iteration, explicit p269 model and norm-sector classification pass the proof check. Two small but mathematically relevant refinements are requested before calling the entire module checked: clarify the coefficient field for cubic character projectors and add the inertia-average step for the stated all-prime nonnegative trace assertion.

## Statement checks

### AC-K01 — PASS

Primitive abelian Artin factors are holomorphic in the open critical strip, so there is no pole cancellation. Every primitive character occurs at its conductor. The invariant order R^H is preserved by t↦t^p; the congruence stays inside it because divisibility byp of an invariant element in a torsion-free ring gives an invariant quotient. The primitive-root factor is the required fixed subfield. The source paragraph after Borger–de Smit Thm1.1 really does rule out a field other thanQ.

### AC-K02 — PASS

A K-endomorphism of a finite field extension has finite order. Thus its reduction on a stable integral order is an automorphism. Frobenius injectivity over a finite field excludes nilpotents, making the finite flat model étale. The p≠3 Eisenstein and p=3 valuation2/3 arguments both force ramification and hence exclude the field model.

### AC-K03 — PASS

The quotient DR_f/H is a well-defined commutative ideal-monoid set. On each divisor stratum its orbit field is E_p∩K_(f/d); prime extension degree3 and minimal conductor force every proper stratum to giveK. This checks B_p=E_p×K^(d(f)−1).

For the iteration, modulo each p the Frobenius power and ψ_p are O_K/p-linear additive maps, and their equalizer is a subalgebra. Commutativity of all ψ gives preservation of every R_n. Each index is supported onT, and an existing full-rank integral model remains contained in every R_n. The finite quotient R_0/R therefore makes the descending sequence eventually stationary. The outside-T step is correct; its precise saturation identity is R_n∩qR_0=qR_n when q∉T. This follows by localizing at every prime, or because the T-primary finite quotient has no q-torsion. No uniform index or complexity bound is smuggled into the proof.

### AC-K04 — PASS

269≡2 mod3 is inert, and q=269². At3 the polynomial equation t−3t²+3t³=30 has derivative1 mod3, giving a Hensel root and hence a cube(-1+3t)³=269. The extension splits overK_3, so the tame conductor is exactly(269). The ray-group cardinality is(269²−1)/6=12060. For x=y+t, t∈P, intermediate binomial coefficients ofq=p² are divisible byp and P³=pO_E, so all mixed terms lieP^4 and the pure t^q term does too. Division byp gives exactly the congruence definingR. The residue-difference map is surjective with kernelR, hence indexq. Every other integral model’s Frobenius congruence forces the same residue equality, proving maximality.

### AC-K05 — PASS

For the finite characters, G_Q=G_K⋊<c> with actual complex conjugationc²=1. A c-invariant finite character extends byξ(gc^e)=ξ(g), proving the converse norm-sector assertion. Inducing a restricted Dirichlet character givesη⊕ηχ_-3, with full Artin local factors. Infinite type(z/|z|)^m|z|^(2it), unit compatibility onμ6, and the nonzero angular type of CM elliptic characters are correct. The claim6|m is only made when the finite part is unramified, as needed.

### AC-K06 — PASS subject to cited AM-H03

The no-CM-overfield obstruction is carried from the supplied checkpoint. Once that is granted, E_p∩M=K and a Dirichlet restriction would putE_p insideM(μ_n), a CM field. The standard fact used here is that the normal closure of a CM field is CM and has central complex conjugation; then the compositum argument is valid. For n≤2 the cyclotomic factor isQ and M itself supplies the same contradiction.

### AC-K07 — PASS

The diagonal traces are absolutely convergent forRe(s)>1 and use the full primitive ideal-series convention. Cubic character values give actual negative real-part eigenvalues−1/2, so this particular positivity transfer fails. No counterexample to cubic RH is being asserted.

### AC-K08 — PASS for representation and L-function identities; refine trace sentence

The S3 character inner products give exactly a_m=(2^m+2(−1)^m)/6 and c_m=(2^m−(−1)^m)/3. Full Artin multiplicativity includes inertia invariants. The all-prime nonnegative trace statement is true but its proof should include:

ForW=V^(⊗2r), Tr(Frob|W^I)=|I|^(−1) Σ_(h∈I) χ_W(Frob h). Every summand equalsχ_V(Frob h)^(2r)≥0 becauseχ_V takes2,0,−1. Therefore averaging proves the ramified case as well.

Alternatively state only the unramified assertion. The rest of the proof is valid as written.

## Required coefficient-field refinement

The phrase “the rational character projectors exist” after the μ3 torsor must distinguish coefficient fields. The individual projectors

e_χ=(1+ω²g+ωg²)/3, e_(χ²)=(1+ωg+ω²g²)/3

lie inQ(ω)[C3], orQ_l(ω)[C3]. OverQ the nontrivial pair has one rational idempotent(2−g−g²)/3 and gives a rank-two representation. The field of definitionK of the cover does not itself change the coefficient field of its étale sheaf. This is a wording/scope correction, not a failure of the finite-host theorem.

## Sources directly consulted during this check

- Entire kummer_lambda.tex as supplied byroot at review time.
- Borger–de Smit v4.tex, stratum decomposition immediately before global-thm and Theorem global-thm.
- Yalkinoglu new_version_bck.tex, equation arithalg.
- Borger–de Smit gl09.tex, label thm-A and following field-obstruction paragraph.

The AM-H01–AM-H04, SGA1 locators and Lean dependency chain were not independently re-proved in this reviewer pass; they remain recorded background inputs inroot’s registers.


## Supplemental independent check: AC-K09

Read the entire newly added proof and the referenced AC-T14 compressed-translation proof. The argument passes as an unconditional finite-window result, with no claim on all windows or on the H04.4 arithmetic ramp.

- Recomputed the completed factor Q^(s/2) Gamma_C(s), Q=3*269^2. Twice its real logarithmic derivative is logQ-2log(2pi)+2Re psi(1/2+it). The digamma series gives the stated lower bound c0=logQ-2log(8pi)-2gamma.
- Reconstructed the prime-power coefficients n<16: norm3 and9 at the split prime above3; norm4 at inert2; split7 and13 with conjugate nontrivial cubic values summing to -1. The residues are 269^2 mod7=2 and269^4 mod13=9. There are no other relevant prime powers.
- Recomputed the essential chain lengths for an interval of length log16: 3,2,2,2,2 for shifts log3,log4,log7,log9,log13. At exact ratio2 for log4 the third endpoint is measure zero. The shift log16 vanishes almost everywhere. These give precisely B4.
- Read all rational interval functions in scripts/check_cubic_269.py. The arctanh remainder, alternating arctangent enclosure, Machin identity interval directions, integer square-root bounds and harmonic bounds for gamma are valid. Recomputed the c0-B4 lower bound with gamma bound n=128 and26 arctangent terms: exact rational comparison gives margin>1; its displayed decimal lower bound is1.2742202212706304. No floating-point sign decision is used.
- The triangle inequality for the prime operator, the archimedean lower bound, closure of the stipulated form and restriction to smaller support complete the proof.

Check type: targeted whole-proof check by an independent reviewer, plus exact finite interval computation. This is not recorded as a fully independent re-proof of all external explicit-formula foundations.
