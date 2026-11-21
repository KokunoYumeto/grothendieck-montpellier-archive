# Independent whole-proof audit: E8 GRR dominance

**Auditor:** /root/imprimitive, GPT-6 Astra Pro, effort inherited/not externally exposed, HODGE_DIVISION.  
**Date:** 2026-11-21, approximately 13:23–13:32 UTC, overlapping the separate supplier audit.  
**Proof:** agents/g34_eightfolds/e8_grr/e8_grr_section.tex, D-E8-GRR-01–06.  
**Outcome:** **PASS** for 01–05; **PASS** for the argument in 06 using its explicitly stated, separately proved D-GAUSS-03 premise.

This is independent of the analytic Riemann–Hilbert proof. The computational check here is a fresh rerun of the peer's audited exact programs with both root choices, not an independently implemented character recurrence.

## Actual factors and GRR normalization

The prescribed first inertia has no fixed vector. Thus every counted tuple, including a non-generating one, gives zero global invariants. Moving sum 22 and the two age sums eleven give a six-dimensional K-parabolic space with signature (3,3). The determinant formula does not require full generation and gives signed class three. A possibly disconnected curve has an actual product Jacobian; its rational M8(K) block and a Rosati-fixed primitive projector give an actual polarized sixfold. No virtual abelian variety is used.

I read Tseng's complete marking and node calculation, published pp.60–64, including (7.3.6.1) and (7.3.7.2), and the marking-gerbe convention in Remark 2.4.2 p.19 and §2.5.1 p.21. The degree-one Bernoulli coefficient satisfies A2(g)/2 = 8/12 − a(g). The node coefficient before pushforward is r²A2(g)/4; the gerbe has degree 1/r and branch choice has degree two. The result is rA2(g)/2 on the reduced boundary. This verifies the factor that is most sensitive to stack conventions.

The marking-gerbe degree product rj⁻¹ is cancelled by Tseng's weighted fundamental class, giving the ordinary tuple mass divided by |G|. Applying the same GRR formula to the trivial representation gives the genus-zero relation eliminating the rank term. Serre duality gives the positive Hodge first Chern class, with the sign used in the proof.

The local coarse smoothing equation t=s^r gives both reduced-boundary normal class −(ψ+ + ψ−)/r and the mass factor 1/r. These agree with pullback of the coarse boundary and projection formula.

## Recurrence, signs and factorials

For a boundary divisor repeated ℓ times, multiplication by its self-intersection gives
\[
\frac{(-tar)^\ell}{\ell!}
\left(-\frac{\psi_++\psi_-}{r}\right)^{\ell-1}
=-r\,\frac{t^\ell a^\ell}{\ell!}(\psi_++\psi_-)^{\ell-1}.
\]
After the reduced-stratum mass, the edge series is
\[
-\frac{\exp(ta(\psi_++\psi_-))-1}{\psi_++\psi_-}.
\]
Its coefficient at endpoint exponents u,v is −a^(u+v+1)/((u+v+1)u!v!). The parent vertex adds a second 1/v!, accounting for every factorial in the L recurrence. A bare root insertion already contributes its vertex factorial in T; restoring the root exponential contributes the additional 1/u!. The final factors restore the labels of equal-class leaves and replace the exponential coefficient by the top power.

The trace [1]/|G| and class pairing |c|/|G| agree with a direct groupoid count: choose trivializations on all vertices, glue inverse holonomies, and eliminate changes of trivialization along a spanning tree. Only simultaneous conjugation remains. The inverse class pairing removes one vertex normalization at each gluing.

Imaginary subtree inversion is harmless because the Hodge weight is inversion invariant. Multiplying the two imaginary factors at the final root inserts the central negative identity; hence the negative Weyl class and denominator 2|W| in the program are correct.

The recurrence is finite. L[c,v] has Hodge degree k−1+v, giving v≤d−k+1. Every child has fewer leaves. I checked that the cached convolution never stores an early zero for a coefficient that is later populated: all queried child coefficients are either already computed or permanently outside the degree truncation.

## Exact arithmetic reruns

I read build_character_input.py, check_character_input.py and exact_hodge_volume.py in full. The builder specializes the official CHEVIE entries at q=v=1 and reconstructs documented alternate rows by sign twist. The retained-input checker reconstructs every class matrix, exact order, invariant Cartan form, characteristic polynomial and both scalar-coset weights.

