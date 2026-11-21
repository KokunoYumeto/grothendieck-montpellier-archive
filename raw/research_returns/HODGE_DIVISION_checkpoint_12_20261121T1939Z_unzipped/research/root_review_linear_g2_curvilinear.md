# Root whole-proof and source review: linear Weil, G2/triality and E820

Reviewer: `/root`, GPT-6 Astra Pro, reasoning effort inherited and not
externally exposed; HODGE_DIVISION, 21 November 2026. Mathematical
outcome: **PASS**, with the input boundaries recorded below.

## D-BI-23a/b/23: linear Weil representations

The complete proof and the exact endpoint checker were read. The actual
root execution reconstructed 24 compatible rows and all 1,288 nonscalar
spectra, with minimum moving rank eight. This reruns the supplied exact
checker; it is not a second implementation by the root. The sibling
imprimitive reviewer separately reconstructed the spectra by an independent
restriction selection and Fourier computation; its whole-proof report
was also read completely.

The determinant adjustment on a third basis vector proves the additional
SL irreducibility assertion for n>=3. The q+3 orbit count reaches the
minimum squared norm of the indicated decomposition, including both
trivial summands. The scalar projector, convex eigenspace-dimension bound,
deleted permutation character, and stronger q=2 estimate have the claimed
constants. The q>=5, q=4 and q=2/3 case inequalities were checked through
all stated endpoints. The real cases have an actual invariant symmetric
form line; an imaginary quadratic subfield of the full inducing character
field forces the multiplier to be nontrivial. The two half-moving inertia
argument therefore has its stated scope without a hidden field-equality
assumption. The transitive tensor and actual intermediate-cover arguments
give the claimed obstruction, without constructing any source.

The original published Gérardin Proposition4.2 and its whole proof,
printed pp82--83, were freshly read through the full article copy at
<https://www.academia.edu/126991842/Weil_representations_associated_to_finite_fields>.
The new SL restriction proof is distinguished from that published GL
input. The official ATLAS L3(4) webpage was read, including its general
WORK IN PROGRESS notice. At root request the structural assertions were
checked independently: the elementary ordered-basis count gives the
order; Breuer CTblLibXpls2.7-4 explicitly gives multiplier C4^2 x C3 and
cites printed ATLASp23; 2.6-4 gives Out=D12 and the three involution
types; 11.5-7 gives the diagonal, field and inverse-transpose operations.
Those precise primary passages were freshly opened and read by the root.
The new source paragraph was read in full. It does not misdescribe HHM's
exceptional-list Table1 as a table of the complete multiplier structures.

The universal-cover quotient by the characteristic prime-to-three center
does give the actual triple cover. Every simple automorphism lifts, and
uniqueness follows from perfectness. The cyclic subgroup types of D12 and
the scalar correction of the outer power relation cover arbitrary
compatible normalizers, not merely a chosen split extension. Every
underlying complete character table remains an explicit published input.

Final reviewed proof hash:
`fd19cb225ea0c284d89dddadfb07ca3f6622cf84eb373473138ca5780b37b053`.

## D-G2T-01--03: complete G2 and triality families

The whole canonical proof, bibliography, source log, GAP exporter, safe
source extractor, complete formal-phase parser, Fraction coefficient
checker and small-cover checker were read. Root actually executed the
source extractor, parser, coefficient checker and small spectra checker.
All 318 nontrivial generic row types / 9,242 cells and all 239 selected
small-cover rows / 11,502 spectra passed. The frozen original entry input
was reproduced with its exact retained hash. The full independent G34
audit was read; that reviewer reconstructed the original expressions and
small spectra without importing the author's parser or Fourier code.

The official complete inventory for all eight G2 and three triality
tables was freshly read. Their field conditions exhaust the relevant
characteristics and congruence classes. The official generic-cyclotomic
definition at <https://oscar-system.github.io/GenericCharacterTables.jl/stable/cyclo/>
was read in full through its mathematical definition: the phases are
exponentials of real rational expressions at every admissible integer
specialization. Their absolute values are one. The triangle bound after
q=q0+x is consequently valid for all x>=0. Treating unrelated formal
phases as independent only enlarges this bound. All translated degree
and class-length polynomials are checked as stated. No finite-q
extrapolation occurs.

The original published table classifications are inputs. The source log
truthfully distinguishes the author-retrieved Enomoto papers from the
Chang--Ree and Deriziotis--Michler tables accessed through the official
complete implementation. Root does not claim to have reread the full
proofs of those two inaccessible original papers. The exceptional
multiplier inventory and the small cover/outer conventions retain the
earlier primary-source verification; every nonlinear row and compatible
cyclic extension is included. The universal-cover lifting, scalar power
rescaling, commutator rank bound, factor-algebra permutation argument,
weighted cyclic-word bound, and final e<=24 contradiction are sound.

The first root rerun exposed a reproducibility defect: runtime seconds
were part of the retained coefficient file, changing its hash despite
identical mathematics. The author removed the timing field from that
certificate, retaining timing in the summary, then regenerated and
rechecked it twice. Root read that exact repair. The deterministic
coefficient-file hash is
`568425a2cf62e62dbe24709a3372d9bd182946e0a53ae74e7fed45ba640dcd13`.
This is an artifact repair, not mathematical movement or a new theorem.

Final reviewed proof hash:
`3c099689c794302e80e0a12d2123e605045fda12935672568b706e52d7fb1067`.

## SF-E820: common curvilinear local modules

Root read the entire frozen Markdown proof, its entire exact arithmetic
certificate and the complete canonical 296-line TeX conversion. The
author certificate was actually executed and passed. The independent
G34 whole-proof report was read completely; it independently reconstructed
the generic Jacobian mixed-wedge identity and the full 256-coordinate
rank32 character, importing no author code.

The quotient-valued map C:T->Q is lift-independent and R-linear. The
first-order lifted Koszul equations contain the actual Poisson brackets
of the chosen, possibly nonlinear, regular-sequence generators; all
discarded terms genuinely vanish modulo I. No assumption that the new
coordinates keep the bivectors constant is made. The normal cotangent
3-plane cannot be isotropic for both complementary rank-two forms, so
one coefficient is a unit. The equal-length conclusion makes C square,
and the unit forces invertibility. The two separately existing
deformations then force exact A-proportionality of all bracket entries.
Their mixed wedge is a nonzero multiple of ell*t^(ell-1), the Artinian
socle element. This contradicts proportionality to the self-wedge-zero
form. It proves every length, not a finite list of thickenings.

The global cap-kernel implication uses precisely the already reviewed
E819 published Buchweitz--Flenner identity and supplied finite-action
compatibility. The rank32 equal-module modifications are actual coherent
extensions with Ext dimension 6m^2*ell. Their full balanced character is
verified. No simplicity, indecomposability or coherent finite action is
asserted for those examples. Arbitrary Artinian modules, singular hulls,
positive-dimensional modifications and unrelated derived objects remain
outside the theorem. The conversion is complete and preserves all limits.

Final canonical hash:
`8793f538a746d0e5f2fb77fd4eafb633dafeb50844bba49f0f5b9347779444bf`.

No TeX compilation is claimed in any of these reviews.
