# Progress ledger: /root/real_weil

2026-11-19: Read the assigned prompt, relevant transcriptions and prior
proofs. Completed D.1 parity obstruction and q=25 arithmetic; D.2 real
orbits and rational counterexample; D.3 arbitrary-order Brauer images;
E.4 finite-field computation and number-ring 2-torsion correction;
E.5 algebraically closed theorem, perfect-field counterexample and
crystalline examples; E.6 Artin–Tate comparison classes.

Primary-source checks are recorded in SOURCE_AUDIT.md. Exact computation
code and output are in code/. Paper fragments, references, results and
check events are ready for the parent's next checkpoint.

The actual-relative-gerbe module descent in D.3 has now been fully
expanded. E.4d adds the coefficient/Kummer consistency obstruction.
E.5e verifies smooth Witt-vector torsor uniqueness, with Steinberg's
original Theorem 1.9 checked for perfect fields of cohomological
dimension at most one. The fragments and ledgers are stable for the
03:34 UTC checkpoint preparation.

Outstanding work retained explicitly: E.4 open localization and
real-place comparison, and D.4 general geometric polarization
compatibility. No general solution is claimed for those gates.

After checkpoint 01 (19 November 2026, 03:50 UTC): the E.4 twist-one
localization gate has moved. E.4e constructs the normalized Gysin maps
from proper duality and gives coherent explicit complexes on all finite
open subsets; E.4f constructs sign deletion and checks localization and
proper duality. The remaining gate is all-twist multiplicative and
real-place comparison with a full motivic theory, not the existence of
the displayed twist-one localization complex.

D.4 has also moved: D.4c gives the exact quotient positivity criterion;
D.4d verifies CM/Lefschetz reduction cases. D.4e proves integral-spectrum
effectivity in the finite-field abelian--Artin--Tate category under the
explicitly cited 2026 van Hoften--Sempliner primary preprint theorem.
The general finite-field gate is now motives outside that category.
The general geometric specialization gate remains. The preprint's
analytic imports are not claimed independently re-proved.

After 04:00 UTC: E.5f constructs a nontrivial fpqc torsor over
Fbar_3(t)^perf for lim(G_m,square), although every finite quotient is
trivial and the field is perfect of cd<=1. The proof is explicit and
the example lifts to Witt vectors. E.5g proves connected-kernel and
compactness conditions that do permit coherent trivializations.
The missing lim^1 phenomenon is now a concrete counterexample, with
Milne 2003's precise characteristic-zero results opened and their
scope retained. Stacks Tag 0F0T verifies the cohomological dimension.
All finite arithmetic checks, source notes and result/check ledgers
have been updated for the next checkpoint.

19 November 2026, 04:14 UTC: E.4g proves the complete rational
compactified number-ring table for every twist, including the dual
negative-even groups, and a coherent rational localization extension
on every finite-prime open. Thus the all-twist arithmetic gate is now
integral: rational groups and restriction are determined, and integral
twists zero/one have the explicit constructions already given.
E.4h re-proves the continuous procyclic tables and makes the forbidden
characteristic-prime cyclotomic-lattice extrapolation explicit.
E.4i independently proves the R15 Brauer injection and the local
finite-etale Azumaya descent criterion. Exact primary Borel1974 and
Grothendieck1966 sources are now in the bibliography and audit.

The next E.4 route is to compare Geisser's Dedekind motivic complexes
and Spitzweck's motivic-spectrum purity with the real-place-retaining
Weil complexes. The specific obstruction is not rational purity:
it is construction of the integral all-twist Gysin and restriction
maps compatible with the chosen duality and real correction, and a
comparison with a full multiplicative motivic theory. Geisser's
Theorem1.2 contains a truncation and a residue-characteristic caveat;
Spitzweck's Theorem7.4 is in the motivic-spectrum category. Neither
can simply be renamed as the missing Weil-complex comparison.

All other open gates are unchanged: D.4 outside the stated abelian
and CM/Lefschetz cases; E.5 the unspecified integral motivic model and
undefined continuous-H1 phrase. These are not declared settled by
the general affine-gerbe counterexamples. Lead D1 is refuted in its
claimed protorus remedy; Lead E2's exact integral identification is
refuted and its corrected finite-field/rational pattern proved;
Lead E3 has the exact structured-moduli interpretation and a retained
definition gate. Root C.2h--j received an independent positive audit,
with a scalar-extension clarification accepted by the parent.

