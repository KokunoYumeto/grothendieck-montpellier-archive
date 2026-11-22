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

19 November 2026, 05:38 UTC: C.3j and C.3k are now integrated by the
parent after separate root and frobenius audits. C.3j proves ordinary
algebraic-equivalence injectivity in dimension at least four by whole-family
descent and proper abelian images. C.3k proves prime-to-residue torsion
injectivity for arbitrary excellent normal strictly henselian rings of
dimension at least three, then extends ordinary injectivity to that
dimension range in the algebraizable characteristic-zero scope. The
two distinct checks of parts(i) and(ii) are retained in the event ledger,
while the statement register has one aggregate C.3k row.

The new C.3m counterexample is complete in C3_surjectivity.tex, with
both independent audits passed and parent approval to integrate after
the exact code certificate. That certificate passed: determinant-one
Jacobian contraction, 337 deformed Segre identities and27 minors, all
over exact rational arithmetic. The construction refutes ordinary J1
surjectivity in every dimension at least four, using actual line bundles
and a complete formal-to-strict-local descent. The canonical ring is
defined by the original affine equations and normalization; the proof's
smooth neighborhood is only auxiliary. Five primary PDFs were obtained
and hashed. All citations, source-opening scopes, proofs and computations
are recorded; this agent now has47 statement rows and101 check events.

19 November 2026, 05:49 UTC: C.3n is finalized as
C3_general_picard.tex after full independent root and frobenius audits,
including fresh visual verification of Boutot's printedVII. The result
removes the algebraizability gate and extends ordinary rational J1
injectivity to every characteristic, in the explicit excellent normal
strict-local coefficient/residue-field scope with dimension at least
three and regular punctures. Characteristic zero gives integral
injectivity; characteristic p gives a p-primary kernel. The proof
constructs actual dual-Jacobian families directly from the proper
parameter curve, so no resolution theorem is needed. Parent approved
immediate integration after C.3m for checkpoint04. This agent now has
48 statement rows and105 actual check-event rows.

19 November 2026, 06:12 UTC: C.3o is finalized and registered after
independent root and frobenius audits. It gives the explicit remaining
complex dimension-two injection and dimension-three surjection failures,
with a strict-local single-exceptional-divisor proof and an infinite-order
class; the exact N1/N2/N>=3 threshold table is included. Over Fpbar the
ordinary Pic_alg group is torsion by the actual-family lemma, so the
positive-characteristic scope is not overstated. There are now49 owned
statement rows and108 actual check-event rows.

The separate C.3p draft proves the complete finite-etale comparison
and local Picard functor completion comparison using Elkik's original
Theorems3 and5 and their precise corollaries. Both independent agents
are auditing this typed draft; it is not yet a registered result.
The ordinary actual-product-family gate in positive-characteristic
surjectivity is retained. A torus-extension counterexample in normal
dimension>=4 is excluded by Kollar2016 Theorem1.7(ii); the nodal-elliptic
Example4.4(2) is a surface phenomenon and is not promoted to that scope.

19 November 2026, 06:37 UTC: C.3p and C.3q are finalized and integrated
after full independent root and frobenius proof/source audits. C.3p
settles finite-etale restriction and all invertible-order Picard torsion
in dimensions >=4, including mixed characteristic, and separately the
coefficient-field local Picard functor's completion invariance. C.3q
lifts every target abelian subgroup up to p-primary isogeny in the
normal essentially-finite-type characteristic-p scope, retaining the
actual fixed-product-family step as a precise remaining gate.

The same checkpoint interval finalized the all-codimension Fpbar
ordinary Chow torsion corollary in C.3o; both independent agents checked
the curve closure, flatness, principal-divisor relation and proper
pushforward in the explicit excellent-base Chow formalism.

C.3u now closes the actual-family gate for smooth projective cone
sources in every characteristic, with arbitrary regular divisor
punctures and dimension >=4. It proves actual Pic_alg(X)=Pic0_red(V)(k),
integral restriction surjectivity, and zero kernel in characteristic0
or finite p-primary kernel in characteristicp. Its direct torsion
calculation uses the proper cone resolution and the exact Stacks0A48
henselian finite-etale equivalence, avoiding an unproved splitting
of the full local Picard group. Frobenius independently passed the
complete typed proof and all three newly opened primary sources.
Parent approved integration after checkpoint05; root's own full audit
is continuing. The final file is C3_smooth_cone.tex; cycles has been
notified. There are now52 owned statement rows and122 actual check
events. New source PDFs and reproducible hashes are preserved.

