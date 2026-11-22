INCOMPLETE

## Part I auxiliary work, 19:58 UTC

The new lemma I7b removes completeness from quotient openness onto the actual image of a residual-column differential above the first arrow. Products of whole source columns remain open quotients and have dense images in cycles. The files `I_strict_dense_columns.md` and `.tex` give the full proof and the exact conditional extension to arbitrary complete additive targets. This does not by itself solve the endpoint or source-family assembly problem.

A separate candidate `I_degree_one_CRT_candidate.tex` now supplies a complete argument for degree-one continuity in the broad category. Semilocal Chinese remainder interpolation controls all finite source tails uniformly; finite generators of Ext^h(A/I,A) and a bounded parameter-power remainder control each exceptional source column. It was submitted to the parent for separate audit. It is not promoted before that audit, and the full higher-degree presentation remains Undecided. The remaining E4 full-schematicity gate is unchanged.

## Further check at19:09 UTC: finite-conductor pinching

Proposition E4.Pinching records why a direct rational-normalization construction cannot produce a nonschematic Picard functor. A finite surjection with finite conductors from a locally projective family lets an ample line bundle descend: trivialize it on the finite conductor near the chosen base point, glue it to the trivial bundle, and use finite-surjective descent of ampleness. Brion2015 Proposition2.4(i), preprintp6, was opened and its proof checked. The general remaining gate is unchanged; an arbitrary pinching is not assumed flat, and simultaneous normalization is not assumed to commute with base change.

## Update 2026-11-20 18:38 UTC: exact remaining schematicity gate and provenance

The full Picard scheme question on 57:315 remains unsettled for higher-dimensional geometrically normal families and for geometrically integral singular curve families over arbitrary scheme bases. Smooth curves, hence geometrically normal curves, are settled; the standard nonsplit-conic example does not satisfy geometric integrality. The detailed file `E4_schematicity_attempts.md` records the attempted torsor, singular-genus-one, relative Chow modification, normalization, and group-space realization routes and their precise missing steps. No arbitrary group-space example is presented as a Picard counterexample.

The smooth-curve proof is an existing derivation: Kestutis Cesnavicius gave the BLR6.6(2c) plus finite-quotient argument on MathOverflow on28April2015. That provenance is now explicitly cited alongside the independently opened BLR and Stacks/SGA3 theorem dependencies. No priority is claimed.

The two marginal notes on57:310 are separated from their mathematical outcomes. Multiplication openness is **refuted** by E4.H; its pale qualifier does not leave that mathematical row open. For the proper-flat-fp cohomologically-flat Picard setting over noetherian bases, finite presentation of Pic-tau already supplies both defensible finite-component conditions. The exact broad iff wording remains uncertain. A fully specified infinite-branch etale group shows why a generic-component-count-only criterion for arbitrary locally finite-type groups would be false; this is not a Picard realization and is not counted as new movement on the main gate.

A targeted separate AI audit of FHI's F10/F10b was completed at18:28:56UTC. Krishna-Majumder2026v2 Theorem9.4, Corollary9.7, Lemma3.2 and the hypotheses onp2 were read. The rank-one conductor bound, finite inertia deduction, and fixed-cover purity descent passed the audit. The audit does not cover F10c/F11 or certify the full new preprint.

## Update 2026-11-20 17:49 UTC: full Picard scheme for smooth curves

Theorem E4.Curve proves schematicity of the full Picard functor for every smooth proper geometrically connected curve family over an arbitrary scheme base. The genus-one case is the significant one: C identifies with Pic1, and Picn is the finite-flat quotient C/E[n]. BLR Section6.6 Theorem2(c), pp164–166 supplies a common affine neighborhood for each finite orbit because C is a scheme torsor under its elliptic Jacobian. Stacks07S6 makes the quotient schematic, including p-divisible n. The primary BLR text also gives the Jacobian as an abelian scheme in Section9.4 Proposition4 p260. Parent independently opened all named primary statements and passed the complete proof. The other genera are relatively projective by the canonical bundle. Noetherian approximation gives arbitrary bases. This rejects the suggested genus-one torsor route to a nonschematic full Picard functor, but leaves the arbitrary-dimensional normal/integral-family question open.

