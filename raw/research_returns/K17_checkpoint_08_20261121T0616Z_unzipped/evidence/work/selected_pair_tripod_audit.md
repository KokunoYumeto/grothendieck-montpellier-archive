# Independent selected-pair faithfulness audit

Reviewer: /root/tripod_integral. GPT-6 Astra Pro; 21 November 2026.

## Verdict and scope

PASS for the complete theorem and arithmetic corollary in
selected_pair_faithfulness_section.tex, reviewed hash f124400b519ba4eee33a2beab4a0a8e866df706dfa06649f7c73df6ed36dfb39.
I read the entire proof, reconstructed its arithmetic and Magnus
arguments, and checked the cited componentwise inputs against the
previous complete universal-cup proof. I freshly read WWE's setup,
Proposition2.2.6 and Corollaries5.1.1–5.1.2 with their full proofs,
and Sharifi Proposition3.4.7/Corollary3.4.8 with their full proofs.
The sole correction requested was the harmless but necessary wording
that it is the logarithm of an odd eigenlift which has only odd target
lengths. The author made that correction, and I read it back. The
resulting group image still starts in length at least3 after its linear
coordinates are removed.

This is injectivity on a specified closed free factor only. It neither
asserts full kernel equality nor makes that factor Gamma-stable.

## Arithmetic character labels and local cup argument

For even e distinct from0,2, applying WWE2.2.6 at reflected character
omega^e makes the actual ramified module in character omega^(1−e)
integrally free of rank one. Its unramified quotient X_chi is cyclic,
where chi=omega^(1−e). Kummer's involution and twist give precisely
T_e[1/p], since1−(1−e)=e. A finite pseudoisomorphism becomes an
isomorphism after invertingp, so this is rational cyclicity, including
all repeated-root possibilities.

The other vanishing is X_theta=0 with theta=omega^(2−e); here
chi=omega^(−1)theta as required by WWE's original notation. These
are genuinely two distinct reflected inputs. Corollary5.1.2 gives
integral varpi surjectivity from this vanishing plus cyclicity of
X_chi(1). It does not require the characteristic series to have
simple roots: that extra condition is only for the assertion that
the two maps are mutual inverses. The excluded0,2 cases match the
already checked zero unramified omega±1 components, and hence
T_e=0 by torsion freeness.

The previously checked universal-cup proof is componentwise. Its
class-two even extension projects to the Delta-eigenspace e, and
the dual H2 target has character2−e. Norm-compatible inputs kill
all Lambda-torsion, including arbitrary omitted odd components.
Thus the fixed-denominator split-socle argument uses only the chosen
T_e and that one target eigenspace. The source's finite-level symbol
surjectivity, same-level nonunit exponent products, parity reduction,
and cofinal group/coefficient indexing remain exactly those of the
prior complete proof. The dual quotient has rootu²/alpha, and its
corestriction transitions are quotient maps without an extraneousp.
A commonp^b cannot annihilate its nonzero torsion-free inverse limit.
No assertion about another even or odd torsion component is used.

## Actual free factor and filtration

The compact product-basis splitting and exact eigenlift construction
precede all cyclicity hypotheses in the earlier proof. Sending the
omitted finitely many torsion basis elements to1 while keeping every
selected generator is continuous on the pointed compact generating
set. The free universal property gives a retraction of H; its compact
image is precisely the subgroup asserted and is a closed free factor.

Assigning degrees1,2,3 to Q, evenT, oddT uses the whole free basis.
The finite odd-torsion characteristic polynomial annihilates every
retained linear coordinate after removing its finitely many resonant
odd generators. Complex conjugation then gives length at least3 for
omitted odd torsion and length at least2 for even torsion. Therefore
actual conjugates outside the selected subgroup still respect the
full assigned filtration. Density supplies a nonzero moment in every
retained odd coordinate. The bounded R-basis change and normalization
are the prior whole-H construction, not a passage to a finite-index
subgroup.

For each selected T_e, actual gamma-conjugates of a cyclic lift give
an invertible rational linear system on its degree-two T coordinates,
plus quadratic Q expressions. They need not lie in the free factor:
only their homogeneous leading expressions change coordinates there.
Those expressions contain no omitted even variable, because the
abelian character component is unchanged, and no odd torsion variable,
because the latter has assigned degree3. The companion error has zero
abelian class, leaving only a quadratic expression in Q at degree2.
This proves the stated moment/pair kernels with no hidden Gamma
stability assertion.

## Laurent separation

After the bounded triangular changes, a nonzero subgroup element has
a first nonzero assigned Magnus degree. Its first target-length
coefficient is a finite pattern sum of singleton and selected pair
kernels. Large odd residue-class tails avoid every discarded linear
and pair-sum resonance and still have interior Cartesian accumulation.
The bounded power-series identity theorem therefore applies after
clearing denominators.

For disjoint chosen pair positions, the variables S_B=z_i z_(i+1)−beta
and one retained variable per pair are legitimate formal coordinates.
Any different adjacent-pair denominator is nonconstant in the remaining
base variables on that stratum; a different root at the same position
is a unit. Maximal pair count, then Pareto-maximal pole order, isolates
the chosen pattern. Character labels distinguish components, while
rational cyclicity rules out duplicate blocks of one character and root.
The remaining singleton coefficient is nonzero and depends on the
singleton variables; each selected numerator restriction is nonzero
in its independent pair-base variable. Their product is nonzero in
the base fraction field. This yields the contradiction, including
repeated roots and the no-pair case.

The finite arithmetic range follows exactly by matching X^[−2j]=0
with X^[2j+2]=0. Replacing9 by any establishedR≤15 is explicitly
allowed by the proof, so the new rangeR=12 also follows once the
separate K40/K44/K48 theorem is invoked. No Triple-NV conclusion
for omitted characters is inferred.