19 November 2026, 04:22 UTC: E.4j--k move the integral comparison
gate by refuting two precise extrapolations. The explicit totally real
quadratic torsor over Z[1/2] disproves naïve integral purity with the
verified finite-field negative-twist groups and ordinary finite
coefficients. The real cyclotomic tower then disproves finite
generation plus the desired rational restriction pattern and every
finite-coefficient comparison, even without purity. Root independently
read and checked both proofs before integration. Their assumptions
are expressly additional; the manuscript's rational localization
statement is not refuted. The remaining constructive direction must
retain actual wild support and, if all finite comparisons and the
rational pattern are retained, non-finitely-generated torsion.
The exact arithmetic script and output are in code/verify_wild_purity.*.

19 November 2026, 04:39 UTC: the separate E4_actual_support.tex
contains E.4l--p and has been sent to root for independent audit.
It computes actual constant-sheaf support as the dual of local
units in degree3 and every twist-zero open group by
Kronecker--Weber. Every negative twist has the explicit extra
RΓ(Qp,Qp/Zp(n))[-2] support. Geisser's exact Proposition5.1
and the local cd=2 bound prove full integral purity for n>=2.
The historically conditional norm-residue input was opened in
Voevodsky2011, Theorems6.16--6.17. E.4o compares the earlier
twist-one complex with the actual Artin--Verdier finite coefficients
using the rational sum-zero correction to the Brauer-invariant
kernel. E.4p assembles a coherent bounded integral family in all
twists with the proper corrected values, ordinary finite
coefficients, and the rational manuscript restriction pattern.
Its supports retain the necessary wild terms; after inverting the
residue characteristic it has all-twist purity. This closes
existence/comparison on this specified family, not identification
with every open Weil topos or construction of arbitrary-scheme
products. No additional finite-generation claim is made.

The requested independent audit of cycles/positivity_consequences.tex
C.1j--l passed. The nonzero decomposable correspondence satisfies
aba=0 for every b, yielding the full Jacobson criterion; the
universal codimension classification follows from the infinite
Griffiths summand on V times projective space. Clemens's exact
primary theorem and genericity qualification were independently
reopened. Parent and sibling were informed.

19 November 2026, 04:41 UTC: E.4l--p are integrated in part_E456.tex.
Root's derivation-level audit passed; frobenius independently checked
the exact Geisser/Milne/Flach--Morin primary purity passages and the
twist-one Ext and quotient arithmetic. These are separate recorded
checks; no claim is made that root had completed every primary-page
check when reporting its first audit. results.csv now has41 numbered
statement rows and CHECK_EVENTS.tsv has77 actual check-event rows.
The outcome report and earlier E.4 scope statements were updated to
distinguish the proved restricted all-twist family from unasserted
universal comparisons.


19 November 2026, 04:55 UTC: D.4f--g integrated after root's
independent audit. D.4f proves the precise equivalence of all-motives
effectivity, Frobenius-identity effectivity, and full Tate cycle
surjectivity in the explicitly stated numerical realization framework.
D.4g proves common geometric polarizations for arbitrary polarized
abelian families with typed specialization functors, under the cited
2026 theorem. General geometric positivity remains separate.
The sibling's further independent audit was requested before the
05:05 checkpoint. Parent requested a new local Picard counterexample
search for C.3; that investigation now begins.


19 November 2026, 05:03 UTC: C.3i, in separate C3_picard.tex,
proves an exact (C,+)^3 Picard restriction kernel for every local
N>=4, with regular source and hyperplane punctures and an explicit
Fermat/projective-bundle construction. Both root and frobenius
independently audited the proof and primary actual-group passages.
Requested inclusion wording and proper cone-contraction clarification
were applied. An exact finite certificate and output are saved in
code/verify_local_picard.py and .out. Parent will include it after
checkpoint03 layout verification. Its scope is full A1 and the local
Picard identity-component interpretation; ordinary Chow J1 is
expressly kept distinct. A possible positive theorem for ordinary
Chow J1 in characteristic zero is now being examined via abelian
images and Kollar's unipotent-kernel theorem.