## Update 2026-11-20 17:42 UTC: fibrewise smoothness refuted

Theorem E4.S supplies a fully specified characteristic-two family of geometrically integral reduced surfaces: quotient the cubic C:y²z+txyz+tyz²=x³ times the fixed ordinary elliptic curve B:y²z+xyz=x³+z³ by inversion on C and translation by P=(0,1) on B. Rigidified descent gives Pic-tau(X)=Y-dual times G[2], with G=Pic0(C), Y=B/P. Its generic fibre is Y-dual times mu2 times Z/2, hence nonsmooth of dimension1; its special fibre is Y-dual times Ga, hence smooth of dimension2. Thus fibrewise Picard smoothness is not an open condition, and tangent-dimension defect is not upper semicontinuous. The relative smooth locus is still open; those are distinct statements. All polynomial checks passed in0.067239159seconds, and DGJ separately audited the generalized-Jacobian descent argument. This settles the plausible mathematical readings of57:309(b-prime) while retaining the pale abbreviation and avoiding any invented direction of semicontinuity.

The separate prime-to-characteristic rank inequality E4.rank.2 now has its exact orientation and proof: special2alpha+mu does not exceed generic2alpha+mu in the geometrically reduced setting, by separated etale prime-to-characteristic torsion. Original FGA VI pp234–235 were visually checked. The arbitrary-base full-Pic schematicity gate is unchanged.

## Update 2026-11-20 17:23 UTC: projectivity removal proved

Theorem E4.T proves that for every proper flat finitely presented scheme family with geometrically integral fibres over an arbitrary scheme base, the locus where a given invertible sheaf is numerically trivial is open and closed. Equivalently, Pic-tau is closed in the full Picard algebraic space. Projectivity is unnecessary in 57:314. Over a complete trait, Zheng2009 Lemma3.8 gives a regular projective Galois alteration, allowing a purely inseparable invariant field. An intersection-matrix correction and the Hodge index theorem make a rational vertical adjustment numerically trivial on every component. Galois transitivity above the unique target vertical valuation, followed by birational negativity on the normalization, removes that correction. Noetherian approximation using constructibility of the geometrically integral fibre locus then gives arbitrary scheme bases.

Exact primary sources were opened: Zheng pp313–314, Kleiman2005 Theorem6.3(h) and proof pp53–54 and Hodge Index TheoremB.27 p79, Kollar2022 Lemma11.60 p436, and the named Stacks limit/trait lemmas. Root separately audited the full proof and arbitrary-base reduction; DGJ separately audited the trait intersection/negativity core in work/dgj/audit_E4_tauclosed.md. Both AI audits passed. This is not a claim of independent human verification or priority. The complete fragment is new_E4_tauclosed.tex and is integrated into section_E.tex.

The remaining substantive E4 gate is schematicity of the full Picard functor for proper flat geometrically normal/integral families over arbitrary scheme bases. The ambiguous marginal notes retain their exact scope gates. The entire assigned task remains INCOMPLETE.


## Update 2026-11-20 16:57 UTC: original scans and final scope consolidation

The official Montpellier PDF was accessed at https://grothendieck.umontpellier.fr/57.pdf. Its selected scans309–315 were extracted directly using HTTP byte ranges, with source URL, exact byte ranges and elapsed time in `code/extract_mpl57_ranges.output.json`; the full129MB document was not downloaded. Original scans309–315 were visually inspected, with enlarged crops of the uncertain309(b′) and310(6)/margin. Earlier manuscript readings outside these selected original pages rely on the supplied exact transcriptions unless another explicit visual-inspection event says otherwise. The preferred reading of309(b′) is “demi-continuité de (Dim. Lissité) des fibres”, but the first abbreviation remains pale and is not silently normalized into a new invariant. The310 Howard footer really only names multiplicity, specialization, flatness, and existence/descent; it specifies no additional descent object.

H6 is now stated in both requested forms: the prompt summary's flat finite-presentation subgroup gives an algebraic-space quotient without closedness; the full HUNCHES wording additionally assumes closedness, giving the separated unramified scheme quotient. The nonsplit-conic quotient is consistent with the former and shows why the stronger conclusion needs more. Parent's separate AI audit accepted E4.Q. B2's exact result excludes a criterion depending only on abstract geometric fibre types and the base; it does not exclude criteria using deformation data. Literal E1 is refuted; its intended relative-normal trait extension statement is proved. These are separate from the remaining arbitrary-base schematicity question.