Fresh runs in agents/imprimitive/grr_audit gave:

| Check | Result |
|---|---|
| 112 class matrices, exact orders and invariant forms | PASS |
| complete character orthogonality and degree sums | PASS |
| all 224 weights from exact cyclotomic spectra | PASS |
| natural traces and central translation | PASS |
| order-twelve root: ninth Hodge intersection | 3009825/64 |
| involution root: ninth Hodge intersection | 3009825/64 |
| either root: tuple-stack degree | 90296156160000 |

The retained source/input hashes are in grr_audit/rerun_input_manifest.json. The two roots are different evaluations of one proved recurrence. Completeness and character status of the author CHEVIE table remain the stated finite-group input; orthogonality alone is not claimed to establish them.

## Canonical extension and period rank

I read the published Catanese–Dettweiler Theorem 2.1 proof, p.242, identifying the semistable relative-dualizing direct image with the canonical Hodge extension characterized by nilpotent residues. The local generator dx/x = −dy/y verifies the compatibility used here. Semistable resolution adds rational components without changing the direct image. The identification over transverse disks at every prime boundary divisor therefore extends globally between the locally free bundles on the normal resolved base, including exceptional divisors.

The full real isotypic variation has rank 96 and F1 rank 48. Each of the conjugate multiplicity bundles occurs eight times. Their first Chern classes agree by the inversion-invariant GRR formula. Thus c1(det F1_full)=16λρ on the compactification, not merely on its open part.

I read the complete proofs of Bakker–Brunebarbe–Tsimerman Lemmas 6.15 and 6.17, author pp.42–44. They apply to the polarized real variation with unipotent monodromy on the smooth projective alteration. The canonical determinant is nef and is big precisely when the Hodge differential is generically injective. Each component therefore contributes nonnegatively; the positive total intersection forces a strictly positive component. The full fixed-multiplicity variation and its primitive sixfold have the same differential kernel, so the latter has rank nine. Only then is the dimension of the unitary target used to conclude dominance.

This argument does not identify the dominant component with the independently exhibited doubled-pair tuple.

## Connectedness upgrade

The explicit commutant calculation in 06 checks. Commutation with the reference complex structure makes the complex-linear part block diagonal and the antilinear part block off-diagonal. Commutation with all tangent matrices makes the linear part scalar; diagonal matrices and matrix units kill the antilinear part. The rational commutant is exactly K. The Baire argument applies to the actual open period image and gives a very general simple fibre with full endomorphism algebra K.

The coefficient algebra End_KJ(V) acts by Hodge maps on parabolic cohomology. Exactly one simple factor is active; its injection into the field K forces multiplicity one and division algebra K. Thus the active summand is absolutely irreducible over K. A rational character would give an intertwiner with its conjugate over K, hence an invertible rational K-antilinear coefficient map. This induces an extra Hodge endomorphism and contradicts End_Hdg=K. The argument also excludes the rational-character quaternionic possibility.

Some reflection must be active: otherwise the local system has only two inverse nontrivial monodromies and zero parabolic cohomology. Applying the separately proved D-GAUSS-03 then forces an eight-dimensional E8 reflection component. It occupies the entire ambient representation. Its reflection subgroup lies in the original real W(E8) and has the same order, so it equals W(E8); an imaginary inertia gives the full group G.

I read D-GAUSS-03 and checked its applicability. This is not a new rerun here of all finite enumerations and classification sources underlying that separate premise.

## Primary sources and limits

- Tseng, Geometry & Topology 14 (2010), §7.3 pp.60–64, complete Bernoulli/node derivation; marking conventions p.19/p.21. Original publisher PDF read.
- Bakker–Brunebarbe–Tsimerman, Inventiones Mathematicae 232 (2023), author pp.42–44, complete Lemmas 6.15/6.17 proofs.
- Catanese–Dettweiler, C. R. Acad. Sci. Paris 352 (2014), Theorem 2.1 proof p.242, original journal PDF read.
- Official author CHEVIE table, whose source hash is recorded in the proof and mathematical input. The rStation numbers are comparison targets, not arithmetic inputs.

No numerical algebraic-cycle degree is certified by this audit. That requires the separate supplier and degree arguments.
