# Exact ordinary admissibility audit

## Verdict and status

The constructed ordinary symmetric-square systems satisfy the actual predicate
`Adm3U_s ι e 2 ρ`, under the project's stipulated use of the pinned archive and
the published automorphic inputs. This is stronger than membership in the
ambient stable compact spectrum. The extra `WitA` and `Th.Unl` clauses are
discharged below; they are not assumed from ordinary automorphy.

This is a mathematical/source audit. No Lean elaboration or kernel build was
run. “Closed” below means that the displayed source theorem has no additional
proposition argument: it is a syntactic declaration with a proof using its
imports. This audit does not assert a new kernel verification of those imports.
It also does not assert that every member of `Adm3U_s` is a point of the
particular deformation ring used to construct the finite comparison set.

Revision: `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` of
`CocoSgt/riemann-hypothesis-lean`. New fetched files were checked by Git blob
SHA1 against the complete pinned `AV_tree.json`; their URLs, SHA256 values and
retrieval times are in `ADMISSIBILITY_SOURCE_ADDITIONS{,_2,_3,_4,_5}.json`.
The metadata records retrieval, not whole-proof review of every incidental
dependency fetched.

Paths below are relative to
`src/Development/AutomorphicArithmetic/AutomorphicVarieties/`, except where
`Foundations/` is explicitly indicated.

## 1. All fields of the actual predicate

`ModularityArgument/ThresholdArguments/DenseThresholdCases/NumberU3US.lean:27–29`
defines `Adm3U_s` by extending `Af.Adm3Alt` and adding

```
Th.Unl l N ![(e : ℤ), 0, -(e : ℤ)] ρ.
```

`AfStmt.lean:29–32` in that same directory gives all three `Adm3Alt` fields:

1. `IsIrr ρ`;
2. `Win.IsAutCsdA ι (tw ρ (cycBar K Ω l)⁻¹)`;
3. `Level l N ![(e : ℤ), 0, -(e : ℤ)] ρ`.

`ModularityArgument/AutomorphyLifting/IsAutCsdA.lean:11–12` defines the second
predicate as `AutCsd0 ι r ∧ (Continuous r → WitA ι r)`. In
`Foundations/GaloisRepresentations/AdmissibleResidues/IsAutomorphicOverImagQuad.lean:35–36`,
`AutCsd0` means that some regular algebraic cusp representation is conjugate
self-dual and attached to `r`.

The old `Wit` in that foundational file is an away-from-ell unlinking
predicate. It is not the `WitA` used here. The `type_of%` examples in
`IsAutCsdA.lean:22–25` compare type signatures; they do not identify these
predicates.

## 2. Level and the extra unlinked flag

The complete relevant definitions in
`AutomorphicForms/BlochKatoSelmerVanishes.lean` were read:

- `IsFlagOn` is an actual upper triangular realization on the decomposition
  group, with ordered diagonal characters, not only a list of Hodge–Tate
  weights.
- `LevelAway` (89–91) requires diagonal inertia through global characters
  killed by the cyclotomic extension containing the indicated roots of unity.
- `LevelAt` (102–107) requires the ordered flag, the displayed inertia powers
  times those global finite characters, and either nonadjacency of the
  decomposition-group characters or potential crystallinity.
- `Level` (111–114) includes continuity and both local requirements.

For level parameter 2, choose all the global finite characters to be 1.
Unramifiedness away from ell gives `LevelAway`; the ordinary flag gives
`LevelAt`. The character inequalities below supply its first alternative,
so the potentially crystalline alternative is not needed.

`AutomorphicForms/LocIsotypic.lean:31–34` defines `FlagAt M m r A κ` exactly as

```
∃ χ, (∀ i, KillsMu M (χ i)) ∧ IsFlagOn r (Dec A) κ ∧
  ∀ i s, s ∈ Ine A → κ i s = cycBar s ^ m i * χ i s.
```

`TheoremsMuLinked/AutP.lean:10–13` defines `Th.Unl`: for every place above
ell, there exists a valuation above it and a tuple `κ` satisfying this
`FlagAt`, with `κ i ≠ κ j * cycBar` for every pair of indices. There is no
additional regular-weight bound, splitting requirement, or finite-coefficient
restriction in this predicate.

If the inertia exponents are `(e,0,−e)`, with `e≥2`, every difference is in
`{0,±e,±2e}`, hence none equals 1. An equality
`κ_i^b=(κ_j cyc)^b` with positive integer `b` would give a nonzero power of
the cyclotomic character trivial on local inertia. Its inertia image over
any finite extension of Q_ell is infinite, which is impossible. This proves
`Th.Unl` with trivial global characters. The same argument works for the
twisted exponent tuple `(e−1,−1,−e−1)`.

## 3. First clause of WitA: positive-power unlinking

`ModularityArgument/AutomorphyLifting/WeakOfAtt.lean:19–30` defines:

