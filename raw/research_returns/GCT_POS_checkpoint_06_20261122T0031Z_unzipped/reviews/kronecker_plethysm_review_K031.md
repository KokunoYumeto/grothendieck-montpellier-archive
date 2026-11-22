# Targeted complete proof check of K-031

Date: 2026-11-21. Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro;
effort not exposed; run GCT_POS.

**PASS.** Read all of `ALL_STABILIZER_SYMMETRY_REDUCTION.tex`, including
the sole-exception corollary and exact source/scope paragraph. No gap
was found. This is a targeted peer whole-proof check: the reviewer had
contributed to the earlier Sylow/normalizer approach and the Luna-chart
route. It is not labeled an independent discovery. Root supplied a
separate complete reading of the new proof.

## Full orbits and generic stabilizer type

For a nonzero quotient point the grading orbit has only the origin in
its affine boundary. On the homogeneous invariant principal open this
grading orbit is closed. Any full stabilizer has finite determinant
image because it fixes a nonzero semi-invariant value; thus a full orbit
has dimension exactly one greater than its effective special-linear
orbit. A purported boundary point in the same chart lies over the same
grading orbit. Its special-linear orbit cannot be the closed one and
must have strictly greater dimension than that closed orbit. Its full
orbit would then have dimension greater than the original full orbit,
contradicting the dimension drop on an orbit boundary. This argument
does not require finite stabilizers.

The chart is smooth affine and the acting full group is reductive.
The complete primary Luna III.2 Corollaries 3–4 and their proof on
printed p.100 were previously read by this reviewer. They apply to this
chart and give finitely many locally closed model strata. Pullback from
the full quotient to the special-linear quotient is legitimate because
the just-proved full-orbit closure statement identifies the relevant
closed orbit. The resulting finite constructible partition has a generic
type H, and intersecting its three cyclic translates gives a nonempty
cyclically stable dense open subset.

## Arbitrary normalizer and finite reduction

The algebraic normalizer in Gbar semidirect C3 surjects onto C3. Jordan
decomposition keeps its semisimple part in the normalizer; the unipotent
part maps trivially to the finite quotient. The cyclic semisimple closure
is diagonalizable. Splitting its finitely generated character group
produces a finite factor, and its three-primary part maps onto C3. This
gives a finite three-primary lift r, with no reductivity assertion and
no claim that r has order exactly three.

J=H<r> is a closed finite union of H-cosets with J°=H°. The symmetric
determinant character extends to the semidirect product, has finite
image on J, and is trivial on H°. A finite subgroup F meeting every
component of J therefore has N=F∩H normal in F and χ(N)=χ(H).
It also maps onto C3. A Sylow-three subgroup of F supplies an element
above the chosen three-cycle; its action on N has three-power order
and preserves χ. All hypotheses of the already checked finite lemma
K-030a hold. The resulting two-primary h has character ξ and a
cyclically stable ambient conjugacy class.

The finite-component-covering input was independently checked here
against the entire classical Borel–Serre Lemma5.11 proof, printed
p.152; see `borel_serre_component_subgroup_audit.md`. The modern
Lucchini Arteche proof is the author's/root's separately checked source.

## Folding, fixed points, and the exceptional class

The scalar torus is divisible, so the finite two-primary element lifts
with finite two-primary order to GL_n^3. Scalar-translation equivalence
of its spectra can be normalized to equal spectra since three is
invertible modulo the lift order. The common factor A then has determinant
of order M, because (det A)^3=ξ. The full P-F30 support theorem and the
already checked K026 balancing argument apply without a stabilizer-size
hypothesis. The dense generic locus is therefore the chain, and closedness
extends the result to W.

The stronger closed-point assertion follows by applying the theorem to
a cyclically fixed singleton. Nonzero chain points have inertia exactly
mu_M, so none can be fixed by mu_(M3^a). This asserts a fixed-point fact,
not the absence of higher-lift components or poles.

The equivariant coherent dimension induction now applies to every
residual irreducible locus. Outside the chain all such loci occur in
triples; the only terms not covered by the supported-module integrality
lemma are closures containing nonzero mu_(3M)-fixed points. The argument
preserves integral coherent classes and only subsequently inverts the
scalar moving-generator factor in the local Laurent ring. K029 proves
this remaining exceptional support is nonempty in infinitely many
dimensions. No exact-M pole or strict-index conclusion is claimed.
