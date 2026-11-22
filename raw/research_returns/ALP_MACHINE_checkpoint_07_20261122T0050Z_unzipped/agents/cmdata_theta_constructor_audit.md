# Source audit: why CMData plus generic thetaG does not instantiate the mixed family

Run ALP_MACHINE, `/root/lift_accounting`, 21 November 2026 UTC. This is
an exact source audit and refinement of the current gate, not a new
theorem replacing accepted DP52 or DP57. The generic-interface distinction
is already stated immediately after the proof of DP52 in the intake.
No Lean execution is claimed.

## The field repair is real but has a deliberately narrower target

Accepted DP57 proves that \(E'=\mathbb Q(\zeta_{28})\),
\(F'=(E')^+\), and \(A=J^2\) furnish the indicated integral CM
action, principal product polarization, unramified CM field condition,
and an actual generic adelic endpoint. In particular it really meets
`CMData`, whose four fields are `cmUnram`, `totReal`, `deg2`, and
`fixed` in `Formalism/LocalRingCardinality/DataSpaces.lean:14–19`.
The geometric type is induced from no imaginary quadratic subfield.
DP57 explicitly does not construct the old `Datum.dom`/`CMObj.HasType`
input; its separate old `8 ∣ f` wrapper also fails since \(f=6\).
Those are carried findings, not new obstructions derived here.

`CMData` is sufficient for the generic `Spaces` layer, subject to its
other geometric inputs. It is not the type of the input of the source
`thetaG_exists` theorem. That theorem begins with `variable (D : D7)`.

## The actual input to thetaG is substantially larger

`Formalism/LocalRingCardinality/RhoDetPrimeEqMuTildeMulChiPow.lean`
defines `D7` from line 76. Besides `Ranks` and `Spaces`, it includes:

* The full old `Host`, `Rows.Data`, all member column chains, their
  periods, fixed coefficient fields and integral row/column lattices.
* Exact ties between `perCol` and the member `PtilCol` maps, both at the
  base tuple and at twisted tuples; actual lattice embeddings and
  compatibility with archimedean norms.
* The local theory, local comparison systems, theta-jet data, finite
  places, stage characters, their arithmetic and Galois compatibilities,
  and the remaining global data.

This is not an inference from the name `D7`: these are visible fields
in its declaration. For example `perCol_base_eq_PtilCol` appears at
lines 169–171, `perCol_tie` at 181–183, and the theta-jet block starts
at line 311 in the recovered copy.

The old `Host` itself extends `Formalism.HC.HostAx`, rather than
`CMData` (`DataHost.lean:39`). Its predecessor `HostRaw` includes the
special Galois/cyclotomic field package and \(\sqrt{-d}\). Its CM
type is literally the set of embeddings taking that element to
\(i\sqrt d\):
`Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean:66`.
This is an induced imaginary-quadratic type. Supplying DP57's generic
field and geometric CM action therefore does not, by itself, supply
this old arithmetic `D7` package.

## What the generic constructor actually proves

`Formalism/LocalRingCardinality/SpanPowerMembership/ThetaFamilyAdmissibleThree.lean`
defines one auxiliary Hilbert space
\(HG=HR\oplus HC\oplus\mathbb C\) at line 16. Its row embeddings
land in the first factor, its column embeddings in the second, and
`v0` in the last (`rowJ`, `colJ`, `v0`, lines 18–33). The `thetaG`
structure is at lines 71–153: its automorphic spaces all equal `HG`,
the cusp/type spaces are the full space, group actions are identity,
Schwartz spaces are all endomorphisms, and periods are inner products.
The specified lowering operator is `rowJ ∘ io ∘ rowQ`.

For an already supplied `D7`, the final theorem at lines 277–279 gives
exactly

    ∃ X : ThetaX D,
      TieRowIsom X ∧ TieIo X ∧ AdmS D X ∧
      TieRowTyp X ∧ TypStable X.

It proves all six components of `AdmS` at lines 215–274. The Rallis
representation used for this construction is the line spanned by the
extra vector `v0` (line 216). In particular the construction's existence
does not prove that the actual abelian theta germs occur in its
prescribed row/column images. This is an auxiliary realization of the
interface, already recognized as such by accepted DP52.

There is a further explicit omission: the theorem does **not** supply
`TieBm`. In `DataTheta.lean:747–752`, that predicate identifies the
actual terminal bilinear period `D.what₂.perCol` with the specific
`Btop` expression on the conjugated column and embedded terminal row,
including its `mY` factor. `TieRowIsom` and `TieIo` are distinct
predicates at lines 739–745. Their proofs do not establish this
terminal identification. No claim that `TieBm` is identically zero or
impossible for the generic construction is made: its noncanonical
conjugation is not silently assumed to preserve the three factors.

## Exact conclusion for the proposed shortcut

The proposed implication “DP57 supplies CMData for J², and thetaG
supplies the six identities, so only one finite coefficient matrix
remains” does not follow from these sources. The theorem providing
thetaG requires the still-unconstructed arithmetic `D7` first and its
conclusion omits `TieBm`; more importantly its theta maps have not been
identified with the classical mixed-CM correspondence or the abelian
theta kernels. The numerical source `SizeData₂` also remains tied to
the selected arithmetic derivatives and lattice errors, rather than to
the bare CM orbit certificate.

There are useful concrete pieces: accepted DP52/DP57 provide the
generic endpoint, AM-R-004 supplies the actual analytic CM torus and
theta germ, ALP-LIFT-05 gives its full stable Hodge normalization,
ALP-LIFT-06 computes the directional bare-certificate/Cauchy equality,
and ALP-LIFT-07 fixes its exact characteristic and theta-null finite
normalization. They reduce the unknown analytic normalization and
identify a genuine source-line mismatch. They do not yet fill the
mixed arithmetic constructor, the actual six identities on its tied
theta family, or the final quantitative selected-value comparison.

The smallest honest next local target is to construct the prescribed
trace-one section and allowed odd-level translates in explicit CM
coordinates, compare their reduced gauges to the integral connection
lattices at the selected primes, and identify the resulting finite
coefficient matrix with the actual theta-lift row/column map. Even that
local matrix identification is not a substitute for all global
constructor and norm hypotheses. This source audit makes no universal
nonexistence assertion about mixed-type theta correspondences.