- `Unl1 r v`: for every valuation over `v`, an actual flag whose characters
  satisfy `κ_i≠κ_j cyc`;
- `PotUnl r v`: for every valuation over `v`, an actual flag satisfying
  `κ_i^b≠(κ_j cyc)^b` for all indices and every positive integer `b`;
- the first clause of `WitA`: at places above ell,
  `Unl1 r v → PotUnl r v`.

The preceding inertia argument directly gives `PotUnl`, whether or not the
antecedent is supplied. It therefore proves this implication.

There is also an exact closed source discharger:
`ImaginaryQuadraticEtaCharacter.potOfFlag`, in
`ModularityArgument/LeviSmoothLocalization/PrincipalSeriesMatching/PotOfFlag.lean:88–99`.
Its proposition is defined in `LeviSmoothLocalization/PotOfFlag.lean:11–16`:
for any number field and any ell, inertia exponents with no difference 1,
together with the flags and any positive auxiliary power eliminating their
finite inertia characters, imply `PotUnl`. Here that auxiliary power is 1.

The entire 99-line proof file was read. Its private `cyc_inf_over` constructs
an infinite-order cyclotomic inertia element after taking a positive power
which fixes the number field; `flag_exp` then proves the contradiction for
all positive powers. No inequality comparing ell to the weight is used.

## 4. Second clause of WitA: its exact quantifiers

For `r=ρ cyc⁻¹`, the other clause at `WeakOfAtt.lean:29–30` is

```
∀ π, IsRegAlg π → AttC ι r π →
  ∃ t : ℝ, ∀ v, (ell ∉ v ∨ PotUnl r v) → WinAt π t v.
```

It quantifies every attached regular algebraic cusp representation. It does
not assume that the arbitrary `π` is conjugate self-dual. A witness for only
one attached representation would therefore be insufficient without the
uniqueness step below.

`LeviSmoothLocalization/WinUpDown.lean:38–41` defines `WinAt π t v` as toral
supercuspidal support together with the strict inequalities

`q^(t−1/2) < |ξ(uniformizer)| < q^(t+1/2)`

for every character in every supercuspidal-support realization at `v`.
Here `q` is the residue cardinality. The single real number `t` must work
at every place selected by the displayed disjunction.

Three closed source theorems give a direct sufficient condition:

| Theorem | Full proposition locator | Full proof locator |
|---|---|---|
| `sphUnl` | `WinUpDown.lean:162–164` | `PrincipalSeriesMatching/SphUnl.lean:25–45` |
| `winOf` | `WinUpDown.lean:158–160` | `PrincipalSeriesMatching/NormAbsPowUnif.lean:124–168` |
| `suppSmo` | `WinUpDown.lean:142–145` | `PrincipalSeriesMatching/SuppSmo.lean:6–12` |

The entire three proof files were read, including the private lemmas in the
169-line `NormAbsPowUnif.lean`. The proofs have the following scopes.

`sphUnl` says that a finite spherical local component has toral and unlinked
support. It uses uniqueness of supercuspidal support and the spherical
Satake unlinking theorem.

`winOf` applies to every cusp representation of positive rank over a totally
complex number field. It produces one real `t`, before quantifying over
places, and proves `WinAt` at every toral-unlinked place. Its proof globally
unitarizes the cusp representation, applies the imported local generic
unitary exponent bound, excludes segments of length greater than 1 by the
unlinked hypothesis, and removes the global character twist. This is a
strict width-one result; no Ramanujan assertion for arbitrary GL3 cusp
representations is assumed.

`suppSmo` says that cofinite equality of the complete Satake multisets
transports `WinAt` with the same `t` to another cusp representation. Its
complete proof uses `strongMultOneC` to identify the two `CuspSub` objects.

Let `π₀` be the already constructed everywhere finite spherical adjoint base
change attached to `r`. Apply `winOf` once to `π₀`; apply `sphUnl` at every
finite place. This gives `WinAt π₀ t v` for all finite `v` with one `t`.
If `π` is any other representation in the universal clause, the two `AttC`
conditions give the same Frobenius characteristic polynomial cofinitely.
The common nonzero `algSat` factor can be canceled, and roots with
multiplicity give equality of the Satake multisets. Apply `suppSmo`.
The resulting window holds at all places, hence certainly at all places
selected by the `WitA` disjunction. This proves the whole second clause.

## 5. Application to the ordinary symmetric-square family

The entire original `main_gate/ordinary_symmetric_square_admissibility.tex`
proof and the complete added `KT-ORDINARY-SYM2-ADM3` corollary were read.
The ordinary two-dimensional basis has diagonal `(δ,η)` with `η` unramified
and `δη=epsilon cyc^e`. Its symmetric-square basis
`(v₁²,v₁v₂,v₂²)`, divided by `δη`, has diagonal
`(δ/η,1,η/δ)` and inertia exponents `(e,0,−e)` in the correct order.
Restriction to E and conjugation to any place preserve the actual flag.
FR Theorem 3.6 includes the Hecke congruence at q=ell, since ell is prime to
the fixed level; hence its form is ordinary in every weight of the Sun
progression. No Fontaine–Laffaille range is imposed.

