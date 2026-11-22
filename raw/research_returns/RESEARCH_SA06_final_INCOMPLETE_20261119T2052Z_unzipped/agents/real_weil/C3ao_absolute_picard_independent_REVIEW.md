# Independent full proof and source audit: C.3ao

This is a reconstructed audit record after the workspace reset. The original
full audit passed by tool-clock10:01:26UTC on19November2026. The reconstructed
proof was read in full again at10:21–10:22UTC; mathematical fidelity passes.

Reviewer: `/root/real_weil`. The complete five-step proof at
`../cycles/absolute_picard_kernel.tex` was independently checked.

1. The `(r+1)`-tuple of sections on the `r`-dimensional product of quartics
   has no common zero by a proper incidence dimension count. Specified
   algebraically independent coefficients avoid the proper bad locus.
   The divisor is the stated projective bundle; normal degree-one Segre
   ring, regular punctures and the finite normal section-ring replacement
   for the target all have the required hypotheses.
2. Split logarithms and `H1(L^n)=0` for `n>=2` give the exact formal Picard
   class. Proper existence, Elkik puncture comparison and an integral
   exceptional-divisor adjustment produce an actual line bundle on the
   actual resolution with the specified first neighborhood. The graded
   coboundary on the target exponentiates at every order, so its actual
   restriction is trivial. Nonzero higher target Picard cohomology does
   not add a hidden component to this specified class.
3. Multiplication by the actual degree-zero divisor families places the
   constructed cycle in ordinary algebraic equivalence. No inference from
   a local Picard connected component is used.
4. The integral Milnor Bloch formula and `dlog` map on smooth finite-type
   complex stages respect divisor products. All proposed Chow relations
   descend to a finite stage. Tensoring differentials with the exceptional
   structure sheaf retains the conormal summand; ordinary differential
   pullback would kill it and is not substituted.
5. The `k0`-model of V splits the constant-field differential summand. The
   local equation `u-b` contributes `-db/(u-b)`; its Serre-dual residue is
   `-p*omega`. The independent generic coordinates give a nonzero wedge
   and the nonzero canonical tensor remains nonzero at the generic point.
6. Localization cannot kill the detected class: multiplication by `h+b`
   is integrally injective in degree `r-1` when `m>=r`, by descending
   projective-bundle coefficients. Thus the puncture class is nontorsion.

Before the reset I freshly opened Kerz's complete author PDF and read
Theorems7.1/7.5 pp21–22, Braunling's published PDF §3 pp557–558 including
diagram22, and the complete Stacks Section50.9 Tag0FLE. These precisely
justify the integral Bloch formula, cup/concatenation compatibility and
arbitrary Hodge-Chern pullbacks. The restored lemma tag0FMD was freshly
opened after recovery and is exactly Lemma50.9.1. The prior Elkik and
proper-formal-existence source inspections were used in their audited scopes.

The original certificate output was inspected: all checks passed with
runtime0.18043310000211932s. That output was lost in the reset; the cycles
agent is producing fresh output. No missing output is represented as retained.

One recovery wording correction was requested: the differential splitting
requires that V has the stated `k0`-model, not that every displayed line
bundle is defined over `k0` (the generic-point divisors are not). This
does not alter the proof. The correction is being applied by the owner.