Current unresolved B/C/E gates are the nonprojective geometrically integral but nonnormal tau-closedness assertion, arbitrary-base schematicity in the normal/integral cases, and the mathematical scope of the incompletely formulated marginal notes. The parts explicitly proved or refuted in `results.csv` must not be reverted to their older historical statuses below. All historical update paragraphs remain as an audit trail, not as the current register.

## Update 2026-11-20 16:28 UTC: numerical quotient and scope corrections

Theorem E4.Q refutes the scheme-quotient question in its written generality using the known nonsplit conic with trivial tau subgroup. Its full Picard algebraic space, hence numerical quotient, is not a scheme. This does not address the strengthened variant assuming full Pic schematic or tau closed. The exact known source is Kleiman Example4.14 pp31–33; the new deduction identifies tau with the identity. E4.H also refutes multiplication-by2 openness even for a smooth projective family, and computes three explicit nonconstant multiplicities. B2 has no fibre-type-only criterion because identical base and fibre types give opposite answers; the fixed-family class-group kernel is the exact supplied iff. H12 is proved in its original cone scope and refuted as an arbitrary-local extrapolation with the punctured-spectrum convention.

## Update 16:16 UTC: explicit Heisenberg counterexample

E4.H now fixes m=96 and 21 equations of degree768 by universal norm coefficients in24 coordinates. Every coefficient and index set is specified; no unspecified degree or basis remains. Length192 first-jet interpolation proves generic smoothness and avoidance of the bad locus. Root structural audit passed. Signed-coordinate and finite-cardinality checks are recorded, without claiming polynomial expansion. Root also audited the full C2.G proof and found no gap.


# Parts B, C, E: working research report

AI-produced by GPT-6 Astra (OpenAI), delegated research run `/root/bce`, 20 November 2026. No priority claimed.

This is a working file, not a claim that all assigned questions are settled. Current
proofs are in `section.tex`; the exhaustive individual status table is `results.csv`.
The latter retains every mathematical leaf on 57:308–315, including duplicate and
ambiguous questions. The files are incremental research materials for the root
checkpoint, not a finished delivery.

## Current update, 20 November 2026, 16:07 UTC

Theorem E4.H closes two further gates, subject to the root audit now requested.
The rank-eight finite flat Heisenberg group over W(k), k algebraically closed
of characteristic2, has group law (z,a,b)(zprime,aprime,bprime)=
(zzprime(-1)^(b aprime),a+aprime,b+bprime). Its character scheme is exactly
mu2 squared times (SpecR disjoint Speck). Raynaud1979 gives a smooth projective
surface X with a complete-intersection torsor Y under this group. Complete
intersection Pic-tau vanishing, and explicit descent of the trivial bundle,
identify Pic-tau(X) with that character scheme. The extra open component is
supported on the closed point, proving nonopenness even for smooth families.
Over R/4, the represented neutral component is mu2 squared and flat, while
the extra component remains nonflat. Thus flat Pic0 does not imply flat Pic-tau.
The group identities and generic character count were checked exhaustively;
the high-degree Bertini construction uses formal independent coefficients
and the opened theorem, not a claimed computer smoothness test.

## Current update, 20 November 2026, 15:54 UTC

**C2 is proved in full**, in the stronger form of every excellent henselian
local base, every characteristic, and arbitrary proper X with finite-length H1.
Theorem C2.G blows up the maximal ideal and takes a Stein factor so the
exceptional ideal becomes Cartier and the first direct image is supported
there. The elementary principal-ideal argument yields local finite determination.
The descended line bundle on the auxiliary Stein space is finitely determined
because its H1 and H2 have finite length. A conductor square then descends
triviality, with Stacks 02OB(3) supplying the exact uniform lifting of units.
Artin--Popescu density and injectivity finish the henselian comparison; an
Artin--Rees fibre-product square removes vertical torsion. A separate AI audit
by GPT-6 Astra /root/fhi checked these gates and found no gap; this is not a
claim of independent human verification. The full proof is in section_C.tex
and the audit trail in C2_audit.md and the sibling audit.