Together with the previously reviewed global symmetric-square theorem and
the characteristic-zero irreducibility input, Sections 1–4 construct every
field of `Adm3Alt` and then `Adm3U_s`. The normalization is important:
`ρ` has weight zero, while `AttC` is applied to `ρ cyc⁻¹`, exactly matching
the geometric Frobenius convention and the factor q in rank-three `algSat`.

The primary ordinary statement was visually checked in Ghate–Vatsal,
*On the local behaviour of ordinary Λ-adic representations*, printed
p.2144, equation (1.1) and preceding paragraph. It explicitly recalls the
general Mazur–Wiles/Wiles upper triangular theorem with unramified lower
diagonal character, without a residual irreducibility hypothesis. The
original Wiles proof is an imported theorem, not a newly read proof.

### Corrected irreducibility reference

A fresh visual check of the saved Ribet PDF found a citation error in the
initial geometry draft. `rankin.pdf`, *On l-adic representations attached
to modular forms II*, has no Theorem 0.1 on p.186. Theorem 3.1 on p.191 is
an **almost-all-primes** integral-image result. Section 3 begins on p.190
and its proof is not contained in pp.189–191.

The needed **every-prime** result is nevertheless explicitly stated on
p.191 immediately above Theorem 3.1: Ribet recalls Momose's theorem that,
for each ell, the image of the finite-index subgroup H is open in
`{x in (D tensor Q_ell)^× : nr(x) in Q_ell^×}`. After coefficient closure,
the Lie algebra contains the `sl₂` factor at every chosen coefficient
embedding. Passing to the finite-index subgroup `G_E` preserves this Lie
algebra, so its adjoint representation is absolutely irreducible. This is
the precise imported statement sufficient for the argument. The author
and parent were notified to correct the theorem citation and the historical
read claim before promotion. No claim to have read Momose's original proof
is made in this review.

The author corrected the draft to this exact p.191 statement and removed
the incorrect Theorem 0.1 and whole-Section-3-read claims. The corrected
irreducibility paragraph and final scope paragraph were reread; the
ordinary-family proof and its actual-admissibility corollary are now a
clean PASS with the stated imported-theorem convention.

The source PDFs and SHA256 metadata are in `main_gate/literature/`; the
exact pages inspected here are saved as PNGs under `lean_chain/primary/`.

## 6. What the obstruction now proves

For each displayed smaller modulus at e₀=26,28,30 and each prime ell
dividing it, the progression e=e₀+(ell−1)t has actual `Adm3U_s` members
whose whole residual semisimplification is
`cyc^e ⊕ 1 ⊕ cyc^(−e)`. Their trace difference from that triple is a
nonunit at every group element. Thus an exclusion test over the entire
actual admissible comparison class fails even after imposing ordinarity,
the precise level, `WitA`, and `Th.Unl`.

The separately checked K2 periodic vanishing criterion and the completed
K52/K56/K60 calculations still show the corresponding K-group components
vanish on these progressions. There is no contradiction: `OneCharU_s`
uses an existential finite set selected from the deformation problem.
Predicate membership and residual semisimplification do not supply a
converse realization in that selected deformation ring or finite set.
Any further arithmetic criterion must distinguish this extra structure.


## 7. Literal GD parameters and a fixed large prime

Whole-read the added KT-ORDINARY-SYM2-GD and KT-ORDINARY-SYM2-EXPLICIT-LARGE corollaries, and both complete small certificate programs. PASS. Reread the entire ClassNumberThree.gd proof64–86: for E=Q(sqrt(-3)), N=2 and trivial psi, every positive even e and ell>=5 with (ell-1) not dividing2e gives GD, without an upper weight bound. The three exact factorial gcds equal1, so every prime divisor of each M is larger than2e0+1. The same nondivisibility persists in e=e0+(ell-1)t.

The full-factor Lucas proof is exact: n-1=2*5*31*1019*2207879; all factors are prime by exhaustive trial division through at most1485. For each q, the displayed witness is Fermat1 modulo n, while its (n-1)/q power differs from1 by a unit modulo n. For every p|n, this forces the q-part of n-1 into p-1; hence n-1 divides p-1 and p=n. This proves n=697446897311 prime, above2^31 by695299413663. Thus the actual admissible obstruction and K-component vanishing coexist at a fixed prime above the carried small-prime cutoff in unbounded weights.

Both scripts were copied byte-identically to this audit directory and freshly executed; both entire JSON reports are byte-identical to the author results. See `ordinary_gd_largeprime_reconciliation.json` and the two replay logs.
