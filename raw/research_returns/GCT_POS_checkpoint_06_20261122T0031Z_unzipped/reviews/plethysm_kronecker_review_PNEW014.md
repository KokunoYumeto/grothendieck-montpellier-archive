# Independent complete review of PNEW-014

Reviewer: `/root/kronecker`, GPT-6 Astra Pro. Date: 2026-11-21 UTC.

## Material read

I read the complete statement and proof in
`branches/plethysm/trace_index_obstruction.tex` and the complete exact
verifier `branches/plethysm/scripts/check_trace_index_obstruction.py`.
I then replayed the verifier independently of the author's run.

## Result

**PASS. No mathematical gap found.** The replay passed all three cases
`n = 10, 12, 14`, with 34,730 actual coefficient degrees checked, the
positive-tail inequalities, independent literal-binomial checks of the
mask, and the sampled exact ambient inequalities. This finite replay
supports the formulas; the all-dimension assertions are proved by the
written inequalities and injection, not inferred from the samples.

I independently reconstructed the following points.

1. The parameter inequalities hold for all even `n >= 10`. The endpoint
   `2^(n-2) >= 2n^2 + 4`, preserved under `n -> n+2`, gives the exponential
   lower bound on `a` and the required separation of the waves from the
   initial holes. All binomial-polynomial arguments before their natural
   starting degrees remain nonnegative integers below the lower index,
   so the asserted global polynomial/quasipolynomial extensions are valid.
2. The exact hockey-stick identity for `B` and the bound `q(S)-B-2 > 0`
   give the initial cancellation and all positive attained values. The
   proof of `q(r) >= 2q(a)` works term by term, including the case with
   `u=0` and the summands that are absent at `a`.
3. The identity `T_F-T_G = 3T_0`, the bound on each signed wave, and
   `q_0(r) >= q(a) >= h+1` prove coefficientwise `c >= 0` on the entire
   tail. Thus the displayed rational `C_3` representation really has
   dimension `f` and trace `g` in every degree. No multiplication of
   those representations is asserted.
4. Direct substitution gives the common reciprocal multiplier `-t^A`
   for every summand. The pole orders at one are exactly `D` and `E`.
   Properness is checked for all terms, so no unaccounted finite initial
   correction is hidden in the quasipolynomial statement.
5. The ambient injection is valid in every degree at least `S`. The
   parity of the first `K` exponents recovers all bits and free exponents;
   the distinct marker exponents `1,...,6` separate the three mask copies,
   the polynomial upper bound, and the two bounded-wave objects. The
   padding variable is distinct from both the free and marker variables,
   and every unpadded degree is at most `ns`. The remaining initial
   degrees are handled exactly.
6. At a primitive `M`th root, only `C T_G` contributes, with the stated
   residue `2C zeta^r(1-zeta^2)`, a unit above three. The correction
   periods are strictly below `M/2`. The denominator of `T_F` is exactly
   `Phi_(3M)` and its numerator is nonzero there. Hence the absence of an
   `M` pole in `F`, presence of a `3M` pole, and absence of all higher
   collision poles in `G` are exact statements about the reduced rational
   functions.
7. The lower bound on `s(g)` tests a constituent at the off-residue
   integer `a`, rather than merely checking attained values. The strict
   index `s(f)=S-1` follows from positivity of every constituent at all
   integers at least `S` and the actual initial zero. The positivity-index
   bound follows from coefficientwise dominance of the two shifted
   products, positive constants in every shifted mask factor, and the
   explicit constant margin over all periodic corrections.

## Scope

The result concerns formal rational characters, with actual rational
`C_3` representations degree by degree. It does **not** construct an
invariant algebra, does not identify `G` with the actual auxiliary
series `B_n`, and does not prove or disprove either strict index bound
for triple-rectangular Kronecker coefficients. It correctly shows that
the listed numerical and representation-theoretic data alone cannot
transfer an exponential auxiliary strict index to the tensor sequence.