**H11 is proved in full over a one-dimensional integral noetherian base after
shrinking**, for arbitrary proper surjections. Quotienting by the affine flat
kernel gives a quasi-compact monomorphism of group schemes, finite on every
fibre. SGA 3 XVI Lemma 4.2 makes that map affine; the kernel torsor is also
affine. Theorem H11.G is in additional_leads.tex. The original normal case is
retained as a useful independent route, but is no longer the extent of the result.

The remaining E4 gates concern p-primary universal openness for normal
morphisms; flatness of tau assuming represented neutral part flat; the quotient
without flatness of tau; closedness of tau for proper integral nonnormal
families; arbitrary-base schematicity; and precisely ambiguous inscriptions
on 57:310. Earlier dated progress paragraphs below record historical states
and are superseded by this update and results.csv.

## Checkpoint update, 20 November 2026, 15:32 UTC

C2 is now proved over an actual excellent henselian DVR in every characteristic,
for arbitrary proper X. The proof bounds H1 of all closed thickenings uniformly
using the finite-length H1 and the torsion part of the finite module H2. A line
bundle trivial at sufficiently high order then has uniformly killed H1, so its
trivializing section lifts after a bounded loss of order. For nonflat X, the
flat closure and a sufficiently thick closed fibre recover X by a fibre-product
algebra; line bundles patch. The remaining C2 gate is higher-dimensional local
algebras over an excellent DVR in positive or mixed characteristic. This is a
strict reduction, not a claim that the full higher-dimensional item is complete.

## Checkpoint update, 20 November 2026, 15:25 UTC

The reduced-fibre dimension question is now refuted by Theorem E4.R.
Take a ruled surface over an elliptic curve and vary the conormal of its
zero section through a Poincare line bundle. Glue two copies along the doubled
section. The resulting finite flat double is projective and flat, has
geometrically reduced connected fibres and universal H0=O, and its neutral
Picard groups are E times Ga to the power h0(P_s). Their dimensions are one
away from the origin and two at the origin. The proof explicitly checks
arbitrary base change of the fibre-product algebra and the units sequence,
including the scalar-unit quotient. This also refutes universal openness even
under the reduced-fibre hypothesis.

Both inequalities in 57:313(ii) are proved in the represented proper-flat
Picard setting, with unprimed invariants special and primed invariants generic.
Gille--Guralnick's Theorems 1.1 and 4.1 give upper semicontinuity of unipotent
and maximal affine commutative subgroup dimensions without flatness. For the
abelian inequality, the flat closure of generic tau has the same special
abelian rank: finite etale Kummer torsors lift over a proper henselian base,
forcing the quotient by the closure's reduced neutral special fibre to be
unipotent. The nonseparated represented case passes through Raynaud's
separated quotient. The precise trait schematicity theorem, finite-presentation
conditions, and reduced neutral groups are included in the proof. The claim is
not silently extended to a nonrepresentable Picard functor.

The remaining gates include C2 in general excellent-DVR characteristic,
H11 for arbitrary nonnormal generic fibres, p-primary universal openness for
normal morphisms, tau closedness for proper geometrically integral nonnormal
families, and arbitrary-base schematicity questions. Each remains explicit in
results.csv.

## Checkpoint update, 20 November 2026, 15:12 UTC

An explicit new counterexample (Theorem E4.N in `section_E.tex`) refutes
properness and projectivity of Picard tau for normal projective families.
Three diagonal quadrics in P5 over C[[t]] give a K3 family with exactly four
ordinary double points in the special fibre and regular total space. The
sign involution is free generically and fixes those nodes. Its quotient has
normal geometrically integral fibres. The generic order-two cover line bundle
cannot extend, by the sign of its linearization at fixed points. All twenty
three-column determinants and the local smoothing equation were computed
exactly. An R-section ensures that an extension in the Picard sheaf would be
an actual line bundle. This also refutes openness implying properness: in
characteristic zero the normal-family tau-part is universally open.

