# Meyer transport: actual commutator and fixed-S defect

Date: 2026-11-21. Model: GPT-6 Astra Pro. Agent: /root/s5_audit. Reasoning effort inherited and not externally exposed. Parent owns final packaging and public delivery. This file records the additional geometric task assigned after the S5 and positivity audits.

## Proved here

The complete new proofs are in `modules/meyer_transport.tex`.

- **MA-MEY-001:** On the actual one-sided Hilbert space H_a = L²(exp(2ax) dx), a > 1/2, the centered theta and Möbius series Z_S and J_S are mutually inverse bounded operators. For compact smooth g and a smooth cutoff ρ whose derivative has compact support, the actual operator C_g Z_S[J_S,M_ρ] is trace class. Its trace is (ρ_− − ρ_+) times Σ_(p∉S,k≥1) (log p) p^(−k/2) g(k log p). The proof gives an elementary localized-kernel trace-norm estimate, an absolutely convergent double operator series, and its diagonal kernel. It does not assign a scalar to an artificial operator. The unmultiplied commutator gives the derivative of the reciprocal Euler multiplier; multiplication by Z_S gives its logarithmic derivative.
- **MA-MEY-002:** Compact cutoffs have zero commutator trace. A one-sided cutoff with values 1 at −∞ and 0 at +∞ has the displayed prime trace. Uniformly bounded compact cutoffs can tend strongly to it, but their smoothed commutators cannot converge in trace norm when the prime trace is nonzero. The trace-norm distance is at least the absolute prime trace. For a test concentrated at log 2 with value 1, S empty, this lower bound is log(2)/sqrt(2).
- **MA-MEY-003:** These operators are exactly the centered diagonal entries of P_+^S − P_- in Meyer's actual common-space construction. With reflection supplying the reciprocal prime term, Tr C_g(P_- − P_+^S) = −B_out(g). Meyer's trace additivity before its support-adapted enlargement of S therefore yields the fixed-S identity χ_(π+) − χ_(π−) = W_S + B_out through actual nuclear operators. The primes omitted from the local set are carried by the common-space defect.

All three claims have a complete post-writing author proof reading. They require neither M nor A nor any zero-location assertion. Independent review was requested from the parent. No numerical operator approximation has been used as proof.

## Exact conventions

x = log t; C_g u(x) = ∫ g(y)u(x−y)dy; T_l u(x)=u(x+l). The centered integer translation is n^(−1/2) T_(log n). Raw Meyer test f(t)=t^(−1/2)g(log t). Raw Hilbert weight α>1 becomes a=α−1/2>1/2. Meyer's J is inversion J_0 f(t)=t^(−1)f(t^(−1)), becoming reflection R under centering. It must not be confused with J_S, the Möbius inverse.

The source maps are i_+v=(Σv,J_0ΣF* v), p_+^S(v0,v1)=M_(1−φ)L_S^(−1)v0+F M_(1−φ)L_S^(−1)J_0v1, i_-v=(v,v), p_-(v0,v1)=M_(1−φ)v0+M_φv1. Thus 1−p_+i_+ = M_φ−𝖥 M_φ𝖥^(−1), with 𝖥=F J_0. Its trace is the actual local Fourier trace.

The common-space signs follow from these definitions. The displayed matrix in the proof of Lemma 5.6, attached label `eq:global_perturbation`, is labelled P_-−P_+ but writes P_+−P_-. This sign typo does not affect Meyer's later zero-trace argument. It matters for the nonzero fixed-S refinement and is corrected by deriving the diagonal entries directly. A missing convolution symbol in one intermediate trace-additivity display likewise does not change the actual preceding and following formulas.

## What remains open

These results provide a concrete geometric piece, not the complete narrow Hilbert transport. In particular, they do not identify each Masullo orthogonal global cutoff M_ρ C_g P_G with each local additive space/frequency cutoff. They do not provide a bounded Möbius inverse in matching narrow norms; MA-MO-001 rules out that extension. The new compact-cutoff counterexample shows why replacing Meyer's one-sided defect by compact cutoff approximants requires an additional regularization or boundary correction.

MT-M24 identifies the actual smooth negative quotient with E/I. The parent assigned a separate Hilbert-to-smooth nuclear smoothing bridge to /root/input_audit. That bridge may identify convolution traces under the full uniform-interior hypothesis of MT-M26; it must not assume the identification for arbitrary partial strips. The current new module makes no claim that this additional bridge has already been proved.

## Complete invoked source proofs read

Primary source: Meyer, R. (2005), *On a representation of the idele class group related to primes and zeros of L-functions*, arXiv:math/0311468v3, 16 March 2005, 53 pages. Journal metadata confirmed on the primary arXiv record: *Duke Mathematical Journal*, 127, 519–595, DOI 10.1215/S0012-7094-04-12734-4. The running PDF title is *Primes, L-functions and group representations*; it is not the formal title.

Attached source: `sources/LIT_Meyer_representation_of_the_idele_class_group/main.tex`.

1. Definitions of weighted spaces, inversion and equivariant Fourier transform; compact norm-one normalization and centered conversion.
2. Lemma 3.2 (`lem:trace_trivial`), pp.18–19: complete kernel, trace-cocycle and one-sided boundary integral proof. Its following Fredholm-module paragraph is the exact source for the cyclic-cocycle interpretation.
3. Lemma 3.3 (`lem:local_trace_I`), p.20: complete nuclear Fourier-cutoff and trace calculation.
4. The following local principal-value lemmas and calculation (`lem:Fourier_ln_norm`, `lem:normalize_principal_value`, `eq:local_trace_formula`, `eq:local_trace_formula_psi`), pp.21–22: read in full, with the source's dependence on upstream Fourier/Schwartz facts retained.
5. Weighted kernel lemma `lem:mother_of_nuclearity`, and full proofs of `pro:T_on_Twist` / `cor:T_on_Twist`: read the actual nuclear-map and compatible-pairing argument transferring the local trace to the smooth local space.
6. Lemmas 5.3–5.4, pp.39–40: complete Euler-product boundedness and common-space embedding proof.
7. Lemmas 5.5–5.6, pp.41–42: complete Poisson two-dimensional defect and global nuclear perturbation proof, including off-diagonal polar corrections.
8. Theorem 5.8, pp.43–44: complete terminal proof, trace additivity, actual local trace, and support-adapted Euler-defect vanishing. The fixed-S refinement replaces that final zero calculation by MA-MEY-001.

These are targeted whole-proof readings of the invoked local/global arguments, not a newly completed audit of all bornological analysis in the paper. No claim of formal verification is made.

Fresh primary web verification: https://arxiv.org/abs/math/0311468 and https://arxiv.org/pdf/math/0311468. Parent must open the source itself before citing a child-agent web reference in the final answer.

## Grothendieck placement

The actual analytic mechanism is a trace of an extension with a one-sided boundary term. Meyer himself places the basic cutoff commutator in an odd summable Fredholm module and cyclic cocycle immediately after Lemma 3.2. The inherited determinant/logarithmic-derivative comparison has exact archive locators ALPOGE_BRIDGES BR-TR-01/02 and F-SM-11/12, cote 1 scans 079–080 and 111–112; those scans were not freshly reread. No unconstructed proper algebraic pushforward or cohomological realization is asserted.