19 November 2026, 07:01 UTC: C.3w is finalized and registered after
root's full independent proof/source audit and its separate check of
the exact quasi-affine Picard-kernel replacement. It realizes every
point of a proper abelian local-Picard subgroup by actual ordinary
curve families in the stated algebraizable strict-local scope, using
a regular alteration, an exceptional-divisor lattice, a rigidified
formal-unit gerbe with an explicit Cech acyclicity proof, proper GAGA,
whole-family Artin approximation and finite-flat norm on the
codimension-one locus. Divisibility removes the alteration degree.
Thus C.3q now gives integral ordinary Picard surjectivity in
characteristic p for N>=4 in its algebraizable scope, with p-primary
kernel from C.3n and a rational J1 isomorphism. No universal actual
family on the whole abelian subgroup is claimed. The arbitrary
nonalgebraizable excellent-ring extension remains outside the theorem.
Cycles has been notified to integrate C3_alteration_family.tex after
root's reserved C.3v. Sources and hashes are recorded; there are now
53 owned statement rows and127 actual check events. Frobenius's
second independent audit remains pending its higher-priority task;
it has not been counted as completed.

### 07:10 UTC — all-positive-characteristic degree-one boundary closure

C.3x typed and registered with exact certificates. It gives the complete
ordinary rational J1 table in the algebraizable characteristic-p scope,
with explicit characteristic2/odd-characteristic cone models and
transcendental non-torsion classes. Parent and frobenius asked for
independent audits; no unreceived audit is counted. Milne8.1/8.2 and
Stacks0F2H freshly opened. C3v full own proof/source cross-check is now
registered under aggregate id C.3v. C3w cycles full targeted check is
recorded, and superseded drafts are comment-only pointers.

Root full C3x proof/source audit passed and was logged at actual07:10 UTC.
Cycles asked to integrate immediately after C3w and optionally review.

### 07:37 UTC — C.3y finalized after two independent audits

Explicit all-characteristic multiplicative divisor quotient registered:
55 owned statements,139 actual checks. Root completed its full audit at
07:20:33UTC; cycles separately passed and reopened ElkikIIIp573. Exact
certificate runtime0.071582seconds retained. C3x cycles audit is also
recorded and its certificate runtime was added/rerun once.
Next: independently audit root C3z and derive the C3aa Segre-Nori
non-top higher divisor-quotient counterexamples.

### 07:47 UTC — C.3aa registered; C.3z fully audited after repair

C.3aa is finalized with full root and cycles independent passes. It
refutes finite integral local B^r groups over C for every
`2<=r<=N-2`, using the exact C.1i primitive cycle and a projective
bundle quotient, with C.3e supplying the strict-local actual class.
The top range `r=N-1,N>=3` remains a separate gate. There are now
56 owned statement rows and146 actual check events.

Root C.3z has passed the full independent read, including the repair
to its final step: full functor-level completion comparison transfers
NS finite generation, and a scheme-theoretic p-power argument handles
even nonreduced multiplicative kernel factors. Its regular model map
and alteration remove the algebraizability hypothesis from C.3w in
the exact excellent coefficient/residue-field scope. The review and
fresh primary-source locators are saved. Cycles confirms C.3y, C.3z,
and C.3aa are integrated in that order.
### 2026-11-19 08:13 UTC: C.3ab finalized

Root and frobenius both completed full proof and exact primary-source
audits of the surface-cone top-cycle theorem. Final fragment:
`C3_surface_cone_top.tex`; old draft retained as a supersession pointer.
Five new bibliography entries and exact source audit/hashes are saved.
The symbolic differential/gluing and Fermat-line certificate passed,
runtime0.175422seconds. Metadata generator now writes57 statement rows
and151 check events. Integration requested from cycles. The result is
an integral positive subfamily, with the unrestricted top B gate
explicitly retained and no movement-reset claim.

## 2026-11-19 08:42:38 UTC — C.3ad finalized

Full root and frobenius proof/source audits passed. Final file
`C3_rational_top_cones.tex`; old draft replaced by a comment-only pointer.
New bibliography/source records and formula certificate runtime retained.
`TOP_QUOTIENT_RESEARCH.md` explicitly captures the proper-K2 construction
and unresolved actual-family lifting step. This rational Qbar-cone theorem
is restricted evidence, not main-gate movement or an integral finiteness
claim for higher dimensions. Integration requested immediately.