H11 is now proved for projective families with geometrically normal generic
fibres after shrinking a one-dimensional base. Proper flat tau-parts give
separated unramified quotient schemes of dimension at most one; the quotient
map is a quasi-compact monomorphism and hence affine by Zariski's Main
Theorem and Stacks 09N9. The remaining map is proper and quasi-affine, hence
finite. The arbitrary nonnormal branch remains separate. A previous shorthand
claim that smooth birational maps preserve the full Picard group was incorrect;
blowups add exceptional divisor classes. The proof does not use that claim.

## Checkpoint update, 20 November 2026, 15:00 UTC

H8 is now settled with its necessary dimension correction: the kernel is exactly
the free lattice on one-dimensional normalization branches; it vanishes when all
components have dimension at least two. H10, including the conormal criterion
without flatness, is proved from SGA 3 VI_B Proposition 1.6 and Deligne 1968.
Their full proofs are in `additional_leads.tex`.

New E4 results in `section_E.tex`: a represented but nonseparated Picard tau-part
from a free K3 involution and a double special fibre; a projective flat square-zero
family with universal H0=O and Picard dimensions 1→2, refuting unrestricted
universal openness and dimension constancy; the product formula under universal
H0=O; separation of tau for geometrically reduced fibres and separation of the
full Picard functor for geometrically locally integral fibres. Normal-fibre
p-primary openness and dimension constancy with only reduced fibres are kept as
separate unresolved rows. The preceding list of principal gaps is superseded by
this update and by `results.csv`.

## Checkpoint, 20 November 2026, 14:40 UTC

Substantial advances since the initial table below:

- **E2/H9 is proved** in the full proper-flat universal-H0 setting over a locally
  noetherian base. After passage to a trait and bi-rigidification, a correspondence
  vanishing generically gives a map from a flat connected-fibre scheme into the
  closure E of the generic identity of the other Picard functor. Raynaud 1970
  Proposition 5.2 makes E étale. Every fibre map is zero, hence the whole map is
  zero. Murre 1966 Theorem 4 then supplies the separated unramified scheme.
- **E1's intended relative-normal valuative statement is proved** (connected
  fibres), while the literal normal-total-space statement is false. Raynaud's
  schematicity theorem over a trait plus FGA VI's proper neutral *subset* gives
  the original extension statement. This does not assert that the fibrewise
  neutral subfunctor is representable: that stronger assertion fails.
- **C2 in characteristic zero is proved.** Generalized finiteness gives eventual
  vanishing of H1(m^n O); formal logarithm makes Pic determined by a finite
  thickening, and Artin density supplies algebraization. The excellent-DVR case
  with only finite-length R1 remains an explicit open gate in this run.
- **The role of lci in B2 is essential.** In P6_R the rank-one 2x3 matrix locus
  with a+e=t w has generic fibre Segre P1×P2 and special fibre a normal isolated
  threefold cone, hence R2. The horizontal P2_R defined by the first row being
  zero is not Cartier. This refutes any R2 sufficiency claim that omits lci.
  Larger matrices yield R_m fibres for arbitrarily large m.
- **The all-local-schemes extrapolation in H12 is false under the literal
  punctured-Pic interpretation.** In characteristic three, the local hypersurface
  xy=z²+t²(1+t) is factorial, while its henselization and completion have
  punctured Picard group Z. The original cone-context claim survives: its
  discrepancy has a finite filtration by additive groups in characteristic p.
  Intrinsic étale-local definitions of local NS must be distinguished, since
  they already incorporate henselization.

The principal unresolved gates are C2 in the requested excellent-DVR generality;
the generality and interpretation of B2's requested fibre-only classification;
H8's negativity theorem with all original hypotheses; H10's supplementary
conormal criterion; H11's affine-versus-quasi-affine question; and the individually
listed E4 openness, separation, rank-variation, and schematicity questions.
None is marked complete merely because a sufficient case is known.

## Initial verified outcomes

