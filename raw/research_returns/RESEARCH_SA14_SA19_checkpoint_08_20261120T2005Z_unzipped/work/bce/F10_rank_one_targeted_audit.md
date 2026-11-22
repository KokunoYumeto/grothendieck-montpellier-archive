# Targeted audit of F10 and F10b

**Result: PASS for the two requested statements.** GPT-6 Astra (OpenAI),
delegated agent `/root/bce`, 20 November 2026. This is a separate AI proof
audit, not independent human verification. The later F10c and F11 arguments
are outside the scope of this audit.

Audited file: `work/fhi/F_abelian_wild_inertia_candidate.tex`.

## Exact primary source checked

Amalendu Krishna and Subhadip Majumder, *Kato's Ramification Filtration via
de Rham–Witt Complex and Applications*, arXiv:2601.12177v2, 8 November 2026:
https://arxiv.org/pdf/2601.12177 . The original PDF was opened and the
following statements were read, including their surrounding hypotheses:

- Page 2: regular, equidimensional, noetherian, F-finite schemes with an SNC
  divisor; finite type over a field is not a standing hypothesis.
- Theorem 9.4(1), page 55: the refined-conductor map is explicitly injective
  at every Witt length. Corollary 9.7, page 56, specializes its target to the
  component restriction needed here. Corollary 9.6 identifies its generic
  stalk with the local refined conductor.
- Lemma 9.8, pages 56–57: the residue filtration on that target.
- Lemma 3.2, page 12: Witt restriction divides the pole bound by p, with
  the integral part taken coefficientwise.

This is a new preprint input. The audit verifies the deduction from these
stated results, not every proof in the 71-page preprint.

## F10: conductor estimate

For a finite-order p-primary character, let S be its exact logarithmic
Swan divisor. If its coefficient s_i is positive, S−C_i is at least
floor(S/p), so the cited component conductor gives a nonzero section of
Ω¹_X(log D)(S) restricted to C_i. A coefficient field of the complete
equicharacteristic ring is perfect. Frobenius finiteness of its power-series
presentation, quotients, and finite-type resolution charts verifies the
source hypothesis. Absolute differentials over F_p agree with differentials
over that coefficient field because Ω¹_{k/F_p}=0.

The logarithmic residue sequence on the smooth exceptional curve has line
quotients of degrees 2g_i−2+ν_i and 0. Every line subbundle of its middle
term consequently has degree at most k_i=max(0,2g_i−2+ν_i). Saturating the
nonzero section after twisting yields S·C_i≥−k_i. If s_i=0, this inequality
follows from the nonnegative off-diagonal intersections. Thus Bs≥−k.

For C=−B, negative definiteness of the exceptional intersection matrix
makes C positive definite with nonpositive off-diagonal entries. The
positive/negative-part proof in the candidate correctly gives C^{-1}≥0
entrywise, hence s≤C^{-1}k. Both the sign and the direction are correct.

Witt restriction represents multiplication by p on the associated
Q_p/Z_p character, so a fixed p-power larger than every coordinate of the
bound kills every logarithmic conductor. Filtration zero is represented
by integral Witt vectors, and hence is unramified. Purity extends the
resulting character to the regular resolution.

The prime-to-p intersection calculation has the correct adjugate-matrix
factor |det B|. Combining the two bounds annihilates the abelian inertia
kernel by one fixed integer. The use of finite generation of the full
abelianized local fundamental group is an explicit existing input, and
then its subgroup killed by a fixed integer is finite.

## F10b: one fixed cover

Choose an open subgroup Q′ of the abelianized local fundamental group Q
disjoint from the now finite inertia kernel I. The associated connected
abelian cover has finite normalization A′. Completeness and connectedness
make A′ local, and its residue field remains k.

For every exceptional height-one DVR R on a fixed regular resolution of
A′, properness of the original resolution over A extends the generic map
Spec Frac(R)→X to Spec R→X. Every finite character of Q/I is a cover of X,
so its pullback is unramified on R. Thus the image of the inertia at R in
Q lies in I. It also lies in Q′, and therefore vanishes. This applies to
each original abelian monodromy representation, not only cyclic ones,
because finite abelian characters separate points. The normalization of
the corresponding finite cover is unramified in codimension one on the
regular resolution; purity supplies the required étale extension.

The cover and the resolution are chosen before the representation. Their
independence from the coefficient prime and rank is therefore justified.