| Item | Status | Gate / result |
|---|---|---|
| B1 / SA14 H2 as framed in the prompt | Refuted | A projective quadric degeneration has a horizontal non-Cartier divisor Cartier on its smooth generic fibre. |
| B2 necessity of R2 / SA14 H13 | Refuted | A regular smoothing has non-R2 special fibre but factorial total space. |
| B2 exact criterion based only on abstract geometric fibres and base | Impossible in that interpretation | Two families have the same base and geometric fibre isomorphism types, with different answers. A criterion must retain deformation/total-space data. |
| B2 R2 sufficient over regular base, relative complete intersection | Proved under stated hypotheses | Induction using SGA 2 XI 3.13(ii); details in section.tex. |
| C1 projectivity after completion | Known, with deduction | Artin 1969, Thm 1.12 p.26; approximate a formal ample bundle modulo the maximal ideal. |
| C3 Pic of punctured henselian spectrum vs completion | Known in greater generality | Elkik 1973 III §1, Thm 3 p.569 and Corollary p.573, any noetherian henselian pair. |
| C2 finite-length R1 | Proved in all characteristics for excellent henselian local bases | Full Theorem C2.G, with two separate AI audits; no flatness hypothesis on X. |
| C characteristic-p local NS / H12 | Original cone claim proved; arbitrary-local extrapolation refuted | Exact cone scope and the separate literal punctured-Pic counterexample are preserved. |
| E1 literal normal-total-space version | Refuted | A normal projective nodal cubic family has a generic degree-zero bundle whose closure is non-Cartier. |
| E1 intended normal-morphism version | Proved in connected-fibre valuative form | Raynaud 3.3.1 plus FGA VI Cor2.3; no scheme claim for the fibrewise Pic0 subfunctor. |
| E3 / H11 flattening | Known | Stacks 77.11.8(3), tag 0CWQ, and scheme version 38.27; no projectivity needed. |
| H6 quotient by flat open-and-closed Picτ | Known, with deduction | Stacks 06PH and 0418 imply a separated unramified scheme quotient. |

## Corrections and distinctions already established

1. The original 57:110 question retains essential properness of the Picard **functor** as a hypothesis. Part B1 and H2 of the supplied prompt omit that hypothesis. Our quadric example refutes the prompt's broader statement, not the original implication with essential properness retained. The paper must preserve this distinction.
2. The phrase at 57:314 is “si X→S est normal”, a relative normality hypothesis. The next page uses the shorter “X est normal et propre sur le trait S”. Taking this to mean only normality of the total scheme yields a false assertion, even for projective X. Hence the prompt's alleged equivalence requires correction.
3. The R1 node factorization is correct in characteristic different from 2 with i²=-1: (z-it)(z+it)=z²+t². A split alternative xy=z(z-tw) gives a projective counterexample in every characteristic without i.

## Sources opened

- Michael Artin, *Algebraic approximation of structures over complete local rings*, Publ. Math. IHÉS 36 (1969), 23–58. Opened primary PDF; Thm 1.10 and 1.12 p.26, Cor.2.2 p.27. URL: https://www.numdam.org/item/PMIHES_1969__36__23_0.pdf
- Renée Elkik, *Solutions d'équations à coefficients dans un anneau hensélien*, Ann. ENS (4) 6 (1973), 553–603. Opened primary PDF; III §1, Thm3 p.569 and Picard corollary p.573. URL: https://numdam.org/item/10.24033/asens.1258.pdf
- Steven Kleiman, *The Picard scheme* (2005), arXiv:math/0504020. Opened primary text. URL: https://arxiv.org/pdf/math/0504020
- Michel Raynaud, *Spécialisation du foncteur de Picard*, Publ. Math. IHÉS 38 (1970), 27–76. Opened primary PDF. URL: https://www.numdam.org/item/PMIHES_1970__38__27_0.pdf
- Sylvain Brochard, *Foncteur de Picard d'un champ algébrique*, arXiv:0711.4545v1 (2007), Thms1.3,4.3.1,4.3.5. Opened. Extra hypotheses recorded, not silently omitted. URL: https://arxiv.org/pdf/0711.4545
- Stacks Project, tags 0CWQ, 06PH, 0418. Opened official pages.

## Computation

`code/check_examples.py` checks exact defining equations, substitutions, Jacobian ideals, and linear independence for the B/E counterexamples. It uses characteristic 0 and the fields F2,F3,F5. Its output records runtime and scope. Normality and Cartier/non-Cartier claims are proved algebraically, not inferred from finite sampling.
