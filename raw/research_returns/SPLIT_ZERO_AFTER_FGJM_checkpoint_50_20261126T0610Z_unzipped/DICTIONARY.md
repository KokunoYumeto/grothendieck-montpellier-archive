# Mathematical dictionary

Entries distinguish a proved translation from an analogy. No arithmetic realization, motive, purity theorem, or categorification is inferred from a coefficient formula alone. Detailed entries are added with their proof-bearing statements.












































































































































<!-- MERGED FRAGMENTS -->


## paper1_dictionary

# Paper 1 dictionary: algebra, geometry, and the stated programme

Each entry states the exact mathematical translation and the proof carrying it. A connection to motives, weights, or lambda-operations is not inferred merely from common terminology. Source locators refer to the attached archive, which is not copied into this workbench.

## Two zeros, ideals, and the affine spectrum (SZ1-002–SZ1-009)

**Algebra.** The new zero tau records absence; the old ring zero records a present coefficient whose ring value is zero. Ideals and congruences distinguish those two states. The ring reflection identifies them. Zero adjunction is fully faithful, preserves injective pullback descriptions R_0=R×_K K_0, and turns a ring product into a pullback of support maps to B.

**Algebraic geometry.** Spec R_0 consists of the ordinary affine scheme's points plus an open generic point eta. Every nonempty open is eta∪U and has semiring of sections Γ(U,O_R)_0. The ordinary scheme remains a closed subspace. The generic local semiring is B, not the fraction field of R. The pullbacks above are algebraic pullbacks of semirings; they are not asserted to identify arbitrary geometric pushouts in a different scheme category.

**Proof carrying the translation.** The ideal classification proves the point correspondence and its specialization order; old-denominator localization gives the stalks; the common generic point forces sheaf sections to make one uniform choice of absent versus present. The two congruence families show exactly how the ordinary affine ring quotient and the zero-adjoined quotient differ.

**Archive cotes.** `ours/foundation/h22_note_v3.tex`, thm:spec, lem:normal, prop:golan, prop:ff, prop:fix; `ours/split_zero_corpus/01_split_zero_secondary_note.tex`, lines 295–313; `02_split_zero_repair_dossier.tex`, line 921; `16_split_support_geometry_arithmetic_curve_v11.tex`, line 496. No assertion about arithmetic weights follows from these algebraic formulas alone.

## Module diagrams and the Boolean generic fiber (SZ1-010–SZ1-012)

**Algebra.** An R_0-semimodule is a join-semilattice L with least point, carrying R-module groups A_l and coherent linear transition maps. The least group may be nonzero. The idempotent of a vector m is em=m+(−m).

**Geometry.** Localization at an old scalar s leaves L unchanged and replaces A_l by (A_l)_s. The new generic point sees L alone, since inverting the old zero collapses each group to its identity. Thus the generic Boolean fiber remembers which groups are present and forgets their vectors.

**Proof carrying the translation.** The inverse identities split the additive monoid into its maximal groups. Fractions never identify distinct support labels; within each label their equivalence is the ordinary module localization equivalence. At e all groups localize to zero. This is a module-theoretic statement, not an identification with the Connes–Consani arithmetic site.

**Archive cote.** `ours/foundation/h22_note_v3.tex`, thm:mod and rem:generic. FGJM Proposition 6.1 and CFMM §§4–5 are the earlier structural ingredients.

## Projectives and Grothendieck groups (SZ1-013–SZ1-017)

**Algebra.** Finite projectives are finite posets P labelled by finite projective R-modules P_p, with group ⊕_{p∈I}P_p over the ideal I. Zero labels are allowed. The only projective with a singleton support semilattice is the zero object; ordinary nonzero R-modules are not projective after restriction to R_0.

**K-theory.** Direct sum is disjoint union of labelled posets. Consequently V(R_0) is the free commutative monoid on nonempty connected labelled types and K_0(R_0) is the free abelian group on those types. Labels require projective-module isomorphism classes V(R), not only their images in the group K_0(R). Extension of scalars to R sends the class to the sum of its labels. Strong projectivity means a direct summand of a finite free module and gives only free semimodules, so SK_0(R_0)=Z.

**Proof carrying the translation.** A free retract has a finite distributive support lattice. Coordinate projections split all group transitions; sum and intersection laws permit successive splitting at join-irreducibles. An explicit idempotent block matrix realizes every labelled poset. Unique connected components then give the free monoid and its group completion. Strong summands must select connected components of a free object's discrete labelled poset.

**Geometric scope.** Ordinary projective R-module labels are vector bundles on Spec R. Their incidence poset is additional Boolean-generic data. No exterior-power lambda-ring structure on this enlarged K_0 has been established here, and no motivic or weight realization is asserted.

**Archive cote and correction.** `ours/foundation/h22_note_v3.tex`, thm:proj and prop:unique. Its prose at lines 89 and 227 incorrectly identifies all one-idempotent projectives with projective R-modules; SZ1-014 gives the corrected statement. The main labelled-poset theorem survives.

## Quasi-coherent sheaves (SZ1-018)

**Geometry.** In the fixed prime-ideal semiring-spectrum convention with ordinary semimodule sheaves, QCoh(Spec R_0) is the category of diagrams L→QCoh(Spec R). On eta∪U, sections form the disjoint union over l of Γ(U,A_l). Association and global sections are inverse on this affine spectrum.

**Proof carrying the translation.** All nonempty intersections contain eta, so compatible local sections have one common label. For a fixed label, the group sections glue by ordinary quasi-coherent sheaf theory on Spec R. Conversely the local group fibers of a quasi-coherent semimodule sheaf glue to the ordinary quasi-coherent sheaves. The empty ring spectrum reduces to B-semimodules and checks the boundary convention.

**Scope and programme.** This is an affine quasi-coherence theorem in a named semiring-scheme setting. It does not claim comparison with every blue-module convention, descent on arbitrary semiring schemes, derived categories, or motives. The framework is Lorscheid (2026), §§1.1 and 1.4.1; the module equivalence itself is proved in Paper 1.

## Every inverse semiring and the two-idempotent construction (SZ1-019–SZ1-022)

**Algebra.** For the CFMM pair (Q,F), a semimodule consists of a Q-semimodule L in zero join-semilattices, a group diagram G, and natural bilinear maps F(q)⊗G(l)→G(ql) satisfying unit and associativity. For I(f), this specializes to R-module diagrams and natural maps A⊗_R G_l→G_0 whose composite to G_l is f(a)-multiplication.

**Proof carrying the translation.** Scalar action on idempotents depends only on the scalar's additive idempotent. Restricting to maximal groups gives the bilinear maps; reconstructing the disjoint union verifies every module axiom by naturality and bilinearity. The matrix description gives exact finite certificates for projectivity and isomorphism, but an intrinsic general classification remains open where transitions need not split or be injective.

**Geometric and motivic scope.** These are coefficient and module categories. A motive or a weight structure requires additional realization data beyond (Q,F); it is not part of this equivalence. The task's programme connection is a common support-and-group language, not an automatic realization theorem.

**Sources.** FGJM Construction 3.5; CFMM Theorem 8.5 and Remark 8.7. These published constructions are credited; their semimodule counterpart is proved here without a priority claim.

## Repeated zero adjunction and coloured support (SZ1-023–SZ1-026)

**Algebra.** R^[k] has idempotents C_{k+1}. Modules carry nested scalar truncations. Its finite projectives correspond to coloured finite posets for which every join-irreducible has a greatest truncation at every smaller positive colour; only top-colour points carry ring-projective labels.

**Geometry and K-theory.** The spectrum adds a chain of k generic points; at a point introduced at step j the final stalk is C_{k−j+2}. V and K_0 are free on connected coloured labelled types, while SK_0 is Z. The successive generic layers record increasingly truncated support, not arithmetic Frobenius weights.

**Proof carrying the translation.** In a finite-chain free retract, scalar truncation is intersection with a nested ideal. A coordinate detecting a join-irreducible also detects each positive truncation, forcing the greatest-element condition. Explicit linear section/retraction maps prove sufficiency, and ring idempotent blocks realize the top-colour labels. Unique connected decomposition yields the Grothendieck formulas.

**Archive cote.** `ours/foundation/h22_note_v3.tex`, rem:chains, has the finite-chain zero-ring observation; the complete coloured-poset theorem is derived and checked in this work. No exact predecessor has yet been located, and no novelty claim is made.

## Double absorber and monoid coefficients (SZ1-027–SZ1-030)

**Algebra and geometry.** A double absorber violates the absorbing-zero axiom. In the FGJM zeroless framework, ideals required to contain the additive identity give the original spectrum, not an added generic point. With ordinary unital zero-preserving module axioms, only the zero module exists. By contrast R_0[M] remains a genuine inverse semiring; its pair has finite monomial subsets and coefficient groups R^U, with convolution.

**Proof carrying the translation.** Multiplying the additive identity by the absorber forces the absorber into every ideal. The module equations ∞m=(∞0)m=∞(0m)=0 and ∞+1=∞ force m=0. For monoid semirings, occupied support is union under sums and setwise product under multiplication, even when ring coefficients cancel.

**Programme connection.** A supported zero of Z_0[q,q^(-1)] means a present weight with zero integer trace. Whether it comes from a positive/negative pair, which Euler factors it carries, and what purity theorem applies are extra data studied in the other papers. The pair alone cannot recover multiplicities that were discarded.

**Sources.** FGJM §3.1, Definition 3.8 and Proposition 3.9 for the absorber framework; FGJM Proposition 5.2 and CFMM Theorem 8.5 for monoid coefficient structure.


## All two-idempotent projectives (SZ1-031–SZ1-033)

**Algebra.** For a unital ring R, an R–R-bimodule A, and a bimodule map f satisfying f(a)b=a f(b), put I=im f and B=R/I. A finite projective left I(f)-semimodule is classified by a finite projective R-module P, a finite projective B_0-semimodule N, and an identification P/IP≅N_top. The equivalence relation uses full flag-preserving diagram isomorphisms, including upper-triangular mixing of chosen complements. Direct sums are direct sums of these triples.

**Proof carrying the translation.** When A embeds as I, free fibers are I^(complement U)⊕R^U inside R^n. A free retract has top group P and least group IP; every intermediate group is the inverse image of its reduction modulo IP. A B_0 splitting lifts to R-linear maps whose error lands in IP. Appending free coordinates with bottom-support section corrects that error and proves projectivity. For noninjective f, matrices with a fixed idempotent Boolean support form a nonunital ring. The kernel of reduction to the image ideal is square-zero. The explicit correction a+(1−2a)(a²−a) lifts idempotents, and inverses in the corners lift image isomorphisms. This gives a bijection of projective isomorphism classes, not an equivalence of all projective categories.

**Geometry.** For commutative R, P is a vector bundle on Spec R. Its restriction to the closed subscheme Spec(R/I) carries the finite distributive family of subbundles given by N. The group at each support is the inverse image of that subbundle. The classification is a gluing statement about a bundle and a finite incidence diagram on the closed subscheme. The bimodule kernel changes possible morphisms but does not add projective isomorphism classes. No assertion about a motivic realization or a lambda-ring structure follows without further data.

**Source and literature.** FGJM Construction 3.5 and Corollary 4.12 provide and exhaust the scalar constructions. The current proof is recorded in `checks/paper1_two_level_derivation.md`; an independent same-model derivation is `checks/root_two_level_independent.md`. The ring-patching analogy is Stacks Lemma 15.6.9 (Tag 0D2G), and the idempotent-lifting polynomial is Lemma 10.32.7 (Tag 05BU). Neither is silently treated as a semiring classification theorem. No priority claim is made.

## Distributive-lattice spectra and branches (SZ1-034–SZ1-035)

**Algebra.** The scalar semiring G_L(R) has zero groups at all lattice levels below the top and ring group R at the top. Its ring reflection is R; its Boolean characters are the bounded lattice characters of L. Its ideals consist of proper lattice ideals and the full lattice together with a ring ideal. They are all subtractive.

**Geometry.** The spectrum is the topological ordinal sum Spec_lat L followed by Spec R: every lattice prime generizes every ring prime. The lattice part is open, the ordinary affine spectrum closed. Localization at a lattice idempotent z_lambda is the principal interval below lambda. A lattice character gives a quotient to R_0 selecting one lattice prime together with all ring primes. For finite L=Id(P), the lattice spectrum is P with order-ideal opens. These are finite incidence coordinates and specializations, not a Frobenius weight filtration.

**Proof carrying the translation.** Ideal absorption and addition classify the two ideal families. The resulting basic opens determine the full topology. Localization at a multiplicative idempotent is its principal multiplicative image. Finite distributivity identifies join-irreducibles with coordinate tests, and the branch map is a literal congruence quotient. The zero-ring case has no ring-prime stratum, so the dimension formula is stated separately. Ideal chains of Artin rings realize the lattice under sum and intersection; their ordinary ideal product is a different operation.

**Archive cote.** `ours/split_zero_corpus/16_split_support_geometry_arithmetic_curve_v11.tex`, theorems labelled `lattice-normal-form`, `lattice-boolean-characters`, `birkhoff-support-coordinates`, `lattice-localization`, `lattice-ideal-classification`, `lattice-prime-classification`, `spectral-ordinal-sum`, `boolean-branch-base-change`, and `branch-selected-spectrum`. Exact line locators are in the register.

## Nonassociative amplitudes: a scope correction (SZ1-036)

The source's sentence that ring reflection forgets only support is false if the amplitude algebra A is nonassociative and “ring” has its usual associative meaning. Any homomorphism to an associative ring annihilates every associator (ab)c−a(bc), so the associative reflection also quotients A by the two-sided associator ideal. Projection to A merely forgets support within a suitable category of nonassociative algebras. This is outside Paper 1's associative-semiring scope and is recorded as a correction, not promoted to its main body. Archive cote: corpus 16, `cor:support-phase-associator-package`, following prose at lines 2171–2173.


## Derivations and the cotangent module (SZ1-037)

**Algebra.** For a ring map A→R and normalized additive Leibniz derivations with d(1)=0, Der_(A_0)(R_0,M)=Der_A(R,M_bottom). The universal relative differential semimodule is the ordinary R-module Ω^1_(R/A) restricted through the ring reflection, so it has one support point whose group need not vanish.

**Proof carrying the translation.** The equality 1+e=1 forces d(e)=0. The equation r+(−r)=e then places every derivative in the additive group at the global zero. The usual ring differential property represents these maps. Every projective R_0-semimodule has zero least group; therefore its target derivations vanish, even when the universal differential module is nonzero.

**Geometry.** Ring tangent data survive in the ordinary differential module but lie in the least group, which free/projective inverse-semiring targets cannot see. Thus the support idempotent is derivationally constant without being a nilpotent infinitesimal. The example R=Z[x], A=Z has Ω=R dx nonzero despite Der(R_0,R_0)=0. No formal smoothness or cotangent-complex assertion is inferred.

**Archive cote.** Corpus 16, `prop:derivation-kills-e`, lines 924–953, proves the first vanishing. The stronger natural identification and representing object were derived in this run; `checks/paper1_derivations_independent.md` is the statement-only independent re-proof.


## paper2_phase_dictionary

# The initial motion of quotient-counting zeros

SZ2-prop-zero-phase is a precise analytic consequence of the quotient-cardinality interpolation L_t(s)=zeta(s,1+t). At a simple critical-line zero, implicit differentiation and Hardy's real function determine the horizontal velocity. The phase is pi W_n plus arctan(1/(2 gamma_n)); the latter term cannot be discarded in an exact sign test. Equidistribution of the complete W_n modulo two makes boundary neighborhoods negligible and implies the asymptotic half-share of right-moving simple zeros. That equidistribution is not established. This describes the analytic path between two cardinality conventions, not a deformation of algebraic varieties or motives.

SZ2-prop-clt-not-modulo gives an elementary probability counterexample to the missing implication: a Gaussian rounded to even integers has a normalized Gaussian limit and the expected leading variance but is concentrated at zero modulo two. A bounded independent uniform addition produces uniform residues, so a bounded correction can destroy them again. The later unpublished IMPLICATIONS §7.2 already recognized the fixed-frequency gap; this is a confirming explicit proof, not a novelty claim. Earlier ZETA_LABELS assertions must be read with the correction and the boundary condition.

SZ2-prop-quotient-apoint-bound applies Arias de Reyna and van de Lune (2011), Theorems 3.1 and 4.1, to the exact quotient series. The all-quotient weighted family has a=u/(1+u), while the separated sheet has a=1. Their rightmost-zero bounds are known analytic results; no Riemann hypothesis for these affine transforms follows from the granted theorem for zeta itself. The reported separated-sheet value near1.78 in the unpublished implications is corrected by the cited defining equation (root approximately1.9401).


## paper2_unadmitted_support_dictionary

# Unadmitted arithmetic support-lift claims

The twelve GATE-ZP rows distinguish a proved scalar identity from an unspecified lift of analytic packets, conormal quotients or primitive corrections. In ordinary terms each asserted lift needs a defined source and target join-semilattice, their group diagrams and scalar actions, a support map, and compatible linear maps on all fibers. The general module-equivalence theorem does not construct these arithmetic inputs. These rows remain in the register as claims that cannot yet be made into the proposed precise arithmetic statements; no check status was upgraded by this reconciliation.


## paper3_arithmetic_dictionary

# Arithmetic intake terminology

The representation ring is the Grothendieck ring of finite-dimensional complex representations of a finite group. Its positive cone consists of actual representation classes. The old zero is the zero representation class; the new zero denotes absence according to a separately stipulated coordinate set.

Character evaluation preserves the zero-adjoined support convention. A zero evaluated character at one group element need not mean a zero representation. Vanishing at every group element means the zero virtual class, but still does not identify whether an ordinary zero coefficient came from an absent or a present coordinate.

A virtual polar coefficient of negative dimension is not an effective representation. This is a positivity statement about a coefficient layer, independent of the analytic construction of a moonshine function.

The coefficient-support object for a fixed Weyl basis is a finite coordinate module over C_0. A single element of G(M_r(C)) does not retain a separate label for every coordinate that happens to vanish.

The principal-part residue identities concern rational differentials on the projective line. Their finite/infinite balance does not construct a C*-algebra extension or a morphism from zero-adjoined modules.

The quantity N(J)=|R/J| is not multiplicative for arbitrary finite-index ideals of arbitrary rings. The retained Dedekind setting supplies the missing arithmetic hypothesis.


## paper3_dictionary

# Paper 3 dictionary

The old zero of a local field is the ordinary point defining a coordinate hyperplane. It is not the adjoined zero of FGJM Definition 3.6. The at-most-one-zero locus is an invariant open subset of a product of local fields. Its standard object is the transformation groupoid for the discrete S-unit group, or its amenable crossed-product C*-algebra. This dictionary gives a precise arithmetic construction; it does not produce an inverse-semiring scheme or a functor from R0-semimodules.

“Primitive defect” translates to a specified group homomorphism: either negative augmentation on the free group on a finite label set, or the exponential connecting homomorphism in a C*-extension. The two are identified only through the explicit extension maps proved here. The kernel A_(r−1) is the usual type-A root lattice with the coefficient inner product. Free characteristic-vector linearization of a support set is an extra construction and is not additive group completion of the Boolean support monoid, whose group completion is zero.

“Natural one-zero algebra” translates to C0(W_P^(1))⋊Γ_P. “Scalar one-zero algebra” translates to C0(W_P^(1)/K_P)⋊Γ_P. The latter is the compact-unit quotient used by Connes and Consani, not Morita equivalent to the former merely because they have the same places. Proper compact quotient gives an injective coefficient map in the opposite direction and hence the scalar-to-natural extension morphism.

“Nonconstant unit fibres” translate to locally constant integer functions on profinite unit groups. At a finite place their invariant group is Z^Ω and their coinvariant group is the Haar-normalized group D^Ω. Rational denominators record growing orbit lengths. The arithmetic p-adic order formula proves Ω finite. Odd difference modulo the real sign quotient gives the finite matrix D; for 2,3,5 its Smith factors produce Z/2⊕Z/4 torsion.

The full middle K1 is given by the two-term complex B in Theorem presentation. Rotation coboundaries lift to generic winding classes; this relation computes the abelian extension rather than assuming a split. This is topological K-theory of C*-algebras. No equality with algebraic K0 of R0-projectives, a lambda-ring, a motive, a weight filtration, a correspondence category, or a purity theorem has been established. Those words are therefore not used as substitutes for an arrow.

“Finite-set coherence” translates to an explicit directed system of stable extensions. Complementary-prime Hilbert spaces and multiplication of rational-number basis labels fix the identifications. The old-stratum embeddings are nondegenerate into their range ideals, not generally into the entire target middle algebra. Their generic-ideal maps are nondegenerate, which is exactly what is needed for the Busby identity.


## paper3_packet_dictionary

# Packet intake dictionary

The old zero e of R remains a supported element of R_0; tau is the newly adjoined additive identity. The two-element set {tau,e} is an internal Boolean semiring whose multiplicative identity is e. Its inclusion in R_0 is not unital when R is nonzero.

A divisor support sheaf means the product of skyscraper fibres on a closed discrete support. Its finite-support presheaf is a different object before sheafification. A chain or Boolean sheaf has finite stalks; sections over an infinite support may be infinite.

The coefficient-support map from truncated jets to a Boolean cube is a map of pointed sets. It is not additive, because nonzero coefficients can cancel. The complete coefficient support uses a chosen local parameter; the vanishing order and socle line are intrinsic.

A packet is a finite orbit of zero locations under the specified involutions. Equivariance transports fibres over the corresponding base homeomorphisms. Invariant pushforward has stabilizer-fixed fibres, with a diagonal description only when the stabilizer action on a fibre is trivial.

A phase decoration is the pointed set consisting of a circle and an extra basepoint. No inverse-semiring module structure is implicit in that phrase. Analytic phase factors and spectral coordinates do not, by themselves, define a sheaf morphism on a Scaling Site.

The spectral affine coordinate z=i(s−1/2) is restricted to |Im z|<1/2 when identifying nontrivial zeta zeros. The global affine pullback also has images of trivial zeros.

The least circle length for a fixed ordinate means the least member of the family 2πn/|ordinate| with n a positive integer. No unrestricted primitive-cycle claim is inferred.

The ordinary monoid semiring retains its empty-sum zero. A contracted presentation must explicitly identify the multiplicative absorbing symbol with that zero.


## paper4_dictionary

# Paper 4 dictionary: algebraic and geometric meaning

This dictionary translates the checked circuit statements into coefficient, support, and monomial-ideal language. It does not infer a theorem about motives or Galois representations from a Boolean predicate. No Grothendieck archive cote is supplied: none of the examined sources establishes such a connection for these circuit counts.

## SZ4-001–003: the ring and its occupied exponents

The ring reflection of R_0[M] is the ordinary monoid algebra R[M]. The extra datum is a finite set S of occupied monoid degrees, including degrees whose coefficient is zero. Over S the coefficients form the R-module R^S; enlarging S extends coefficients by zero, and multiplication is convolution. This is exactly the explicit pair of CFMM Theorem8.5 proved in Proposition3.1. For M=N^n the reflected ring is the coordinate ring of affine n-space over R. Occupancy is additional semiring data, not an additional ordinary polynomial coefficient.

## SZ4-004–009: a predicate quotient and its arithmetic lifts

The idempotent base Q_n consists of upward-closed families of subsets of the variables. A finite exponent set determines such a family by asking whether an assignment contains one of its variable supports. Over a predicate f the coefficient group consists of integer polynomials all of whose monomials have true supports. The surjection from Z_0[x] is proved by adjoining the minimal true squarefree monomials with coefficient zero. These are coefficient groups over an idempotent base; calling them a sheaf of motives would add structure not present in the theorem.

For a graph, its minimal true supports are its edges. Thus the lifting problem asks for a polynomial whose monomials all contain an edge and whose supports witness every edge. One gate list maps functorially to its ring polynomial and its predicate. The arithmetic minimum over all such lifts equals the monotone Boolean minimum because the gates themselves are unchanged. These are Proposition4.1, Proposition4.3 and the first assertion of Theorem1.1. The support criterion is already Jukna's read-k Lemma1; the inverse-semiring wording gives its coefficient group above each predicate.

The standard monomial-ideal correspondence (SZ4-040) gives a further translation. In monomial-ideal language, forget the nonzero coefficients of P and form J(P), the ideal generated by its occurring monomials in Z[x]. The condition P in Sup(G) says that the radical of this monomial ideal is the squarefree edge ideal I_G=(x_u x_v:uv in E). To verify the translation, a monomial ideal's radical is generated by the squarefree supports of its monomial generators: a power of each squarefree support lies in the original ideal, and a squarefree monomial ideal is radical. The latter follows by writing it as the intersection of the coordinate prime ideals indexed by sets meeting every generator. Thus equality of radicals is precisely equality of the minimal variable supports. This is a description of the Boolean quotient through coordinate subspace arrangements, not an inference that taking radicals preserves circuit size.

## SZ4-010,034–037,039,041–042: exact size for a homogeneous support and the missing witnesses

When every output monomial is a squarefree edge of degree two, positivity forces each useful gate to be homogeneous. A product support is a complete bipartite rectangle; four-cycle-freeness forces a star. Linear subcomputations shared across different star centers would give a four-cycle. Counting the separate center networks and the common quadratic network proves the coefficient-independent bound |E|+vc−1. The all-one coefficients attain it. This is the quadratic assertion of Theorem1.1, proved in Section5.

The minimum-degree part is obtained by keeping the lower-degree operand at unequal-degree additions, and multiplying minimum-degree parts at products. No extra gates are needed. Hence, if every edge has a squarefree witness, this lower envelope has exactly the edge support and the same lower bound follows. This is the classical lower-envelope/read-1 reduction, spelled out in `lem:lowerenvelope` and the read-1 part of Theorem1.1.

If r edges have only higher-power witnesses, the same operation keeps a subgraph G_2. A cover of G_2 extends to a cover of G by at most r vertices. If some edge is missing and the quadratic part is nonzero, the lower-envelope operation removes an unequal-degree addition. A deepest product in a parse tree for a missing-edge monomial has a quadratic monomial u², uv or v², none allowed in the output quadratic part, so that product is also removed. This supplies two additional gates (`lem:lostgates`) and proves the full exact bound even when just one witness is missing. If exactly two gates are removed, the original output has the normal form P=P_2+bcD, where b,c,D are linear and every nonsingleton support lies in an old star neighborhood. Four-cycle-freeness then permits at most one missing edge. Thus r≥2 costs at least three discarded gates (`lem:threelost`), with sharp examples verified on all Boolean inputs. The full bound now holds for every r≤2 (`thm:twomissing`): in the remaining cover-drop-two case, an optimal quadratic remainder and exactly three lost gates force a forbidden cover exchange. If r≥3 and E_2 is nonempty, at least four gates disappear (`lem:fourlost`), so the loss in the star bound is at most2r−4 (`cor:fourlostbound`). This preliminary argument requires r≥3 for a saving; the subsequently proved full r≤3 theorem strengthens the current requirement to r≥4. The exact general charge remains open. In the ideal dictionary, the lower envelope can omit generators of the radical even though the full polynomial still has radical I_G. That is the precise reason an argument in the homogeneous coordinate grading does not settle arbitrary lifts.

## SZ4-011–016: linear dependence on one side

Marking one bipartition side gives a partial polynomial grading. Degree at most one means the circuit can propagate a marked variable through conjunctions only by multiplying by an unmarked expression. The dependent computation is therefore linear over the Boolean coefficient semiring. Its transposition computes the neighborhood predicates. The neighborhood sets meet pairwise in at most one variable, and the partition argument counts their disjunction gates even in the presence of arbitrary conjunctions. First conjunctions on successful paths give a vertex cover. These statements are Lemmas6.1 and7.1–7.3, `thm:onesided`, and `cor:degreewitness`.

This use of a grading is compatible with the monoid algebra and the idempotent quotient, but it is not a K-theory invariant. The gate count depends on a presentation by a finite acyclic list. The theorem implies that a cheaper circuit, if one exists, must have degree at least two in both bipartition gradings.

## SZ4-017–025: semantic zero versus a coefficient zero

The embedding R_0 into R times B keeps both the ring value and the presence bit. A coefficient zero is a zero in one group R^S at an occupied monoid degree. A semantic output zero instead occurs after substituting particular values: x−1 has no coefficient zero but evaluates to the old zero at x=1. These are different operations, as stated at the start of Section8.

Over F_2, if the final answer never equals the old zero, its ring bit equals its presence bit. Its circuit therefore has a monotone shadow of the same size. Conversely the arithmetic expression a+b+ab implements disjunction on {tau,1}, using three gates, although an intermediate sum may be the old zero. Allowing old-zero final outputs gives ordinary Boolean complexity within constant factors. The all-gates prohibition is refuted even by disjunction. These are `prop:complexity` and the following output-condition remarks.

Alon–Boppana's clique bound and the classical Berkowitz–Wegener slice simulation then have the precise consequences in `cor:clique` and `prop:slice`. An exponential ratio alone does not say that the smaller complexity is polynomial. Parity distinguishes tau, old zero, and one by the presence bit and ring bit; the even-parity pair is Boolean with its own unit, so its inclusion is not unital (`prop:parity`).

## SZ4-026–028: effective sign classes and the two forgetful maps

For M=Z, the effective coefficient semiring N[C_2 times M] records positive and negative sign multiplicities at each Tate weight. Their sum determines occupancy and their difference determines trace. Mapping these to Z_0[M] is surjective: any integer is a difference of positive multiplicities, and1+epsilon gives an occupied zero. This is a coefficient-level effective realization; it does not assert that every formal coefficient table satisfies associativity or is realized by varieties.

The other lift, N[M] to Z_0[M], has no cancellation and never creates an occupied zero. The monomial x^2y nevertheless becomes the same Boolean support as xy. Conversely x−x has an occupied coefficient zero without a repeated variable, and1+epsilon does so at weight zero. Proposition9.1 proves the independence. Thus trace cancellation and passing from monoid degrees to the radical support ideal are two separate losses. What transfers without another theorem is evaluation through the homomorphisms and preservation of equations already satisfied by a lift.

## SZ4-029–033,038: the unresolved question and the finite evidence

The unrestricted exact count for girth-at-least-five and for four-cycle-free graphs is an optimization over every positive polynomial with the prescribed radical monomial support. Neither the coefficient modules nor the radical operation furnishes the missing gate charge. The final section states this question exactly. Historical public-node statuses are separated from unretrieved live statuses.

The original truth-table enumeration verifies the finite graphs recorded in SZ4-033. The independent SMT encoding in SZ4-038 checks full Boolean truth tables and distinguishes UNSAT from a timeout. These computations concern finite circuit spaces; they do not prove an asymptotic or universal complexity statement, and no Lean certificate is claimed.

## SZ4-043–048: rigidity and the limits of discarded-gate counting

Equality in the weighted quadratic bound forces every coefficient to be1, every nonoutput gate to be read once, a partition of the edge set into stars at a minimum cover, and binary sum trees for both the leaf forms and the star outputs (`lem:quadoptimal`). These are statements about an optimal arithmetic presentation, not an invariant of the reflected ring alone.

A product of k linear forms whose nonsingleton supports lie in old graph neighborhoods has an induced matching of r new exact edge supports and requires at least2^r distinct factor restrictions. Equality gives all matching transversals with no extra variables (`prop:oldfactors`). The bound counts factors under explicit support hypotheses, not gates in an arbitrary circuit.

The12vertex girth5 example (`ex:chargefailure`) has r2, cover drop2, and only3deleted gates. Its retained quadratic circuit has16gates whereas15is optimal. It refutes the rule that discarded gates alone always pay r plus the cover drop; it satisfies the conjectured19gate total. This is why the full r≤2 theorem uses both deletion count and rigidity of the retained circuit.

## Canonical determinant target (SZ4-051)

The element Delta_n^can in R0[x_ij] has exactly the permutation exponent vectors occupied, with determinant signs as ring coefficients. Occupancy projection produces the formal permanent support polynomial in B[x], where exponents remain formal. Proposition `prop:canonicaldet` proves the elementary binomial(n,floor(n/3)) gate bound for n≥3. A gate-by-gate lift of an ordinary determinant circuit can have extra occupied zero coefficients and is not automatically this canonical element. The bound is a classical support-method consequence, separately checked, not a Boolean lower bound.

## Common cubic and grid configurations (SZ4-052–053)

`lem:commoncubic` applies to a family UVD_i of valid old-neighborhood cubic products and forces all missing edges to share one vertex. `lem:cubicgrid` applies to U_iBD_j, i,j in{1,2}, and gives at most three distinct missing edges across the four cells. These are local support configurations. Neither is an arbitrary circuit gate bound without a separate structural reduction. Both have completed separate-worker statement-only checks.

## Five discarded gates and independent product insertions (SZ4-054–055)

The five-deletion lemma applies to the canonical minimum-degree extraction when the quadratic part is nonzero and at least four edges have only higher-power witnesses. Its proof preserves the retained frame during absorption rewrites, classifies all four deleted-gate configurations, and then bounds Boolean supports using the checked local factor statements. It has a complete targeted check after an incomplete fresh attempt, accurately distinguished in the events. A further statement-only full attack remains incomplete and parked; it is not counted as completed. The resulting bound is |C|≥|E2|+vc(H)+4 for r≥4. In particular the full star bound follows for r=4 with cover gain≤1, and for r=5 with cover gain0; the unrestricted conjecture remains open.

The independent-products lemma says that UVL+WXM+UVWX has at most two missing edges when all six forms have old-neighborhood support, the three products are valid, and nonzero old low parts A,B satisfy A⊆M, B⊆L with AB,AL,BM supported on old edges. Those mandatory cross contexts are essential hypotheses. It has a separate statement-only proof with earlier equality-case and elementary reduction exposure disclosed. It eliminates the two-independent-product pattern from a prospective three-missing-edge counterexample, but does not by itself settle dependent insertions.

## A direct context in the dependent case (SZ4-056)

For the four-deletion configuration with products UV and (A+alpha UV)W and two cuts, a nonzero direct output context D1 of the first insertion supplies an old center k for A. Either the second product reads the first cut directly, or it reads a retained linear gate; following that retained gate to its first quadratic product supplies k in D1. Thus the independent-products lemma applies to UV and WD2 when the cross coefficient vanishes, giving at most two missing edges. The statement is a consequence of the circuit configuration, not of an arbitrary displayed polynomial identity. It needs no optimal quadratic remainder. A separate-worker derivation was saved before the new author proof was read and then completely compared.

## The zero-direct-context companion (SZ4-057)

For the same one-affected-input shape with cross coefficient zero, D1=0 and three missing edges force the quartic equality case. Its context D2 has two variables and meets every missing edge. In an optimal quadratic remainder, either those variables already lie in a minimum center cover, or the affected center can be replaced by them. Hence the cover gain is at most one. This is a complete checked exclusion of that zero-cross one-affected-input shape from the r3/cover-gain2 residual; the later058–064 results complete the four-deletion analysis and leave the stated five-deletion residual.


## Three missing witnesses (SZ4-058–064)

Two quartics sharing three old factors have at most two missing edges (058). Three related cubics under the stated common old low-part condition have at most two (059). In the optimal direct-product configuration, a two-center exchange gives cover gain at most one (060). One-product configurations have missing support covered by a star or at most two context vertices, and an optimal remainder permits the required cover exchange (061). The complete four-gate synthesis gives cover gain at most one for an optimal remainder (062), yielding the full star lower bound for three missing witnesses when the cover gain is at most two, and one below it at gain three (063).

The stronger support-only synthesis (064) proves that any four-deletion configuration with three missing witnesses has missing-edge cover number at most two, without optimality. Thus a gain-three circuit one gate below the star count must have exactly five deleted gates and an optimal quadratic remainder. This was the preliminary r3 deficit configuration; the full069–070 proof below subsequently excludes it. It was never asserted to be a counterexample. All061–064 checks were completed from the new statements before their author proofs were opened, with prior admitted component exposure explicitly disclosed; subsequent comparisons are separate targeted events.

The earlier auxiliary label lem:fourfactors is mapped to canonical SZ4-044. It is the four-variable matching clause argument used in the at-most-two-missing theorem; its occurrence does not create a duplicate canonical result.


## Empty quadratic support at three missing edges (SZ4-065)

Every nonempty simple graph with at most three edges has the full Boolean star count, without a formal-witness restriction. Essential-input counting handles every type except the four-vertex path and triangle; read-once structure excludes three gates for the path, and the two predecessor gates exclude three gates for majority on three variables. Thus empty quadratic support at r=3 is settled. The preliminary r3 deficit was the nonempty-H, cover-gain-three, five-deletion, optimal-remainder configuration, subsequently excluded by069–070. A fresh foundation proof and two complete comparisons are recorded.


Historical manuscript locations at checkpoint08 (current labels/pages are in the latest checkpoint crosswalk): 061 is Lemma 5.22; 062 and 064 are Proposition 5.23; 063 and the residual consequence of 064 are Theorem 1.3; 065 is Lemma 5.24 and the empty-quadratic clause of Theorem 1.3.


## A pure algebraic matching obstruction (SZ4-066)

The expression gL+fM+alpha g²+beta gf+gamma f² cannot Booleanize to a three-edge matching under the six exact f templates in Lemma lem:twoproductmatching. The factors have arbitrary supports, with no old-neighborhood hypothesis, and affine contexts and zero forms are allowed. A fresh foundation proof and complete comparisons establish this algebraic statement. The separate circuit-to-template normalization was subsequently proved and admitted as067; its full proof is in the paper. The r3 five-deletion residual was subsequently closed by069–070.


## Full quadratic carriers and two private products (SZ4-067)

For minimum output degree two, every retained quadratic node and every restored degree-two addition on its output path carries its full current polynomial additively to the output. Its off-path multiples can be erased using Boolean absorption without changing any quadratic coefficient or retained gate. With at most two deleted products, the remaining signals are linear combinations of variables and the two product signals. The exact modified polynomial has the template of SZ4-066 plus its unchanged quadratic part. No bound on deleted additions, graph condition or optimality is assumed. Nonzero quadratic part alone is insufficient wording if a linear output part is also allowed.


## One-cut five-deletion profiles (SZ4-068)

For exactly three missing edges and cover-number gain three, the six missing endpoints induce a matching and all quadratic boundary signals vanish there. With exactly one extraction cut, every deleted gate lies before its high input and the output context is scalar or linear. Four private products give at most six factor clauses, below the eight needed. Three products and one private homogeneous sum resolve into at most two quartics sharing their context; equality confines that context to two matching edges and rules out the third. The stated result retains the optimal-frame residual hypotheses.


## Induced matching is weaker than maximal cover gain (SZ4-071)

The disjoint union of the four-star eight-cycle construction and a two-leaf star has a14-gate optimal quadratic circuit. Adding the quartic matching term on the four cycle endpoints and xy(x+y) on the separate star uses exactly five further gates while missing three quadratic witnesses. The missing graph is an induced3K2, but the cover gain is only one. The resulting19-gate circuit is above the18-gate star count. Thus induced missing matching alone cannot replace the maximum-cover-gain condition in the remaining profile argument.


## A sharp deleted-product bound without graph restrictions (SZ4-072)

If six vertices induce a three-edge matching in G and no quadratic edge in H, at least three multiplication gates disappear under extraction. Normalize at most two private products before specializing to those six variables; the unchanged quadratic base vanishes, leaving the forbidden two-product matching template. This needs no C4-freeness, cover-number condition, optimal frame, or bound on deleted sums. Example071 attains three deleted products but is not asserted optimal as a complete circuit.


## Full three-missing-witness bound (SZ4-069–070)

The remaining three-product/two-cut profile is impossible at cover gain three with an optimal quadratic frame. Its proof retains every variable outside the assigned cover, including isolated ones, so that a small direct insertion context legitimately permits a center exchange. One visible cut gives at most seven linear clauses; both-visible cases are classified by the number of private products ancestral to the first high signal. Together with067and068this exhausts all five deleted gates and proves the full star lower bound whenever at most three quadratic witnesses are missing. The unrestricted problem with four or more missing witnesses remains open. Earlier partial063/064statements remain valid intermediate results, not contradictory current scope claims.


## Current four-witness ledger after SZ4-136–138

A variable-input positive circuit with exactly four missing quadratic edges can beat the star count only in one of two numerical configurations: cover gain2, five deleted gates and zero retained excess; or cover gain3, six deleted gates and zero retained excess. Both have optimal quadratic remainders. These are necessary possibilities, not examples and not proved realizable. The gain3 five-deletion/one-excess-product row is now fully excluded by137. No unrestricted C4-free or girth-five circuit conjecture is claimed solved.

136 is the full equal-minimum-degree hidden-addition theorem on induced H-empty P4+K2 or K3+K2 targets. It preserves affected retained linear operands and the exact original quadratic frame, permits arbitrary retained counts, and exhausts both-f insertions, pure private sums, affected private sums and the equal-degree sum of two private products. Its full separate root derivation and two comparisons close the gate.134 covers the unequal-minimum-degree hidden branch at K<=tau(H)+1;135 is a nonancestral pure-linear-sum ingredient.137 combines those results with the all-visible and one-visible boundaries, first as a conditional separate operator synthesis and then unconditionally after136closure.

138 is narrower than a general D6 theorem. With a minimum retained-product frame, gain at least3, an exceptional outside target, only visible deleted additions and pairwise nonancestral original private products, it forces at least four private products. The proof first derives old quadratic private inputs, then uses the already proved safe-center replacement to make each surviving disjunct individually safe, and finally charges at most one missing edge to each disjunct. It does not cover hidden additions, product ancestry, other outside shapes, or an extra retained product.

The source-of-truth locators are prop:hiddenhomogeneous (136), prop:gainthreefiveprivate and cor:fourresidualfinal (137), and prop:nonancestralexceptional (138), with exact numbered locations generated in the checkpoint23 crosswalk after the clean build. Earlier preliminary dictionary entries are historical proof stages, with their current refinements stated above.

### Checked refinements 140 and 142

On the minimum-product exceptional outside graphs, the all-visible profile requires at least four private products (140), even with ancestry. With pairwise nonancestral private products, at least four private additions are required (142), with arbitrary product count and hidden placements. Thus the remaining three-product/three-addition profile requires both a hidden addition and private-product ancestry; it remains open.

### Checked refinements139 and143

139 is the exact safe old-product template ABCL,DEM,ABCDE with four missing K2/P3-component edges; the independent-high affine/zero corollary is proved separately. It is not a universal three-product normalization.143 gives vc(G)<=K+1 for the original hidden-unequal p2/a3/two-visible-cut network for every K, excluding that branch of the remaining d2/D5/optimal-frame row. Equal-minimum-degree hidden additions and all-visible arrangements remain separate.

### Checked refinements144 and146

144 replaces a mere hidden-addition requirement by an original deleted1+1 minimum-degree sum on the minimum-product exceptional targets, with arbitrary other additions and product ancestry. This does not assert full operand homogeneity.146 is a global at-most-three-missing bound for at most two original nonancestral products and three visible cuts, without cover or retained-count assumptions; it removes the all-visible nonancestral p2/a3 branch in the gain-two row.

### Checked global two-addition and one-visible refinements145/148

145 excludes every original p<=3/a<=2 configuration with exactly four missing quadratic edges, with arbitrary retained counts and cover gain. Consequently the remaining gain-two, five-deletion, optimal-remainder row has exactly two private products and three private additions.148 proves that on the minimum-product exceptional outside targets at gain at least three, the six-deletion p3/a3 profile cannot have exactly one visible cut. Together with140/142/144 it must have product ancestry, exactly two visible cuts and one hidden original1+1 addition. Its full operands may still be inhomogeneous. Neither of the two remaining numerical saving rows is closed.

147 is the algebraic ingredient: a safe product of one arbitrary homogeneous linear form and any positive number of original old-neighborhood factors has at most two target witnesses on an H-empty P4+K2 or K3+K2. Its proof keeps all outside isolates and does not assume a minimum product count or cover gain.

### Checked refinements149–151

149 proves vc(G)<=K+1 in the all-visible two-product/three-cut case with four missing edges, for arbitrary retained product count K.150 concerns exactly two visible cuts: any hidden equal-original-degree sum must become a pure sum of two old linear forms after full-current-carrier erasure.151 globally bounds the pure-sum/nonancestral two-product/two-visible configuration by three missing edges, including squares and sharing. Thus the remaining optimal-frame gain-two p2/a3 case has either one visible cut and two hidden additions, or two visible cuts with a pure hidden sum and original product ancestry. No argument here silently omits the one-visible case.

### Checked refinement152

152 excludes the exact two-visible original1+1 p3/a3 profile at minimum retained multiplication count, gain at least three and exceptional outside graph P4+K2 or K3+K2. Full inhomogeneous operands, raw private ancestors, fanout, repeated products, direct degree-two insertions and zero restrictions are included. The proof keeps the original frame and uses only safe selected highs; earlier unselected highs need not be safe. Together140/144/148/152 exclude the exceptional p3/a3 allocation. This supersedes the earlier open wording for that particular allocation. It does not close either remaining numerical saving row or assert safe-center replacement on P3+2K2.

### Checked refinements153–156

153 is the full old-quartic-grid bound with at most three missing witnesses.154 uses it to exclude the original-dependent two-visible pure-linear p2/a3 profile globally, with no retained-count or cover-gain assumption. Together149–151 and154 leave exactly one visible insertion cut and two hidden additions in the optimal-frame gain-two/five-deletion row. This supersedes the earlier two-alternative wording; the one-visible branch remains open.

155 is an algebraic union bound: four missing witnesses of cover number at least three in two safe old products require eight distinct factor supports across them.156 uses connected original-DAG boundary counts to exclude exactly one visible cut, and two visible cuts with all four private products ancestral to the first high, in p4/a2. It does not cover the remaining two-visible ancestry allocations or p3/a3, and neither numerical saving row is closed.

### Checked refinements157–158 and the single numerical residual

157 proves vc(G)<=K+1 for two private products, three additions and exactly one visible cut, without restricting the two hidden additions or the retained counts. Its complete four-gate DAG/formula proof and the separate root direct-placement proof agree. Together145/143/149–151/154 it removes the entire gain-two/five-deletion/optimal-remainder row. The only remaining necessary numerical saving possibility for four missing witnesses is gain3, six deleted gates and zero retained excess. This does not assert realizability or close the unrestricted conjecture.

158 gives vc(G)<=K+2 for four multiplicative-old-network products, two visible cuts and zero independent-symbol cross coefficient, allowing raw sharing and arbitrary retained counts. Its proof counts distinct old boundary supports, forces two cubic trees and full two-point contexts, and charges actual retained products. It excludes that precise gain-three branch; positive cross and affected old inputs remain separate. Earlier ledger descriptions are historical stages superseded by this paragraph and cor:fourresidualfinal.


## Current precise residual after159

The only numerical possibility remains d=3,D=6,e=0. Existing096,101 force exactly p3/a3 or p4/a2; existing115 already excludes outside4K2 for p3. The p3/a3 outside targets still under research are P3+2K2 and3K2 with the fourth missing edge meeting the minimum H-cover.159 gives the arbitrary-K cover bound K+2 for its exact old-cubic/two-direct-witness actual-context hypothesis, even with positive cross coefficient. It does not assert that every remaining p4/a2 circuit has that decomposition. Earlier two-row wording above is historical and superseded by157.


## Two affected factors after an old cubic high (160)

The exact two-visible high f=C(A OR g)(B OR g), with the stipulated actual low inclusions and old cubic g, has cover number at most K+2 for arbitrary retained K and mixed coefficient. Full five-factor confinement supplies the zero-cross proof; the positive-cross case cannot supply four missing witnesses. This is a specified actual high, not a normalization theorem for the remaining p4/a2 row.


## Complete three-boundary cubic-high profile (161)

For the stipulated exact original frame, old cubic g and f equal to a product of three old-or-first-cut-affected linear boundaries, all affected subsets and q>=0 give vc(G)<=K+2. This subsumes the separately preserved160 scope and includes the previously open single-affected zero-cross template. It does not classify direct proper-private-ancestor inputs or every other product allocation.162 (clause dichotomy/one-visible path consequence) and164 (nonancestral all-visible path cover bound) are separately saved pending candidates, not main results.

## 2026-11-25T10:00:52.189774+00:00 — SZ4-162

`lem:threeandtwoor` is the complete abstract three-AND/two-OR DAG dichotomy, with a full sharing-to-formula argument. `prop:onevisiblepath` excludes exactly one visible cut on an induced H-empty P3+2K2 at p<=3/a<=3, regardless of retained counts or hidden degrees. The ambient original H-neighborhoods remain in force before restriction. `cor:fourresidualfinal` retains the sole numerical d3/D6/e0 row and now requires at least two visible cuts in this outside-path branch. This does not close the two-visible or dependent all-visible cases. Full author and separate fresh proofs, prior author display correction and mutual comparison chronology are preserved.

## 2026-11-25T10:11:51.666301+00:00 — SZ4-164

`prop:paththreevisible` proves vc(G)<=K+2 for the complete induced P3+2K2 missing graph, all-visible p<=3/a<=3, and original nonancestral private products. The full proof uses productive indices, full singleton contexts, actual mixed-low identities and original-product cover charges. No safe-center replacement is assumed for this non-well-covered graph. At minimum K the all-visible case must now have private-product ancestry; two-visible/hidden cases remain separate. Both author and separate root proofs and full mutual comparisons are retained.

## 2026-11-25T10:20:54.486149+00:00 — SZ4-163

`prop:quartictwoboundary` adds the exact Boolean old-quartic/second-two-boundary cover bound vc(G)<=K+2 at arbitrary q and retained K, with exactly two visible private additions. Factor repetition is Boolean padding; original arithmetic degrees, actual contexts and selected frame stay fixed. `cor:fourresidualfinal` excludes this precise p4/a2 component, without claiming a full high-template normalization. Full occurrence-count, quintic confinement, sextic grouping and original-product cover proofs are inserted.

## Refinements165,166,168,169

The raw-divisor, raw-quadratic-ancestor and quadratic-first/four-boundary templates have the stated K+2 cover bounds; the zero-cross path template with one extra linear boundary has the same bound. All retain their full actual-frame hypotheses. The original-operand normalization167 remains pending and no full p4/a2 or D6 closure follows.

##167/171 complete four-product/two-addition reduction

All original raw ancestor and repeated-private-square cases are classified at their original degrees. The remaining Boolean-quadratic template is168, giving tau(G)<=K+2 for arbitrary original retained K. At the sole d3/D6/e0 saving row, only p3/a3 remains. This is a strict allocation closure, not a full four-witness or unrestricted star theorem.

170: product-first/union-second selected path-plus-two-edge obstruction; full support only.172: arbitrary-cross extension of169, actual unaffected high network and original K.173: common quadratic ancestor chain/fork CNF obstruction; bounded old/raw original operand classification only.

174: original1+1 exclusion at equality in the marked-addition forest, only internal-cover or nonold-mate endpoint matching attachments.175: exact three-visible literal join, arbitrary original retained K, induced global target; no broader normalization.

176: prepared quadratic high with two or three affected old bases, arbitrary q and original K.177: one affected old base, zero cross, K+2 with all four global missing.178: positive-cross counterpart is an induced selected-target obstruction. None treats raw nonold preparation as a later base or supplies exhaustive hidden normalization.

179: common raw-linear preparation S in both highs; seven-clause exact template.180: two distinct g insertions before a common product and third high hC or h(C OR g), bounded only.181: at least four GLOBAL missing edges allow global rejection of the three-small-products alternative; every H-independent restriction then has at most seven maximal independent sets, so both remaining outside shapes require at least two visible cuts.182: literal old/raw u,uC,v, one occurrence each; full original-context K+2 charge, not arbitrary insertion allocation.

184: arbitrary Boolean linear first high and at least one affected factor in a three-clause second high; CNF at most7, no oldness needed, no arithmetic-degree change or hidden normalization.

183: one shared first insertion g into both h inputs, followed by literal hC; three distinct consecutive highs g,h,f, not180 double-g allocation. Full original-low/three-coefficient case proof; no general normalization.


Recovery additions185–188,189,196,197,210:185 is the exact nested-both-affected support obstruction;186 the independent join with linear-or-zero contexts;188 the stronger one-old-factor/three-clause preparation theorem, with187 its substitution corollary.189 covers all original literal old/raw operands and insertion multiplicities.196 proves sharpness of K+2 with a25-gate circuit, without unrestricted optimality.197 derives original essentiality, ancestry survival and exact nonraw operand forms; affected networks remain unclassified.210 is only the named independent-pair/raw-affected-final network. Full original proofs, outage session times, verified recovery saves and complete comparisons are preserved separately.

191: exact old-product/later-old-sum two-visible obstruction, no broad normalization.202: purely algebraic listed-occurrence subproduct theorem;193 and195 are proved as its explicit substitutions, preserving their original scopes and separate complete check histories. The stronger theorem replaces duplicate manuscript arguments, not the preserved author/checker files.

194: bounded unaffected-later-linear-preparation cover bound, opposite affected placement from191.198: hidden quadratic join as first high, with affected old bases later.203 and205: independent quadratic/lower-quadratic parts in the later preparation; full-context cover charge proved once and reused.209: raw shared ancestor after an unequal preparation; canonical conclusion stays K+2 despite a stronger checker observation. All are exact two-visible templates and do not provide an arbitrary hidden-DAG normalization.

201: explicit original old/raw first-join reassociation preserving full polynomial, P2, frame and K;199 is its old-only specialization.200: complete original first-hidden-old-quadratic-join reduction using198/201, with repeated original nodes and additive-carrier cases explicit. It does not classify a higher-product join or a different hidden placement.

190: full original two-visible earlier old-linear preparation inventory, with whole protected-carrier erasure and controlled private-use rewiring.206: full original first-hidden-private-product-join reduction, including repeated/proper-ancestor/incomparable inputs and unrestricted later high within the budget. Both preserve exact original K and do not classify other hidden placements. These close the finite recovery batch185–210 except192/204/207/208, which remain unadmitted.

## SZ4-192 — earlier-high reuse after a shared first cut

The exact original highs are g=UV, h=(A OR g)(B OR g), and f=h(C OR lambda*g OR mu*h), with the original three insertion occurrences and every actual low/context identity. Every nonnegative lambda/mu/cross pattern and compatible scalar/zero context is covered. This extends183 within its named support template; it neither classifies all dependent operands nor closes the remaining numerical saving row. Full statement/proof: prop:sharedcutearlierreuse. Complete separate derivation16:21:50, full forward16:26:57, full reverse16:27:02; author first accessed only after independent readback.

## SZ4-207 — raw middle product and affected last boundaries

Exact original g=UV,h=gA,f=(B OR epsilon*g OR delta*h)(C OR epsilon2*g OR delta2*h), three original insertion occurrences once each, all original low/context identities. The complete five-pattern proof gives vc(G)<=K+2 for arbitrary retained K. No raw last operand, raw-square middle high or exhaustive all-visible normalization is asserted. Full proof: prop:rawmiddleaffectedlast; complete fresh16:29:04 and full mutual16:34:07.

## SZ4-208 — a later three-factor linear preparation

Exact original two-visible frame g=UV, S=C OR D, f=(A OR alpha*g)(B OR beta*g)(S OR gamma*g), at least one affected boundary and its stated common first low. The uniform seven-clause argument forces an isolated first-high witness and full singleton actual context, giving vc(G)<=K+2. Scalar/zero contexts are included. No arbitrary hidden placement or raw-preparation normalization is asserted. Full proof: prop:laterthreefactorpreparation; complete fresh16:25:17 and full mutual16:35:21.

## SZ4-204 — one affected dependency and a raw descendant

The named original g=UV,h=(A OR g)B,f=h(C OR lambda*g OR mu*h) occurrences give vc(G)<=K+2 for arbitrary retained K. The seven-clause complement of gL forces an isolated direct witness and a full singleton actual context; all original lows and scalar/zero cases are explicit. Full proof prop:oneaffectedrawdescendant. Complete fresh16:53:23; forward16:55:15; reverse16:56:52.

## SZ4-212 — full outside old leaf support at a matching attachment

For the exact min-product/gain3 matching profile, existence of an original1+1 private addition forces the fourth edge to cross at one center h; its complete old outside leaf support N_h must be nonempty and contained in a partial matching transversal, with the old mate included for a matched attachment endpoint. All other centers fail that containment test. The original marked-addition forest proof keeps zero boundaries and distinct operand incidences. This includes and strengthens174, whose exact statement remains and whose original full proof is preserved in checks/paper4_matchinglinearsum_full_proof_checkpoint32.tex. It does not exclude other hidden input degrees or close the numerical row.

## SZ4-214 — private products on every matching restriction

prop:matchingprivateessential: formal-zero intervention preserves the original quadratic frame, while every three-matching restriction loses a witness. This is an original-node necessity result, with no injective witness assignment or first-true claim.

## SZ4-213 — original two-visible hidden-node inventory

The induced path target with p3/a3 and vc(G)>K+2 permits only an unequal hidden sum of a degree-one current signal A+beta*g and a raw private product, or an exact second-high product-join reassociation into three visible cuts. The former remains open; the latter preserves the current erased/pruned polynomial and original quadratic frame and transfers to the all-visible case. Original degree-one/degree-one hidden inputs are excluded, including affected inputs. No complete all-visible classification or numerical-row closure follows.

## SZ4-215 — an old factor after an earlier unequal preparation

The literal original chain u=UV,S=C+u,g=SZ, with all displayed base forms old homogeneous linear and g first visible high, forces vc(G)<=K+2. The proof derives the second high as the third original product and exhausts its ten unordered operand-type pairs. This excludes that exact subfamily of213; it does not classify a first high S*S, a longer raw input, or a later unequal preparation. No211/213 premise was used.

## SZ4-211 — exhaustive all-visible original-node inventory

For the exact original all-visible p<=3/a<=3 induced P3+2K2 four-global-missing frame with vc(G)>K+2, p=a=3. Three distinct highs have no raw operands and exactly the stated necessary affected-type table; two distinct highs are comparable and the uninserted product has exactly R1/R2/R3, retaining all occurrence coefficients and the common-singleton index restriction when both R3 inputs are affected. Every private product satisfies214; no realization or numerical closure is asserted. The manuscript uses the shorter separately checked graph-free066 support route. Original fresh and author versions remain unchanged; the separate numerical correction4-to6 is explicitly post-author and still below the required8. Minimum degrees, rather than homogeneity of affected products, are asserted.

## SZ4-216 — squared unequal preparation

For N=3K2 or P3+2K2, u=UV,s=C OR u, and f the product of two operands u,s or A OR alpha*s, the expression sL OR fM OR qsf cannot equal the edge function, with arbitrary affine L,M and all zero/repeated cases. Consequently the exact original p3/a3 two-visible literal u=UV,S=C+u,first high g=S*S branch is impossible after whole-current-carrier erasure, with arbitrary third product/second high and no K bound; no other hidden normalization claimed. The local lemma needs no old-neighborhood assumption. The circuit consequence derives the literal third-product operands rather than assuming normalization; g and S have equal Boolean value but remain different original nodes/minimum degrees. Same-occurrence frame squares are excluded by squarefree P2.

## SZ4-217 — alias first high

For exact original p3/a3, two visible cuts, literal old u=UV,S=C+u and first high g=Su or g=u*u, no circuit can realize an H-empty induced3K2 or P3+2K2 target. Full actual third-product/second-high input census, degree-two first selected low, affine contexts, raw fanout and squares are included; arbitrary retained counts and no other hidden normalization.

## SZ4-218 — raw cubic beside unequal preparation

For exact original p3/a3, two visible cuts, literal old u=UV,S=C+u and first high g=uA on four global missing edges inducing P3+2K2 with H[T] empty, no circuit exists for arbitrary K. The third product/second high and relative S/first-cut order are initially unrestricted; complete original census and all actual contexts are proved. This is the stronger impossibility statement; original weaker cover-bound proof is preserved.

## SZ4-219 — complete original R2 cover bound

For the exact original all-visible p3/a3 literal R2 family g=UV,u=AB independent,f=u(C+sum delta_i g_i),with n=1or2 original g occurrences and3-n f occurrences,on four global missing edges inducing P3+2K2 with H[T] empty,vc(G)<=K+2 for arbitrary K. Both highs must be T-unsafe,all selected lows degree1,same-high pair coefficients0;positive mixed coefficient and n=2 are impossible. The remaining n=1/q=0 allocation has a full original-context cover charge. No other operand normalization or numerical-row closure. The unions of contexts are not assumed old. Both independent proofs retain full ambient supports and original retained products for the global charge. The earlier narrower mixed-cross-necessity candidate is preserved without retroactive promotion.

## SZ4-221 — both-affected original R1 exclusion

The exact original all-visible p3/a3 R1 network u=UV,g=uA,f=(B+sum beta_i g_i)(C+sum gamma_i g_i),with both coefficient sums positive,n=1or2 actual g occurrences and3-n f occurrences,cannot supply the four global missing witnesses inducing P3+2K2 with H[T] empty. All scalar/zero contexts,actual same/mixed occurrence coefficients and original degrees/fanout are preserved; arbitrary K. Single-affected R1 and other networks remain outside this impossibility. The proof gives a two-target bound for a safe old cubic times an arbitrary affine context, never assuming the context union old. Original proof versions and the pre-author clause-count wording clarification remain unchanged.

## SZ4-220 — independent quadratic first high beside an unequal preparation

For the exact original p3/a3/two-visible induced P3+2K2 four-global-missing frame, literal u=UV,S=C+u,g=AB with old nonzero homogeneous linear factors and independent original old-quadratic first high g implies vc(G)<=K+2 for arbitrary retained K. The initially unrestricted third product is the second high and has exactly Su,Sg,S^2,or S(D+alpha g) as its surviving literal inputs,with all original identities,degrees,fanout,selected lows and context coefficients retained. Raw alternatives are impossible; the nonraw alternatives satisfy the full original-product cover charge. No other unequal preparation or saving-row closure is asserted. The count is for the original selected products and includes all ambient old edges; Boolean factoring does not change any original node or budget.

## SZ4-222 — the quadratic source itself as the first visible high

The exact original p3/a3/two-visible induced P3+2K2 four-global-missing family with literal old u=UV,S=C+u and first chronological visible high the original source u itself is impossible for arbitrary retained K. The two remaining products and second high are initially unrestricted; their connected product/high/input inventory is derived, preserving every original node,minimum degree,wire repetition,coefficient,fanout,selected low and context. No ordering of S beyond the actual DAG or longer-raw-input/general unequal-hidden classification is assumed. Listed factor occurrences are retained when applying202; Boolean idempotence does not merge original products or alter degrees.

## SZ4-223 — the entire literal old-quadratic unequal preparation

For the exact original p3/a3/two-visible induced P3+2K2 four-global-missing frame with sole hidden literal u=UV,S=C+u and full nonzero old homogeneous linear U,V,C, vc(G)<=K+2 for arbitrary retained K. Both visible highs and the two other private products are initially unrestricted. The original first-high/remaining-product/high-boundary census is derived with all minimum degrees,full carriers,fanout,repetitions,coefficients,lows and contexts fixed. No longer raw input,affected C or general hidden normalization is claimed. Earlier individual first-high proofs remain inline as explicit prerequisites; the current opening/residual now uses this stronger complete family bound.

## SZ4-224 — the complete single-affected original R1 cover bound

For the exact original all-visible p3/a3 induced P3+2K2 four-global-missing family u=UV,g=uA,f=C(B+sum beta_i g_i), with full old factors,one affected final input,n=1or2 actual g occurrences and3-n f occurrences,vc(G)<=K+2 for arbitrary retained K. All original minimum degrees,occurrences,lows,context coefficients,fanout and retained-product incidences are preserved. Together with221 this removes all R1 from the gain-three minimum-retained row; nonraw three-high table,R3 and other numerical cases remain outside this claim. The full actual context, rather than its restriction to T or a rewritten product, supplies the original K-product charge. No proof route from223 is a premise.

## SZ4-225 — affected degree-one input beside an old quadratic source

For the exact original p3/a3/two-visible induced P3+2K2 four-global-missing frame, let the sole hidden sum be S=R+u, u=UV with full unaffected old homogeneous linear U,V, and actual degree-one R=C+beta*g, beta>0, where g is the first visible high and C its nonzero old selected part, not necessarily an available wire. With both highs and the other products initially unrestricted, vc(G)<=K+2 for arbitrary retained K. All original minimum degrees, occurrences, coefficients, fanout, lows, contexts and retained-product incidences are preserved. Longer or affected raw sources and other hidden placements are not normalized. The full first/second-high original census and all scalar/cross cases are proved inline. No new old wire is introduced for the selected part C.

## SZ4-227 — arbitrary raw source beside a genuinely affected hidden input

For the exact original p3/a3/two-visible induced P3+2K2 four-global-missing frame, suppose the sole hidden addition has literal inputs S=R+u with actual retained degree-one boundary R=C+beta*g,beta>0,first visible high g,and nonzero full old selected part C not necessarily available as a wire. The source u is any raw original private-product output with initially unrestricted inputs,minimum degree and ancestry. Then vc(G)<=K+2 for arbitrary retained K. Every original node,degree,occurrence,coefficient,fanout,low,context and retained-product incidence is preserved. The unaffected-input case with a longer/affected raw source,remaining all-visible types and matching attachments are not classified. The full original timing/source/last-input inventory is proved inline;225 remains an explicit admitted prerequisite rather than a silently broadened scope.

## SZ4-226 — the complete original repeated R3 cover bound

For the exact original all-visible p3/a3 induced P3+2K2 four-global-missing R3 family g=UV,u=(A+sum beta_i*g_i)(B+sum gamma_i*g_i),f=u(C+sum delta_i*g_i), with full old nonzero linear factors,n=1or2 actual g occurrences and3-n actual f occurrences,and no u insertion,vc(G)<=K+2 for arbitrary retained K. At least one middle input is affected; if both are affected,their positive index sets are the same singleton. All actual temporal restrictions,minimum degrees,coefficients,squares,crosses,lows,contexts,fanout and original retained-product incidences remain fixed. Together with219/221/224 this excludes all repeated-high alternatives of211,leaving the nonraw three-distinct-high table and other hidden/matching cases open. Full common-prefix rigidity is explicitly proved; the final ambient cover counts original retained multiplication nodes.

## SZ4-228 — An unaffected hidden input with a proper ancestral raw source

In the exact original three-private-product/three-private-addition frame with two visible cuts, four global missing edges inducing P3+2K2 and nonempty H with H[T] empty, let the sole hidden addition have literal inputs S=C+u, where C is an actual full unaffected nonzero old homogeneous linear input wire and u is a raw private-product output of original minimum degree at least two. If u is a proper surviving original descendant of the first visible high g, then vc(G)<=K+2 for the arbitrary original retained product count K. All original node/input/insertion identities, minimum degrees, coefficients, fanout, lows, full contexts and retained-product incidences are preserved. Source inputs and the second high are initially unrestricted; either possible actual order of the first insertion and S is allowed. No retained optimality, Boolean-identity wire replacement, or numerical-row closure is inferred. Full pair 2026-11-25T22:46:04.879212+00:00; author/fresh/readback/forward/reverse versions and exact main transcription are linked in the register.

## SZ4-229 — An unaffected hidden input whose raw source is the first high

In the exact original three-private-product/three-private-addition frame with two visible cuts, four global missing edges inducing P3+2K2 and nonempty H with H[T] empty, let the sole hidden addition have literal inputs S=C+u, with C an actual full unaffected nonzero old homogeneous linear input wire and u a raw original private-product output. If the first visible high is the SAME ORIGINAL product node u, then vc(G)<=K+2 for arbitrary original retained K. The source inputs, minimum degree, ancestors and second high are initially unrestricted; no order between the first insertion and S is imposed. All original nodes/occurrences, minimum degrees, coefficients, fanout, lows, full contexts and retained-product incidences, including scalar/zero cases and repeated inputs, stay fixed. The old-quadratic case invokes223 only after its literal original-input hypotheses hold. No228 dependency or numerical-row closure is claimed. Full pair 2026-11-25T22:46:42.677141+00:00; author/fresh/readback/forward/reverse versions and exact main transcription are linked in the register.

## SZ4-230 — the full actual unaffected-input hidden-preparation family

In the exact original three-private-product/three-private-addition frame with two visible cuts, four global missing edges inducing P3+2K2 and nonempty H with H[T] empty, let the sole hidden addition have literal inputs S=C+u, where C is an actual full unaffected nonzero old homogeneous linear input wire and u is any raw original private-product output of original minimum degree at least two. Then vc(G)<=K+2 for the arbitrary original retained product count K. Source inputs, minimum degree, ancestry and first/second-high identities are initially unrestricted. All original nodes, operand and insertion occurrences, coefficients, fanout, selected lows, full contexts and retained-product incidences are preserved, including repeated inputs and scalar/zero context cases. The old-quadratic, same-first-high and proper-descendant theorems are applied only at their exact original-input hypotheses; every other source relation is covered by the complete original-node inventory. No retained optimality, Boolean-support wire replacement, all-visible normalization, matching-attachment or numerical-row closure is inferred. Full pair 2026-11-25T23:16:07.716635+00:00; all original versions, complete independent proofs, readbacks, comparisons and main transcription are linked in the register.

## SZ4-232 — the complete two-visible path reduction

In the exact original three-private-product/three-private-addition frame with two visible cuts, four GLOBAL missing edges inducing P3+2K2 and nonempty H with H[T] empty, arbitrary retained K and the stipulated whole-current-carrier-erased/pruned polynomial P*, if vc(G)>K+2 then the unique hidden addition is the single-use second visible high S=u+v with raw private-product operands and original degree-one selected low a. The exact arithmetic reassociation a+(u+v)=(a+u)+v gives an all-visible circuit with the same P*,quadratic frame,H,K and product nodes; two additions replace two additions. The original first high,u,v remain distinct insertion occurrences even when nodes or Boolean values coincide. Equivalently either vc(G)<=K+2 or this exact all-visible representative exists. No retained optimality, identity of addition DAGs, equality to the unerased higher polynomial, all-visible/matching/numerical closure is inferred. This checked synthesis of213/227/230 earns no additional mathematical-movement credit beyond actual review30. Full proof-pair completion2026-11-25T23:50:01.181408+00:00; complete original versions, precision history, mutual comparisons and exact transcription are linked in the register.

## SZ4-233 — two target potentials and seven zero-cross reductions

For a positive variable-input circuit on finite simple C4-free G with nonempty squarefree quadratic support H, exactly four GLOBAL missing edges xy,xz,ab,cd inducing P3+2K2 on T with H[T] empty, a fixed original selected frame with arbitrary K retained products, exactly three deleted original products and three visible deleted additions, three distinct product highs inserted once apiece, and every private operand of original minimum degree one with nonzero old homogeneous base plus compatible earlier insertions: (A) each actual private-product value is true on at least two distinct target edge assignments, with no unique/first-true or injective allocation claim. (B) If all original pairwise occurrence coefficients are zero, vc(G)<=K+2 for the exact patterns g=UV and (h,f) equal (AB,(C OR g)D), (AB,D(C OR g OR h)), (AB,(C OR g)(D OR g)), (AB,(C OR g)(D OR g OR h)), ((A OR g)B,CD), ((A OR g)(B OR g),CD), or ((A OR g)(B OR g),(C OR g)D). All old forms are full nonzero homogeneous forms and may repeat; coefficients, original nodes/degrees/occurrences, selected lows, fanout, full contexts and retained incidences remain fixed. No other cell, positive-cross allocation, full231 or numerical-row closure is inferred. Full pair completed2026-11-26T00:27:35.686807+00:00; both entire pre-exposure proof/readback gates and full comparisons are linked in the register. Original231 partial origin remains disclosed without claiming full231.

## SZ4-234 — Unsafe nonraw highs and the complete split cell

For a positive variable-input circuit on a finite simple C4-free G with nonempty ordinary squarefree quadratic support H, exactly four GLOBAL missing edges xy,xz,ab,cd inducing H-empty P3 disjoint2K2 on T, a fixed original selected frame with arbitrary retained-product count K, exactly three original private products and three visible private additions, three distinct product highs inserted once each, and every original private-product input of minimum degree one with nonzero old homogeneous base plus compatible earlier original insertion contributions: (A) all three original high Boolean functions are globally unsafe on G, each true on a G-independent assignment. (B) If any original high v_k implies both v_i and v_j for distinct insertion occurrences i,j, the actual pair coefficient q_ij is zero; k may equal i or j. Neither A nor B assumes vc(G)>K+2. (C) The entire double/split cell g=UV, h=(A OR g)(B OR g), f=(C OR g)(D OR h OR epsilon*g), epsilon0/1 with all actual q initially unrestricted, satisfies vc(G)<=K+2. All full old forms, original nodes/degrees/cuts/coefficients/lows/paths/fanout/contexts and retained incidences remain fixed; support absorption changes no counted gate. The auxiliary proof openly changes its own H to H-prime; only the final cover proof charges the original K. No full231, other row, matching-attachment or numerical closure.

Complete separate author/fresh proofs and ENTIRE readbacks preceded author exchange; both full comparisons PASS without repair. Admitted233 background disclosed. A/B have no cover inequality; complete original C proof retained. Full pair: 2026-11-26T01:03:34.459155+00:00. Complete sources and exposure chronology are linked in the register.

## SZ4-235 — The complete double-affected-middle row

For a positive variable-input circuit on a finite simple C4-free G with nonempty ordinary squarefree quadratic support H, exactly four GLOBAL missing edges xy,xz,ab,cd inducing H-empty P3 disjoint2K2 on T, a fixed original selected frame with arbitrary retained-product count K, exactly three original private products and three visible private additions, three distinct product highs inserted once each, and every original private-product input of minimum degree one with nonzero old homogeneous base plus compatible earlier original insertion contributions: The entire double-affected-middle row h=(A OR g)(B OR g), g=UV, satisfies vc(G)<=K+2 for all four exact last-product cells f=CD, (C OR g)D, C(D OR h OR epsilon*g), (C OR g)(D OR h OR epsilon*g), epsilon0/1. Every actual q12,q13,q23 is initially unrestricted. All full nonzero old forms may repeat; actual affected-boundary, degree, low/context, coefficient, occurrence, fanout and original retained-product incidences remain fixed. Optional g coefficients remain recorded despite Boolean absorption. The proof uses admitted233 exact necessity and old-factor/context facts, not234 or230. Only this entire middle row is removed; independent/single-affected rows, matching attachments, full231 and the numerical saving row remain open.

Complete separate author/root proofs and ENTIRE readbacks preceded235 author exchange; both full comparisons PASS without repair. Limited related234 strategy-label exposure was disclosed and not used; no pristine isolation from every related hint is claimed. Neither234 nor230 is a proof premise. Full pair: 2026-11-26T01:21:13.848211+00:00. Complete sources and exposure chronology are linked in the register.

## SZ4-231 — prop:allvisiblethreeproductcover

For a positive variable-input circuit on finite simple C4-free G, with nonempty squarefree quadratic support H and exactly four GLOBAL missing edges xy,xz,ab,cd inducing H-empty P3 disjoint2K2, keep the exact original selected quadratic frame and arbitrary retained multiplication count K. If canonical extraction/pruning deletes exactly three ORIGINAL multiplication nodes and three ORIGINAL addition nodes, all additions visible, then vc(G)<=K+2. All original ancestry, raw/affected operands, minimum degrees, repeated high values or high nodes across distinct insertion occurrences, compatible scalar/zero contexts, actual cross coefficients, full lows/paths/contexts and retained-product incidences are initially unrestricted and preserved. Boolean support identities create no wire, identify no original node and change no original degree or counted gate. This proves the whole all-visible path-target family, not hidden additions, matching attachments, other outside shapes, empty H or the unrestricted numerical row. Combined with admitted232 in the saving row, it excludes the path outside shape; three-matching attachments remain open.

Separate complete author/fresh proofs and ENTIRE readbacks preceded same-claim exchange; both full comparisons and entire comparison readbacks PASS. Checker complete v2 used admitted<=229 only; later233/234/235 clean-statement reads were comparison-phase exposures. Author used admitted233/234/235 and full inline row proofs; no236 proof dependency. Part D transcription clarifies minimum-degree-two, already correct in Part A; original proofs unchanged and no mathematical repair. No new230 proof route used.

Sources: checks/paper3_all_visible_three_product_cover_statement.md; checks/paper3_all_visible_three_product_cover_author_complete_v1.md; checks/paper3_all_visible_three_product_cover_author_complete_v1_entire_readback.json; checks/paper3_all_visible_three_product_cover_author_complete_v1_copy_manifest.json; checks/outage_20261125/circuits/SZ4-231_independent_complete_v2_node_identity.md; checks/outage_20261125/circuits/SZ4-231_independent_complete_v2_readback.json; checks/outage_20261125/circuits/SZ4-231_forward_comparison_v1.md; checks/outage_20261125/circuits/SZ4-231_forward_comparison_v1_entire_readback.json; checks/outage_20261125/operator_k/SZ4-231_reverse_comparison.md; checks/outage_20261125/operator_k/SZ4-231_reverse_comparison_entire_readback.json; checks/outage_20261125/root/SZ4-231_pair_closeout.json; checks/outage_20261125/circuits/SZ4-231_insert.tex; checks/outage_20261125/circuits/SZ4-231_insert_entire_readback.json; checks/outage_20261125/root/checkpoint46_both_stages_entire_root_readback.json.

## SZ4-236 — prop:independentmiddlerow

For the exact original three-private-product/three-private-addition all-visible frame on a finite simple C4-free G with nonempty H and exactly four GLOBAL missing edges xy,xz,ab,cd inducing H-empty P3 disjoint2K2, arbitrary retained-product count K, three distinct original product highs inserted once each and minimum-degree-one original product inputs, let independent old quadratics g=UV,h=AB precede f of type OG,OJ,GG,GH or GJ: (C OR g)D, D(C OR g OR h), (C OR g)(D OR g), (C OR g)(D OR h), or (C OR g)(D OR g OR h). With every actual q12,q13,q23 initially unrestricted, full contribution gL OR hN OR fM OR q12gh OR q13gf OR q23hf safe and supplying all four witnesses implies vc(G)<=K+2. All full old bases, original nodes/degrees/occurrences/coefficients/lows/paths/fanout/contexts and retained incidences remain fixed; old bases need not be standalone wires. This independently excludes the entire independent-middle row, not the single-middle, matching or unrestricted numerical family.

Separate complete operator author and foundation fresh proofs and ENTIRE readbacks preceded exchange; both full comparisons and entire readbacks PASS without repair. Foundation pre-author partial correction is preserved. Root236 attempt remains explicitly INCOMPLETE partial and receives no complete fresh-proof credit; root acted as editor only. No231 premise.

Sources: checks/paper3_independent_middle_row_statement.md; checks/paper3_independent_middle_row_author.md; checks/paper3_independent_middle_row_author_entire_readback.json; checks/paper3_independent_middle_row_author_copy_manifest.json; checks/outage_20261125/foundation/SZ4-236_independent_complete_v1.md; checks/outage_20261125/foundation/SZ4-236_independent_complete_v1_readback.json; checks/outage_20261125/foundation/SZ4-236_independent_complete_v1_original_scratch_save.json; checks/outage_20261125/foundation/SZ4-236_independent_partial_v1.md; checks/outage_20261125/foundation/SZ4-236_pre_author_partial_precision.md; checks/outage_20261125/foundation/SZ4-236_forward_comparison.md; checks/outage_20261125/foundation/SZ4-236_forward_comparison_entire_readback.json; checks/outage_20261125/operator_k/SZ4-236_reverse_comparison.md; checks/outage_20261125/operator_k/SZ4-236_reverse_comparison_entire_readback.json; checks/outage_20261125/root/SZ4-236_pair_closeout.json; checks/outage_20261125/foundation/SZ4-236_insert.tex; checks/outage_20261125/foundation/SZ4-236_insert_entire_readback.json; checks/outage_20261125/root/checkpoint46_both_stages_entire_root_readback.json.


## paper5_gemini_dictionary

# Gemini originals: precise translations

The original name globalization means FGJM zero adjunction, with a new additive
identity and multiplicative absorber distinct from the old ring zero. A singlet
means a fixed point of a specified unit-group action; it does not define an
additional symmetry theory. The action fixes the new zero and the annihilator of
the ideal generated by unit differences. The two-zero pair is the Boolean
semiring with unit equal to the old zero.

Integral or semidomain is translated separately into absence of new-zero
divisors and multiplicative cancellation. The first always holds for R_0; the
second fails at the old zero whenever R is nonzero. The correct spectrum is
specified by its ideal convention. Forgetting addition gives multiplicative
monoid ideals and a different, infinite-dimensional spectrum for Z_0.

The absorber extension is a zeroless inverse semiring as in FGJM Section 3.1.
Nonempty absorbing ideals may omit its additive identity and add a generic point;
requiring the identity removes that singleton ideal. Neither convention repairs
the standard semimodule zero axioms, which force the trivial module.

The original monoid-algebra symbol is translated to a contracted ordinary
integral monoid ring, not to the inverse-semiring coefficient construction
Z_0[M]. Its old-zero central idempotent splits off Z. The source's proposed
single Euler factor is not Deitmar's finite-type zeta definition. An ideal norm
must name its congruence quotient, and an ideal-class relation must name its
allowed multipliers: the old zero destroys the unrestricted class relation.

These statements connect to ordinary schemes through the ring reflection and
the closed old spectrum, to monoid schemes through contracted monoid base change,
and to ordinary ideal-class theory through regular fractional ideals. No motive,
correspondence or geometric class-field cover is inferred from the change of
zero alone. Exact source cotes are retained in the crosswalk.


## paper5_november1_dictionary

# Scope of the GCT and GRH consult translations

Finite witness support, coefficient signs, canonical-basis existence and polynomial-time accessibility are separate data. The canonical N→Z0 map identifies nonempty positive counts with occupied nonzero integers, but does not encode efficiency. Isolation of one signed term concerns a weighted polynomial before specialization; ring cancellation at the specialization remains possible. These distinctions match SZ4-018 and SZ4-026.

Fixed finite skeletons must be specified as constant sheaves or locally constant objects with transport. A functor from a fixed finite poset to ordinary sheaves is an ordinary diagram category. It does not by itself define derived functors on the full category of variable-support inverse-semiring sheaves. Weight assertions require an actual Weil realization and the hypotheses of the corresponding cohomology theorem. SZ-NOV-FIXED-SHEAF records that unresolved framework instead of importing a general purity theorem.

The arithmetic complexity catalogue concerns ordinary schemes and finite covers. Rephrasing nonemptiness as a Boolean coordinate does not make those independent analytic theorems depend on zero adjunction; they remain in OTHER_RESULTS. The granted Dirichlet input is not enlarged to arbitrary number-field zeta functions.


## paper5_november2_dictionary

# Trace, dimension, Boolean presentation, and fixed realization

A finite R0-semimodule with a finite support lattice is a finite diagram of ordinary modules. Choosing complex or l-adic finite-dimensional fibres and compatible Frobenius maps is additional realization data. A signed Möbius sum of fibre traces is an ordinary finite signed trace. In particular it has a fixed finite set of possible exponential roots. SZ5-prop-fixed-diagram-obstruction proves the obstruction without importing the earlier archive-specific scalar40.

The plain sequence Tr(F^n) has only simple generating-function poles even if F has Jordan blocks. An inserted sequence Tr(AF^n) can have higher poles, but its pole locations still belong to the reciprocal spectrum of the same finite F. These two statements must not be exchanged. An unbounded family of point-count varieties Y_n is not one fixed Frobenius object, and the order of a Hilbert-series pole is not by definition an arithmetic conductor.

Any integer Laurent polynomial has effective even and odd parts. A specified Boolean cube with zero transition maps can likewise display a binomial signed trace. These are legitimate coefficient presentations under the module-diagram theorem; none makes the cube canonical or equips its fibres with associative composition. SZ-NOV-COEFFICIENT-CATEGORIFICATION retains that precise gate. Half-integral formal grading does not automatically provide an arithmetic half-Tate object.

The rank-four word order overZ[D] and one explicit localization are now specified in the manuscript. A least coefficient ring depends on a chosen order, basis and positivity constraint. The historical claim that a finite search bound follows from the rank-three pattern has no supplied proof, and SZ-NOV-E4-CANONICAL retains that gap. Neither a positive Gram form nor rationality of coordinates solves it.

The quantum-integer Weil-restriction examples are individual ordinary geometric realizations. Their one-step traces can differ from graded dimensions because Frobenius permutes the geometric factors. They do not give a simultaneous algebra object without additional multiplication maps. The source enumeration132/116/16 and its alternative180-entry normalization have not been adopted as independent computations in this run.


## paper5_november3_dictionary

# Repairs in the implications consult

Finite projective labels may be zero. Tensor products retain those support vertices, so an unrestricted negative power of rank is undefined and the asserted rank≥number-of-vertices inequality fails. SZ1-051 uses only positive ranks. The semiring-scheme QCoh equivalence uses the precise module convention of Paper1; changing to a different relative or blue module theory is not automatic.

The prime correspondence gives one height increment above every minimal prime ofR, not a unique height-one prime for every ring. For exampleR=k×k has two minimal primes and hence two height-one primes after zero adjunction. The old zeroe is idempotent and is not a regular equation of an effective Cartier divisor. The correct ideal and regular-class statements are SZ1-002 and SZ5-prop-class-collapse.

The later phase discussion correctly rejects CLT→modulo-two equidistribution, but its reflection-symmetry sufficient condition needs a boundary qualification. The probability measure equally supported at0and1 modulo2 is invariant under reflection and has zero odd Fourier coefficients, yet gives mass0to the open semicircle(0,1). The manuscript's full equidistribution condition avoids that boundary counterexample, and its arctangent term gives the exact initial direction.

The positive cone generated by(v−v^{-1})^a f(v), f with nonnegative coefficients, is pointed by evaluation at any realv>1. Evaluation only atv=1, as in the source sketch, does not itself rule out nonzero elements vanishing there. The Boolean inclusion–exclusion identity is formal; half-integral arithmetic twists and compatible multiplication objects require extra definitions.

Point-count formulas from affine pavings or torifications use the decompositions themselves. Equality of a virtual class to a polynomial is weaker and does not force an affine paving or even cohomology. Boolean eventual periodicity likewise does not alone assign a Weil weight; an actual finite-monodromy realization is needed. The inserted-operator and plain Frobenius trace distinctions are made explicit in Paper5.

The source does not verify every Selberg-class hypothesis of its functional-equation argument. SZ-NOV-SEPARATED-FE therefore keeps a precisely delimited open analytic-class problem; the meromorphic continuation already proved is not used as a substitute. The task grants inputA, not the unrelated external algorithmic hypothesisE or arbitrary number-field GRH.


## paper5_november4_dictionary

# Scalar sign, Frobenius sign, and categorical realization

The fixed-point formula SZ1-009 concerns multiplication by a fixed ring unit. It must not be confused with an even iterate of a chosen Frobenius representation. For the integer sign, epsilon^2=1 is not fixed by epsilon and is not in the Boolean pair. In a representation with eigenvalues plus or minusq^j, an even Frobenius power does give the unsigned dimension-weighted trace; that different statement is part of SZ2-thm-sign-main.

The effective coefficient criterion SZ5-prop-criterion constructs an associative table in the parity semiring. A monoidal category also needs objects, morphisms, tensor functors, associators and the pentagon coherence. An arithmetic geometric realization needs still more. Numerical associativity alone supplies none of that omitted data. The framework gate remains SZ-NOV-COEFFICIENT-CATEGORIFICATION. Likewise a rationalQ(D)coefficient can have a pole and need not be a finite Laurent polynomial; the word-order descent theorem does not make every rational basis a finite Tate basis.

The right-moving label of a simple Hurwitz zero is a Borel function of its exact phase, with the arctangent offset in SZ2-prop-zero-phase. It is not an additive character of the phase circle. A normalizedCLT does not imply fixed-frequency decay. The source first-moment velocity claim also needs a definition at multiple zeros or a simplicity hypothesis and additional analytic estimates; it is not admitted merely from inputA.

The Connes–Consani comparison first needs a named additive or Gamma-ring construction. A pointed monoid alone has no specified addition. The established ordinary semiring-scheme statements do not identify the points or topos of an unspecified compactified arithmetic refinement. The source-wide claim that every theorem automatically has a split-zero refinement is therefore not a theorem here.


## paper5_word_dictionary

# Integral Hecke word order and positivity

SZ5-thm-hecke-word-descent specifies an ordinary associative order A over Z[D], embedded in the Hecke tensor algebra, and proves finite generation, torsion-freeness, faithful Laurent scalar extension and integrality of regular characteristic polynomials. The proof uses a finite free coefficient extension and semilinear fixed-word coordinates. The diagram supplies the algebraic order that was missing from the earlier rank-four question; it is not an effective dimension semiring, a canonical basis or a motivic realization. The regular trace is a particular additive invariant, not the character of an individually descended simple representation.

SZ5-cor-hecke-word-localization gives an effective form of generic freeness: a selected nonzero coordinate minor makes a chosen word basis integral. It does not select a smallest localization, and a rational coefficient in that localization is not automatically a Laurent sign-Tate trace. The precise connection to the project's degree-one direction therefore still needs an effective class and its specified arithmetic realization. Cotes: the rank-four question in the prompt and structural/GCT §4.2–4.3; published generators are Blasiak, Mulmuley and Sohoni (2013), Definition 11.1 and equation (93).

SZ5-prop-bottom-shift-obstruction translates another basis-search obstruction into positivity of a finite-dimensional real algebra at positive q. The bottom central idempotent has a positive coordinate vector, and the three bottom coefficients satisfy a common sign relation. Their required trace-support degrees violate that relation at both ends unless at least two extra weights occur. This excludes bottom shears of the displayed B/C dimension examples, with arbitrary complementary bottom vector. It makes no assertion about all positive bases or all effective lifts.

SZ5-prop-rank4-word-minor makes the selected-minor certificate concrete:114 printed words and coordinate rows define g(v), and the fourfold norm defines f(D). The exact nonzero modular residue is independently replayed. The generic upper dimension114 is a published input, not deduced from specialization. The resulting localization is sufficient, not minimal, and no positive-basis or finite-motive realization follows.


## Canonical statement translations

The following index gives the standard-language statement of every canonical series row. The term correspondences above specify the meanings of support, fiber, packet, occupied zero and the other source terminology. Unadmitted and corrected claims keep their stated status; indexing a claim does not verify it. Exact source occurrences and proof/check locators remain in REGISTER.tsv and CROSSWALK.tsv.

| Canonical id | Statement in the stated standard vocabulary | Paper | Current status |
|---|---|---|---|
| GATE-ZP-001 | The scalar coefficient square is the usual zero-adjunction square; the accompanying analytic packet and support-base identifications require their separately supplied framework. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-002 | The claimed reconstructed linear lifts of every coefficient map require explicit coherent support diagrams and support maps; those inputs are not verified here. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-003 | The scalar square and Boolean zero-ring boundary are standard zero-adjunction data; the actual arithmetic support carriers require their separate definitions. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-004 | The scalar square is standard zero adjunction; the asserted supported quotient and cohomology identifications depend on the separately specified analytic framework. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-005 | The assertion that all original support labels and cohomology classes remain unchanged requires the supplied source maps; it is not certified by the ordinary scalar inequality. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-006 | Standard scalar zero-adjunction data accompany a fixed-width transfer for a specified reflection-stable analytic packet; the imported support framework is not reconstructed here. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-007 | The reconstructed sum-coordinate inclusion and projection are asserted to preserve the original support labels; a complete coherent support diagram is required. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-008 | The least-norm correction is asserted to be an original theta boundary whose split lift becomes the supported zero at its label; the primitive and support maps must be supplied. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-009 | The lifted arithmetic quotient is asserted to keep killed amplitudes at their receiving support label and keep external absence separate; the actual source carrier is an input gate. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-010 | The inside/outside norm decomposition is asserted to lift to the retained support diagram; its scalar Hilbert-space identity alone does not specify that lift. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-011 | The boundary correction is asserted to carry a compatible supported-zero lift; the source primitive and receiving support need verification. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| GATE-ZP-012 | The conormal quotient maps are asserted to lift while retaining old zero and external absence separately; coherent source and target support diagrams are required. | 2 | unadmitted; missing coherent arithmetic support carriers and maps; no proof check credited |
| SZ-AR-001 | The supported-coordinate model identifies the zero-adjoined ring with one unsupported point and one full ring fibre. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-002 | The unital Boolean homomorphism is uniquely the support character. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-003 | Reflection merges the two zero elements, while Boolean support singles out only the new zero. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-006 | A semimodule element absorbs its additive idempotent support under addition. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-009 | A join diagram of ring modules reconstructs the semimodule by disjoint union and transport to joins. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-012 | A free semimodule has a Boolean cube of supports, with the ordinary coordinate modules as fibres. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-016 | Units and nonzero supported irreducibles agree with those of the domain; the old zero retains its special divisibility behavior. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-058 | Every finite-group character evaluation lifts functorially to the zero-adjoined representation ring and preserves support. | 5 | independent derivation saved before original proof; primary Serre locator verified; manuscript input ready |
| SZ-AR-059 | On a prescribed set of grades, genuine representations exist uniquely exactly when all irreducible-character inner products are nonnegative integers. | 5 | independent derivation saved before original proof; primary Serre locator verified; manuscript input ready |
| SZ-AR-060 | All multiplicities vanish exactly for the zero representation class, which remains supported on a grade chosen to be present. | 5 | independent derivation saved before original proof; primary Serre locator verified; manuscript input ready |
| SZ-AR-070 | A finite list of representation-ring coefficients has the ordinary Boolean support skeleton. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-071 | Changing a present coefficient to the old zero retains its grade, while changing it to the new zero removes that grade. | 1 | duplicate of already checked retained construction; no new independent proof claimed here |
| SZ-AR-074 | Character inversion uses the dual character; omitting conjugation extracts the dual irreducible multiplicity instead. | 5 | independent derivation saved before original proof; primary Serre locator verified; manuscript input ready |
| SZ-NOV-CC-REFINEMENT | Sectionwise zero adjunction is proposed to refine the Connes–Consani compactified arithmetic structure and its topos, but no precise compatible geometric category and comparison functor are constructed. | 1 | unadmitted framework; not a theorem of the named ordinary semiring-scheme model |
| SZ-NOV-COEFFICIENT-CATEGORIFICATION | Separate geometric or sign-Tate realizations of individual structure constants do not yet give coherent composition maps realizing the algebra multiplication. | 5 | open; associative categorification not supplied by coefficientwise realizations |
| SZ-NOV-E4-CANONICAL | A canonical rank-four basis calculation requires a specified minimization order, normalization and termination or finite-bound theorem, none supplied by the source extrapolation from rank three. | 5 | open; canonical positive basis and finite search bound not established |
| SZ-NOV-EVEN-SIGN | The assertion that even powers of the scalar sign land in its Boolean fixed-point pair is false; scalar powers and Frobenius traces are distinct. | 1 | refuted; refined statements SZ1-009 and SZ2-thm-sign-main |
| SZ-NOV-FIXED-SHEAF | For a specified constant finite support semilattice, fixed-support R0 sheaf data can be formulated as a diagram of ordinary module sheaves, but the source cohomology and purity assertions require a named sheaf category and exact constructibility/lisse hypotheses. | 1 | framework required; not admitted as stated |
| SZ-NOV-NONSTANDARD-RH-REALIZATION | A full equivalence between a specified nonstandard RH problem and external Dirichlet RH plus effective dimension-ring existence requires a named basis, finite arithmetic realizations, and coherent categorical or geometric data; the source does not establish that equivalence in general. | 5 | unadmitted framework gate; exact nonstandard RH statement and required realizations remain to be specified |
| SZ-NOV-PHASE-CHARACTER | The half-circle right/left indicator is not a character of the additive phase circle, and the displayed quotient by another circle is not well-defined as written. | 2 | refuted; refined statement SZ2-prop-zero-phase treats it as a Borel label |
| SZ-NOV-SEPARATED-FE | The shifted ideal-counting sheet over a higher-degree number field has the proved meromorphic continuation, while a functional equation in a precisely specified analytic class remains unproved. | 2 | open; analytic class and hypotheses must be fixed before a nonexistence theorem |
| SZ-NOV-VELOCITY-MOMENT | The proposed sum of initial Hurwitz-zero velocities has a stated main term, but the source omits simplicity and the needed contour, reciprocal-derivative and remainder estimates. | 2 | unadmitted analytic claim; RH alone does not establish the simple-branch sum or its estimates |
| SZ1-001 | Zero adjunction R↦R_0 is FGJM Definition 3.6. | 1 | background |
| SZ1-002 | Ideals are {tau} and J∪{tau}; primes are {tau} and p∪{tau}; all ideals subtractive; zerosumfree and no new-zero divisors. | 1 | proved |
| SZ1-003 | Spec R_0 adds one generic open point, with Boolean stalk; other stalks (R_p)_0; O(eta∪U)=O_R(U)_0. | 1 | proved |
| SZ1-004 | Congruences have kept-new-zero and collapsed-ring families indexed by ideals J. | 1 | proved |
| SZ1-005 | R_0→R is the universal ring reflection. | 1 | proved |
| SZ1-006 | Zero adjunction is fully faithful on commutative unital rings. | 1 | proved |
| SZ1-007 | For every injective ring homomorphism R→K, R_0≅R×_K K_0. | 1 | proved |
| SZ1-008 | (A×B)_0≅A_0×_B B_0 using support maps. | 1 | proved |
| SZ1-009 | Unit-fixed points are Ann_R((u−1:u∈R×))∪{tau}; the Boolean pair occurs iff the annihilator is zero. | 1 | proved |
| SZ1-010 | Every R_0-semimodule is a diagram of R-modules over a zero join-semilattice; the least fiber may be nonzero. | 1 | proved |
| SZ1-011 | Localization at supported s preserves the support semilattice and localizes each group; generic localization is the support semilattice. | 1 | proved |
| SZ1-012 | Cancellative R_0-semimodules are ordinary R-modules via ring reflection. | 1 | proved |
| SZ1-013 | Finite projective R_0-semimodules are finite posets labelled by finite projective R-modules, with fibers the direct sums over ideals. | 1 | proved |
| SZ1-014 | Projective R_0-semimodules with one idempotent consist only of the zero object; no nonzero ordinary R-module is projective. | 1 | proved |
| SZ1-015 | V(R_0) is free commutative on connected labelled posets; K_0 is free abelian on the same types, with labels in V(R). | 1 | proved |
| SZ1-016 | Finite strongly projective R_0-semimodules are free; SV=N and SK_0=Z. | 1 | proved |
| SZ1-017 | Ring reduction of a finite labelled-poset projective is the direct sum of its ring labels. | 1 | proved |
| SZ1-018 | In the stated ordinary-semimodule semiring-scheme convention, QCoh(Spec R_0) is diagrams of QCoh(Spec R) over zero join-semilattices. | 1 | proved |
| SZ1-019 | Modules over an inverse semiring (Q,F) are group diagrams over Q-semimodules with natural bilinear unitary associative action maps. | 1 | proved |
| SZ1-020 | Modules over I(f) are R-module diagrams with natural A⊗G_l→G_0 maps whose composites to G_l are multiplication by f(a). | 1 | proved |
| SZ1-021 | I(id_R)≅R×B; its semimodules and finite projectives split into ring and Boolean factors. | 1 | proved |
| SZ1-022 | Every finite projective over (Q,F) has explicit support/fiber idempotent-matrix data, with U,V matrix certificates for isomorphism. | 1 | proved |
| SZ1-023 | Repeated zero adjunction gives a chain of idempotents, a chain of new generic primes, and the stated chain/local-ring stalks. | 1 | proved |
| SZ1-024 | Modules over R^[k] are R-module diagrams with nested commuting scalar truncations p_i p_j=p_min(i,j). | 1 | proved |
| SZ1-025 | Finite projectives over every R^[k] are coloured finite posets with greatest lower truncations at every positive level, and top-colour projective R labels. | 1 | proved |
| SZ1-026 | V and K_0 for R^[k] are free on connected coloured labelled types; all finite strongly projectives are free and SK_0=Z. | 1 | proved |
| SZ1-027 | Adjoining a double absorber breaks zero absorption and lies in FGJM zeroless inverse semirings for inverse input. | 1 | proved |
| SZ1-028 | With ideals containing the additive identity, absorber adjunction preserves Spec B and adds no point. | 1 | proved |
| SZ1-029 | Usual zero-preserving unital semimodule axioms over double-absorber adjunction force the zero module, hence only zero finite projective. | 1 | proved |
| SZ1-030 | R_0[M] is the inverse-semiring pair (finite subsets of M, R^U) with convolution and zero-extension transitions. | 1 | proved |
| SZ1-031 | The finite labelled-poset projective classification over R_0 holds for arbitrary unital rings and left modules. | 1 | proved |
| SZ1-032 | Finite projectives over every FGJM I(f) are gluing triples (P,N,phi:P/IP≅N_top), with P projective over R and N projective over (R/I)_0, modulo full diagram isomorphisms. | 1 | proved |
| SZ1-033 | Replacing the Peiffer bimodule A by its image ideal preserves finite-projective isomorphism classes and direct sums, via square-zero lifting in fixed-support matrix rings. | 1 | proved |
| SZ1-034 | For bounded distributive L, G_L(R) has ring reflection R, Boolean characters Spec_lat L, subtractive ideals of two types, ordinal-sum spectrum, and explicit localizations. | 1 | proved |
| SZ1-035 | Lattice characters give branch quotients G_L(R)→R_0, and finite lattice spectra are the join-irreducible posets with order-ideal topology. | 1 | proved |
| SZ1-036 | For nonassociative amplitudes the projection forgetting support is not a reflection to associative rings: associators must also vanish. | 1 | refuted, refined |
| SZ1-037 | Normalized A_0-derivations R_0→M are A-derivations R→M_bottom; Ω^1_(R_0/A_0) is the ordinary Ω^1_(R/A) through ring reflection, and all projective-target derivations vanish. | 1 | proved |
| SZ1-038 | Zero adjunction is the fully faithful left adjoint to the unit additive-group-fiber functor on unital inverse semirings. | 1 | proved |
| SZ1-039 | R_0 is Noetherian, respectively has every ideal principal, exactly when R has that property. | 1 | proved |
| SZ1-040 | The cancellative multipliers of Z_0 are exactly the old nonzero integers; units and associates are the usual signs. | 1 | proved |
| SZ1-041 | The Pythagorean triples of Z_0 are ordinary integer triples, (a,tau,±a), (tau,b,±b), and (tau,tau,tau). | 1 | proved |
| SZ1-042 | With nonempty additively closed multiplication-absorbing ideals, A(B) has ideals {infinity} and J∪{infinity}, and Spec adds one generic open point. | 1 | proved |
| SZ1-043 | Modules over G_L(R) are R-module diagrams over L-semimodules, with proper-lattice scalars acting by fiber zeros. | 1 | proved |
| SZ1-044 | Finite projective modules over Id(C) are finite colored posets with exact greatest color truncations. | 1 | proved |
| SZ1-045 | Finite projective R-module diagrams on a finite poset are sums of principal-upset diagrams with canonical projective quotient labels. | 1 | proved |
| SZ1-046 | Finite projectives over G_Id(C)(R) are colored-poset data with projective R-labels on admissible order ideals, which can be nonprincipal. | 1 | proved |
| SZ1-047 | For nonempty C, V(G_Id(C)(R)) and K0 are free on data connected by comparabilities and nonzero admissible-label ideals. | 1 | proved |
| SZ1-048 | For nonempty C and nonzero R, strong projectives over G_Id(C)(R) are free; for zero R their monoid is N indexed by components of C. | 1 | proved |
| SZ1-049 | For commutative R, tensor product of labelled projectives uses P×Q and labels M_p tensor_R N_q, allowing zero labels; ordinary K_0(R_0) is the monoid ring of connected labelled posets. | 1 | proved; separate statement-first check completed |
| SZ1-050 | Pic(R_0) is naturally Pic(R); tensor invertibility forces finite projectivity and a one-point labelled support poset. | 1 | proved; separate statement-first check completed |
| SZ1-051 | At a chosen prime, sum rank^(-s) over positive-rank labels is an additive and multiplicative character for all complex s, with D_-1^+>=D_0^+ on actual projectives. | 1 | proved; separate statement-first check completed |
| SZ1-052 | For any inverse semiring (Q,F) and fixed Q-support L, the category of semimodules with identity support maps is equivalent to additive modules over the explicitly presented action ringoid A_L. | 1 | proved |
| SZ1-053 | Finite semimodule generation is equivalent to finite Q-generation of the support and finite A_L-generation of the amplitude functor. | 1 | proved |
| SZ1-054 | Finite projectivity is equivalent to support projectivity, A_L-amplitude projectivity, and vanishing of C_sigma for some section of a finite free support cover; for fixed sigma this is finite generator image membership. | 1 | proved |
| SZ1-055 | For nonzero R, the top-born R diagram over Boolean support B^2 has projective support and amplitude but has nonzero C_sigma for every support section and is not R_0-projective. | 1 | proved |
| SZ1-056 | Zero adjunction preserves arbitrary pullbacks of commutative unital rings: (A times_C B)_0 = A_0 times_{C_0} B_0. | 1 | proved |
| SZ1-057 | For finite Γ and any unital ring R, finite projective R_0[Γ]-semimodules are finite Γ-posets with finite projective R[Γ_p] stabilizer labels; zero labels allowed and no invertibility of \|Γ\| required. | 1 | proved |
| SZ1-058 | V(R_0[Γ]) is free commutative on decorated finite Γ-posets transitive on comparability components; K0 is free abelian on these actual labelled isomorphism classes. | 1 | proved |
| SZ1-059 | All finite strongly projective R_0[Γ]-semimodules are free, including zero R; SV=N and SK0=Z. | 1 | proved |
| SZ1-060 | The scalar-then-transition spans for admissible Q-linear functionals form a two-sided ideal J_L of the action ringoid. | 1 | proved |
| SZ1-061 | Finite projectivity over every inverse semiring is equivalent to projective Q-support, finite projective action-category amplitude, and J_LG=G. | 1 | proved |
| SZ1-062 | The canonical ideal condition equals vanishing of quotient extension of scalars and classifies finite projectives with identified support; support isomorphisms transport the data. | 1 | proved |
| SZ1-063 | The admitted amplitudes are images of finite representable idempotents with all entries in J_L, classified by rectangular intertwiners. | 1 | proved |
| SZ1-064 | For an entire idempotent Q, finite projectives over Q×_B R_0 are projective Q-supports L labelled by finite projective R-modules on J(B⊗_Q L). | 1 | proved |
| SZ1-065 | The canonical ideal J_L need not be idempotent, even for finite distributive entire support Q and finite free L=Q². | 1 | proved |
| SZ1-066 | Every two-sided ideal I of every unital ring R occurs as J_L with A_L=R at singleton projective support, so canonical ideal powers need not stabilize. | 1 | proved |
| SZ1-067 | For finite Q and L, greatest admissible functionals exist and their diagonal join identity exactly tests support projectivity, giving a Q^{\|L\|} retraction. | 1 | proved |
| SZ1-068 | For finite Q and L, each canonical ideal component is the image of the single group F(delta_l(k)) under its scalar-then-transition map. | 1 | proved |
| SZ1-069 | For finite inverse T and finite support L, scalar-then-transition normal forms make its action category a finite unital category ring. | 1 | proved |
| SZ1-070 | Finite projectives over every finite inverse semiring are finite support tables passing the greatest-functional test, labelled by multiplicities of simple-module projective covers on which the canonical ideal acts nontrivially. | 1 | proved |
| SZ1-071 | For every inverse semiring T=(Q,F) and every Q-support L, the action category has exact hom groups colim_{q l≤k}F(q), with multiplication induced by the coefficient product. | 1 | proved |
| SZ1-072 | The canonical support ideal is the image of the directed coefficient colimit over all admissible functionals; every element has one functional/coefficient representative. | 1 | proved |
| SZ1-073 | For finite Q and arbitrary L and F, action-category blocks are F(r(l,k)) and canonical ideal blocks are images from F(delta_l(k)); composition is explicit. | 1 | proved |
| SZ1-074 | The universal ring reflection is colim_Q F; group-valued T-semimodules are reflection-ring modules and are finite projective exactly when ordinary finite projective and generated by the image of F(0). | 1 | proved |
| SZ1-075 | Finite unital-ring presentations effectively yield inverse-semiring presentations R×B with a named cyclic singleton-support projective Tc that vanishes exactly when R=0. | 1 | proved |
| SZ1-076 | For a finitely presented nonunital algebra A over a finite field and named idempotent e, (k⊕A)⟨u,v⟩/(uv−1,vu−e) is zero iff e=0; if e≠0 its unitization embeds. | 1 | proved |
| SZ1-077 | Uniform zero and isomorphism testing for specified finite projectives over finitely presented inverse semirings is undecidable, even for Boolean support and one-by-one idempotents. | 1 | proved |
| SZ1-078 | A finite projective support frame parametrizes every admissible functional by finitely many scalar inequalities and computes the canonical coefficient ideal as an image over the resulting intrinsic scalar order ideal. | 1 | proved |
| SZ1-079 | For every finite projective support, its intrinsic scalar order ideal C is two-sided and satisfies C²=C; the associated coefficient ideal need not be idempotent. | 1 | proved |
| SZ1-080 | Ideal completion does not reflect ordinary projectivity even for a cyclic finitely presented module over the tropical integer semiring; its completed module is a rank-one complete-projective retract. | 1 | proved |
| SZ1-081 | When the support unit is greatest, the coefficient images in F(1) form an increasing diagram of two-sided ideals and a support-preserving inverse-semiring quotient. | 1 | proved |
| SZ1-082 | For an n×n idempotent support matrix over integral Q, the kernel in its coefficient ring fiber satisfies N_E^(n+1)=0, with no support-height or cardinality hypothesis. | 1 | proved |
| SZ1-083 | The integral-support image-ideal quotient induces a direct-sum-preserving bijection of finite-projective isomorphism classes and isomorphisms of V and K0. | 1 | proved |
| SZ1-084 | For integral support and nonzero local unit ring, finite projectives are classified by projective Q-supports and finite multiplicities on allowed mutual-W reachability classes, including infinite supports and coefficient groups. | 1 | proved |
| SZ1-085 | For every inverse-semiring pair, the context-test subgroups form the largest coefficient ideal vanishing on all fibers above the support unit; its quotient has no residual ideal of that kind. | 1 | proved |
| SZ1-086 | For arbitrary support and every n-by-n idempotent support matrix, the canonical quotient coefficient-ring kernel satisfies N_E^(n+1)=0. | 1 | proved |
| SZ1-087 | The canonical quotient for arbitrary support preserves finite-projective isomorphism classes, direct sums, V and K0; integral support recovers the image-ideal quotient. | 1 | proved |
| SZ1-088 | The canonical action ideal may be replaced by its largest idempotent subideal, obtained by transfinite squaring and limit intersections, without changing its finite-projective amplitudes or typed finite idempotent matrices. | 1 | proved |
| SZ1-089 | For arbitrary inverse-semiring support, the all-context tests into upper multiplicative-idempotent rings give the largest coefficient ideal vanishing there; its quotient has no residual ideal of that kind and strictly strengthens the upper-unit quotient. | 1 | proved |
| SZ1-090 | For the upper-idempotent coefficient quotient and every n-by-n idempotent support matrix, the additive matrix-fiber kernel satisfies N_E^(n+1)=0 even though the global coefficient ideal need not be nilpotent. | 1 | proved |
| SZ1-091 | The upper-idempotent quotient preserves finite-projective isomorphism classes, direct sums, V and K0; integral support recovers the image-ideal reduction. | 1 | proved |
| SZ1-092 | For arbitrary inverse-semiring support, all upper-idempotent context tests into ordinary Levitzki radicals define the largest compatible coefficient ideal locally nilpotent at those fibers; the quotient has no residual ideal of that kind and strictly extends zero detection. | 1 | proved |
| SZ1-093 | Every finite idempotent support matrix has a locally nilpotent coefficient kernel for the compatible Levitzki quotient; the unital enlargement E join I has a finite Peirce decomposition and the original-fiber transition kernel annihilates that fiber. | 1 | proved |
| SZ1-094 | Extension along the compatible Levitzki coefficient quotient preserves finite-projective isomorphism classes, direct sums, V and K0 at exact supports. | 1 | proved |
| SZ1-095 | The compatible Levitzki coefficient ideal commutes entrywise with all finite matrix constructions at every support, and its quotient commutes with matrices; upper-idempotent zero detection need not do so. | 1 | proved |
| SZ1-096 | At every upper multiplicative idempotent, the compatible locally nilpotent coefficient ideal is the intersection of upward-transition preimages of the ordinary Levitzki radicals. | 1 | proved |
| SZ1-097 | Every coefficient fiber of the compatible locally nilpotent ideal is the intersection of additive preimages of ordinary Levitzki radicals in explicit upper-idempotent two-by-two matrix fibers; finite Q gives at most \|Q\|^4 tests. | 1 | proved |
| SZ1-098 | If Q is finite and every upper-idempotent coefficient ring F(e) is semiperfect, finite-projective T-semimodules are classified by finite projective Q-supports and unique multiplicities of the simple-type projective covers of B_L on which I_L acts nontrivially, modulo support automorphisms. | 1 | proved |
| SZ1-099 | For the support chain bottom<1<u with nonbottom maximum product and constant field fibers, the regular-support category ring is lower triangular 3 by 3 and its canonical ideal selects exactly the middle simple; projectives at that support have fibers 0,K^n,K^n. | 1 | proved |
| SZ1-100 | For arbitrary Q with all upper coefficient rings local or zero, canonical-ideal-generated projective amplitudes are finite sums of allowed representables with unique multiplicities; each diagonal canonical ideal is either the whole local action ring or lies in its Jacobson radical. | 1 | proved |
| SZ1-101 | Local upper coefficient rings do not force local or semiperfect action endomorphism rings: the degree-filtered polynomial diagram over max-plus support has singleton action ring k[t] and zero canonical ideal. | 1 | proved |
| SZ1-102 | The compatible upper-Jacobson coefficient ideal is maximal, contains H, has a quotient with no such residual ideal, has radical fixed-support kernels and commutes with finite matrices. | 1 | proved |
| SZ1-103 | Reduction modulo the compatible Jacobson ideal lifts isomorphisms between existing finite projectives and injects V; under semiperfect upper coefficient rings it lifts exact-support projectors and induces V and K0 isomorphisms. | 1 | proved |
| SZ1-104 | For Z localized away from2and3, the compatible Jacobson quotient is F2 times F3 and the projective monoid map is the diagonal N to N², so unconditional projective-object lifting fails; the locally nilpotent ideal is zero. | 1 | proved |
| SZ1-105 | With arbitrary Q and semiperfect upper coefficient rings, all canonical-ideal-generated finite projective amplitudes have unique finite multiplicities on local idempotents in diagonal canonical ideals, modulo explicit inverse-arrow equivalence; semimodule classes also take support automorphism orbits. | 1 | proved |
| SZ1-106 | For the three-support field diagram with zero top fiber, the compatible Jacobson coefficient family is zero, the global Jacobson–Bourne radical is the whole semiring, and J_s is only the global zero; the coefficient union is nonsubtractive and the coefficient/Bourne quotients differ. | 1 | proved |
| SZ1-107 | Any finite family of canonical-ideal-generated finite projective amplitudes over arbitrary(Q,F) has simultaneous exact corners in one ordinary coefficient matrix ring; its finite-source ideal N satisfies(ker pi)N=0, and all mixed-corner morphisms are isomorphically modeled. | 1 | proved |
| SZ1-108 | The compatible Jacobson coefficient ideal is the intersection of upward ordinary-ring Jacobson tests on upper fibers and, at every support, of explicit2by2upper-fiber tests; finite Q gives at most\|Q\|^4terms. | 1 | proved |
| SZ1-109 | One inverse semiring with semisimple upper coefficient rings has infinitely many pairwise nonisomorphic projective amplitudes on the free support Q, each with endomorphism field k, such that every fixed finite set of action objects fails to detect some nonzero amplitude. | 1 | proved |
| SZ1-110 | If every upper coefficient ring is exchange, every finite idempotent over any compatible coefficient quotient lifts inside its exact original support fiber, including nonunital matrix fibers and nonzero bottom coefficients. | 1 | proved |
| SZ1-111 | Under exchange upper coefficient rings every compatible coefficient quotient surjects on finite-projective classes and K0; the compatible Jacobson quotient induces isomorphisms on V and K0, with no claim of injectivity for arbitrary coefficient ideals. | 1 | proved |
| SZ1-112 | For arbitrary(T,L), one small category C_L of coefficient fibers and its explicit ideal N_L model the entire category of canonical-ideal-generated finite projective amplitudes, with all morphisms and support-automorphism actions; C_L/N_L is diagonal. | 1 | proved |
| SZ1-C01-003 | The universal ring reflection R_0→R has no unital zero-preserving section. | 1 | proved |
| SZ1-C01-006 | For a nonzero ring R there is no unital semiring map B→R_0. | 1 | proved |
| SZ1-C01-010 | For a UFD with infinitely many irreducible classes the multiplicative monoid spectrum of R_0 has infinite dimension. | 1 | proved |
| SZ1-C01-011 | For a domain R, the ordinary contracted integral monoid ring of R_0 is Z×Z[R_nonzero]. | 1 | proved |
| SZ1-C01-019 | The support functor is left and right adjoint to Boolean restriction, and the least group fiber is right adjoint to ring restriction. | 1 | proved |
| SZ1-C01-021 | Subsemimodules are compatible module subdiagrams on zero join-subsemilattices. | 1 | proved |
| SZ1-C01-022 | A finite generating set generates the support semilattice and each fiber by transporting its generators with smaller support. | 1 | proved |
| SZ1-C01-024 | The source norm formula needs an explicit multiplicativity hypothesis, though the shifted weight N+1 is nonmultiplicative. | 1 | refuted, refined under multiplicative-norm hypothesis |
| SZ1-C01-025 | The ordinary and shifted finite-quotient norm series have the same abscissa of absolute convergence. | 2 | proved |
| SZ1-C01-026 | Units and old nonzero irreducibles of a zero-adjoined domain are their ordinary counterparts. | 1 | proved |
| SZ1-C01-027 | The old zero of a zero-adjoined domain is reducible and divisibility-prime. | 1 | proved |
| SZ1-C01-028 | A finite nonnegative multiplicative ideal norm extending a nonconstant ordinary norm vanishes on both absorbing zero ideals. | 1 | proved |
| SZ1-C01-032 | Subtracting N Taylor terms leaves a function holomorphic on Re(s)>sigma_a−N. | 2 | proved |
| SZ1-C01-033 | A unique simple pole at1 of the original Dirichlet series remains the unique pole of the shifted family with unchanged residue. | 2 | proved |
| SZ1-C01-037 | The first two logarithmic jets of the quotient-counting shift have explicit arithmetic-kernel expansions. | 2 | proved |
| SZ1-C01-040 | The source Bernoulli defect formula fails at m=0 under the standard convention; subtracting B_(m+1)(1) is the correct form. | 2 | refuted, refined as SZ1-C01-051 |
| SZ1-C01-051 | For the Hurwitz defect D_t=zeta−zeta(.,1+t), D_t(−m)=[B_(m+1)(1+t)−B_(m+1)(1)]/(m+1), in particular D_t(0)=t. | 2 | proved from classical formula |
| SZ1-C02-040 | Encoding the finite witness count by a positive old integer or the new zero makes its support exactly the shell-solvability indicator. | 5 | proved |
| SZ1-C15-063 | The source final synthesis overstates the completeness of support, valuation and leading coefficient; these determine only the initial graded term, not the full element. | 5 | refuted, refined as SZ1-C15-064 |
| SZ1-C15-064 | Support, valuation and leading coefficient specify the associated-graded initial term, with distinct absent and exact-zero states, while higher coefficients remain undetermined. | 5 | proved |
| SZ1-C16-013 | The inverse image of zero under the universal ring reflection is exactly the set killed by every ring-valued homomorphism. | 1 | proved |
| SZ1-C16-015 | The coordinate ring reflection of a finite product (R_0)^I is R^I, with Boolean cube of idempotent masks as zero fiber. | 1 | proved |
| SZ1-C16-019 | Localization of a finite semiring product at one tuple is the product of its coordinate localizations. | 1 | proved |
| SZ1-C16-020 | For a finite power of a zero-adjoined field, localization at a tuple leaves unit coordinates unchanged, turns old-zero coordinates Boolean, and deletes new-zero coordinates. | 1 | proved |
| SZ1-C16-021 | Identifying an old-zero mask with a tuple of nonzero field amplitudes on the same finite face Booleanizes exactly that face. | 1 | proved |
| SZ1-C16-022 | Old zero and nonzero amplitudes have equal support, while imposing their equality yields the indicated full or facewise Boolean quotient. | 1 | proved |
| SZ1-C16-038 | The claimed three-stage F1-to-lattice-to-Boolean arrow is interpretive until the category and first map are specified. | 1 | not a precise statement |
| SZ1-C16-042 | In a lattice-supported nonassociative algebra, associators are amplitude associators and multiplicative identities with matching variables pass through the support coordinate. | 1 | proved |
| SZ1-C16-045 | Cayley–Dickson zero divisors, interpreted as nonzero amplitudes, first occur at the sedenion stage and persist in later stages; support adjunction records their products as old zero. | 1 | conditional on standard Cayley–Dickson facts; nonassociative framework |
| SZ1-C16-049 | The contracted monoid semiring of the multiplicative monoid of R_0, modulo ring-addition relations, recovers R_0. | 1 | proved |
| SZ1-C16-050 | Extension of ring ideals to R_0 preserves their ideal products. | 1 | proved |
| SZ1-C16-051 | For a Dedekind domain, supported fractional-ideal classes and ordinary quotient-norm counting recover its classical ideal class group and Dedekind zeta function. | 5 | proved |
| SZ1-C16-052 | The occupied quotient cardinality N(J)+1 is not a multiplicative ideal weight. | 2 | proved |
| SZ1-C16-053 | The shifted quotient-counting series has no normalized ordinary ideal Euler product; over Z it is zeta(s)−1. | 2 | proved |
| SZ1-C16-055 | A vector over a zero-adjoined field is unimodular exactly when one amplitude is nonzero. | 5 | proved |
| SZ1-C16-056 | Unimodular vectors modulo scalar units split by nonempty occupied subsets into ordinary projective spaces on those subsets. | 5 | proved |
| SZ1-C16-057 | For G_L(K), each nonempty top-support subset contributes an ordinary projective space and arbitrary proper-lattice decorations on the other coordinates. | 5 | proved |
| SZ1-C16-058 | The unimodular-vector orbit set maps to ordinary projective space by ring reflection and to Boolean support profiles by the support map. | 5 | proved |
| SZ1-C16-059 | The projective line distinguishes old-zero and new-zero versions of both zero and infinity, despite their identical ordinary amplitudes. | 5 | proved |
| SZ1-C16-060 | For finite L of size ell, the orbit count is ((q+ell−1)^N−ell^N)/(q−1), with the stated polynomial coefficients and resulting finite point-counting Euler factors. | 5 | proved |
| SZ1-C16-061 | For R=F_q, the unimodular-vector orbit count in length N is ((q+1)^N−2^N)/(q−1). | 5 | proved |
| SZ1-C16-062 | The Boolean-support point-count polynomial gives the finite zeta product with exponents equal to binomial tail sums. | 5 | proved |
| SZ1-C16-063 | Every invertible matrix over B is a permutation matrix. | 5 | proved |
| SZ1-C16-064 | For a nonzero field K and any bounded distributive L, every invertible G_L(K)-matrix is monomial; the same argument works for every nonzero commutative ring. | 5 | proved |
| SZ1-C16-065 | The general linear group of R_0 is the monomial group (R^×)^n semidirect S_n. | 5 | proved |
| SZ1-C16-066 | Quotienting the monomial group by central scalar units gives the stated projective linear group, acting in rank2 by scaling and inversion. | 5 | proved |
| SZ1-C16-067 | A nonzero translation, and more generally a nonmonomial Mobius matrix, does not give a global invertible split matrix on all support profiles. | 5 | proved |
| SZ1-C16-068 | The signed Leibniz determinant over G_L(K) has ordinary determinant amplitude and lattice-permanent support; that support is a join of matching levels, not necessarily an attained matching level. | 5 | proved |
| SZ1-C16-069 | Lattice-valued characteristic coefficients have supports given by joins of principal cycle-cover levels, with the same nonattainment qualification. | 5 | proved |
| SZ1-C16-070 | For R_0, the determinant distinguishes absent matching, occupied cancellation, and nonzero determinant amplitude. | 5 | proved |
| SZ1-C16-071 | Split characteristic coefficients have classical amplitudes and Boolean cycle-cover support, and are invariant under monomial conjugation. | 5 | proved |
| SZ1-C16-072 | A trace word has the classical trace amplitude and Boolean existence of a closed walk with the prescribed edge colors, and is invariant under monomial simultaneous conjugation. | 5 | proved |
| SZ1-C16-074 | Inclusion of the monomial normalizer induces a character-variety morphism whose trace pullbacks are cycle sums, with an additional Boolean closed-walk datum for split representations. | 5 | conditional on invariant-theory framework |
| SZ1-C16-075 | Monomial matrices over G_L(K) are conjugate precisely when their permutation cycles have matching lengths and cycle-product weights. | 5 | proved |
| SZ1-C16-079 | The block-replication embedding A→A tensor I_q raises split characteristic polynomials and determinants to the qth power and multiplies trace powers by q. | 5 | proved |
| SZ1-C16-080 | For a surjection A→k, fibers of its zero-adjoined map are the ordinary residue cosets, while the new-zero fiber is a singleton. | 1 | proved |
| SZ1-C16-081 | The old-zero fiber is the kernel ideal with its zero center, while the new zero remains a separate absent point. | 1 | proved |
| SZ1-C16-082 | The inverse image of a residue support star is a disjoint family of residue cosets and kernel-ideal factors indexed by activated absent coordinates. | 1 | proved |
| SZ1-C16-083 | Modulo the square of the kernel, each fixed support-activation stratum is a torsor under a product of the kernel cotangent vector space m/m². | 1 | proved |
| SZ1-C16-084 | Zero adjunction commutes with the inverse limit of the adic quotient tower because compatible tuples have constant occupied support. | 1 | proved |
| SZ1-C16-085 | For the hyperreal standard-part quotient, the zero-adjoined residue fibers and their support-star strata are the corresponding ordinary infinitesimal cosets. | 5 | conditional on standard-part datum |
| SZ1-C16-089 | The zero-adjoined surcomplex standard-part quotient has fibers c+m and the corresponding support-activation strata. | 5 | conditional on class-sized coefficient framework |
| SZ1-C16-095 | In a two-coordinate zero-adjoined surcomplex product, inverting a nonzero first coordinate and the old zero in the second yields S×B. | 5 | conditional on class-sized coefficient framework |
| SZ1-C16-096 | Identifying the old zero with any nonzero surreal amplitude yields B, or the corresponding facewise Boolean quotient. | 5 | conditional on class-sized coefficient framework |
| SZ1-C16-097 | If a normalized differential-field derivation has partial(omega)=1, then partial(omega^-1) is nonzero, so it cannot be identified compatibly with the derivationally constant old zero. | 5 | conditional on stated differential-field normalization |
| SZ1-C16-098 | The coordinate-swap matrix is a global involution exchanging the two zero points with their corresponding infinity points. | 5 | proved |
| SZ1-C16-099 | Coordinate inversion bijects the support-star residue neighborhoods of zero and infinity; nonzero kernel elements become reciprocals after the required field base extension. | 5 | proved |
| SZ1-C16-100 | The two projective infinity points are distinct unimodular-vector orbits, and inversion carries punctured valuation-zero neighborhoods to their reciprocal neighborhoods. | 5 | proved after fixing the valuation-neighborhood convention |
| SZ1-C16-102 | The Cayley transform is valid on the ordinary full-support stratum but its nonmonomial matrix does not extend to an invertible split matrix. | 5 | proved |
| SZ1-C16-103 | The classical transformation x/(omega−x) has a nonmonomial matrix and thus no global split-linear extension. | 5 | proved |
| SZ1-C16-104 | The projective map x↦[1:x] extends ordinary inversion and sends old and new zeros to the distinct infinity points. | 5 | proved |
| SZ1-C16-105 | Cancellation of a common polynomial factor extends the corresponding rational projective map near the specified point, while the uncancelled old-zero pair remains non-unimodular and distinct from the absent pair. | 5 | proved |
| SZ1-C16-106 | The claimed two-condition split-limit theorem lacks a fixed topology or limit definition; the residue/support tests alone are not a defined convergence theorem. | 5 | not a precise statement |
| SZ1-C16-109 | In a chosen univalent or classifying-space completion, the inversion isomorphism gives a path; this does not make distinct scalar elements equal. | 5 | conditional on specified completion/category |
| SZ1-C16-111 | The map Spec Z_0→Spec Z that identifies the new generic point with the old generic point is continuous. | 1 | proved |
| SZ1-C16-112 | Conditional on the absolute-site point package, the prescribed map of point classes separates the trivial ordered group from Z above their common Picard image. | 5 | conditional on unverified primary point package |
| SZ1-C16-113 | The displayed group inclusions give the corresponding spherical-stalk chain, whose final term is perfect for pth Frobenius. | 5 | conditional on unverified primary stalk package |
| SZ1-C16-115 | Conditional on that package, the arithmetic Jacobian is Pic_f×B as a multiplicative monoid, and its idempotents form the Boolean configuration lattice with the second coordinate reversed. | 5 | conditional on unverified primary Jacobian package |
| SZ1-C16-116 | Positivity gives a semiring map from nonnegative reals to B, and the nondegeneracy of a one-dimensional seminorm is generator-independent and multiplicative under tensor product. | 5 | elementary assertion proved; Jacobian identification conditional |
| SZ1-C16-117 | Conditional on the stated Abel–Jacobi package, its idempotent images are the empty configuration and the singleton finite or archimedean configurations. | 5 | conditional on unverified primary Abel–Jacobi package |
| SZ1-C16-118 | Collapsing the absorbing ideal M×{0} of M×B gives the multiplicative monoid M with one new absorber. | 5 | proved |
| SZ1-C16-119 | Integration of principal logarithms over measurable supports defines a Boolean-lattice valuation whose zero supports are exactly the proper restricted adelic curves. | 5 | proved |
| SZ1-C16-120 | The adelic defect transform is a linear map from L∞ to characters of K×, evaluates on characteristic functions as the support defect, and identifies its quotient by the kernel with its image. | 5 | proved |
| SZ1-C16-121 | The quotient of L∞ by the defect kernel pairs nondegenerately with the real span of the principal logarithms in L1. | 5 | proved |
| SZ1-C16-122 | A boundedly weighted logarithmic height changes under scalar rescaling by its defect character and descends to projective space precisely when that character vanishes. | 5 | proved |
| SZ1-C16-123 | When norm logarithms are integrable, the weighted logarithmic degree changes under scaling by minus the defect character and descends exactly when it vanishes. | 5 | proved |
| SZ1-C16-124 | A measure-preserving refinement preserving local absolute values commutes with the defect transform and pulls back balanced supports. | 5 | proved |
| SZ1-C16-126 | The support localization is the measure algebra of the restricted adelic family, which is proper exactly when the selected logarithmic height descends. | 5 | proved |
| SZ1-C16-128 | For a global field, a real weighting of normalized principal logarithms vanishes on every nonzero field element exactly when all weights are constant; balanced supports are therefore empty or full. | 5 | proved |
| SZ1-C16-130 | Adjoining an arbitrary measured family of trivial absolute values leaves principal logarithms and ordinary heights unchanged and adds a full neutral factor to the support lattice and defect kernel. | 5 | proved for specified norm-integrability framework |
| SZ1-C16-131 | After adjoining trivial places to Q, balanced supports are exactly an empty or full ordinary place set together with an arbitrary support in the added family. | 5 | proved |
| SZ1-C16-133 | Booleanizing any field absolute value tests only whether the scalar is zero, so it does not distinguish places and separates trivial absolute values from zero seminorms. | 5 | proved |
| SZ1-C16-134 | Presence and metric nondegeneracy identify the three local line states with the incidence sublattice {(s,d):d≤s} of B², and tensor product is meet. | 5 | proved |
| SZ1-C16-135 | Measurable three-state line data modulo null sets are incident pairs of measurable support classes, with a distributive-lattice defect valuation on the nondegenerate component. | 5 | proved |
| SZ1-C16-173 | Adjoining a new point to a vector space functorially distinguishes a supplied vector of value zero from absence of a vector. | 5 | functorial statement proved; anomaly application conditional |
| SZ1-C16-177 | The identity GL_n(C_0)=monomial group identifies the specified split local systems with pushforwards of rank-one local systems on finite covers. | 5 | proved in specified local-system framework |
| SZ1-C16-180 | For arbitrary matrix Higgs fields on monomially reduced bundles, split characteristic coefficients glue and refine ordinary Hitchin coefficients by cycle-cover support. | 5 | proved for explicitly defined matrix Higgs data; principal-normalizer interpretation corrected |
| SZ1-C16-181 | Conditional on the imported Langlands functor and specified spectral-stack map, pullback defines the stated monomial restriction functor. | 5 | conditional on imported functor and spectral-stack framework |
| SZ1-C16-192 | Adding two fixed points to a simply transitive W-torsor gives action groupoid BW disjoint union BW disjoint union a point. | 5 | proved |
| SZ1-C16-193 | The product of two such split torsors has nine coarse states and the indicated Boolean support square, conditional on the external torsor realization. | 5 | proved conditional on external torsor realization |
| SZ1-C16-194 | Finite products of the split torsors have the stated Boolean support cubes and product action groupoids. | 5 | proved conditional on external torsor realization |
| SZ1-C16-195 | Internal zero adjunction on semiring objects of a topos is functorial, has amplitude and support morphisms, and commutes with inverse-image functors. | 5 | proved |
| SZ1-C16-196 | Sections of the sheaf coproduct adjoining zero are pairs of a clopen support V⊆U and an old section on V; on nonempty connected U they are A(U)_0. | 5 | proved |
| SZ1-C16-197 | Universal Frobenius maps extend across internal zero adjunction and preserve support; the old-zero and new-zero stalk localizations are B and the terminal semiring. | 5 | structural statement proved; literal stalk integer labels refined |
| SZ1-C16-198 | The same internal construction separates absent, old-zero and other tropical profile germs on the scaling site, with old-zero localization retaining only support. | 5 | proved for the stated semiring sheaf |
| SZ1-C16-199 | The final synthesis combines earlier precise results and conditional interfaces, but its universal measure-algebra completeness assertion is false without additional measure hypotheses. | 5 | refuted in part; refined and conditional component statements |
| SZ2-PKT-001 | The zero-adjoined ring has the supported coordinate model (r,1), with one unsupported zero, and its unital Boolean character is the support projection. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-002 | Products of rings give the Boolean fibre product after zero adjunction, but the displayed ordinary monoid-semiring presentation omits the necessary relation [tau]=0. | 2 | original presentation refuted; contracted presentation independently proved |
| SZ2-PKT-003 | The old-zero scalar projects a semimodule onto its additive idempotents, which form a join semilattice. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-004 | Each support fibre is an R-module, and addition of a larger support element gives the transition homomorphism. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-006 | Cancellative semimodules reduce to R-modules; a free module has a Boolean support skeleton with fibre R^I. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-007 | The ideals are the new-zero ideal together with the lifted ordinary ring ideals, with the expected product. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-008 | Divisibility by the supported zero detects the two zero elements; the corresponding prime condition is the domain condition. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-009 | Differentiating a shifted Dirichlet series raises its argument and multiplies by a rising factorial; the resulting translation expansion converges for shift modulus below one. | 2 | independently proved; see packet intake note |
| SZ2-PKT-010 | Logarithmic derivatives of the shifted series are the usual universal polynomials in its normalized derivatives. | 2 | independently proved; see packet intake note |
| SZ2-PKT-011 | A positive nonintegral shift has a first exponential scale that is not an integer, so it cannot be an ordinary absolutely convergent Dirichlet series; the unit-deleted endpoint has no normalized Euler product. | 2 | independently proved; see packet intake note |
| SZ2-PKT-012 | Endpoint residues identify the two coordinate supports with the principal-part subspaces; the inverse residue matrix and support fibres are explicit. | 2 | independently proved; see packet intake note |
| SZ2-PKT-013 | Deleting the integer one creates a coprime multiplicative defect exactly on pairs with one coordinate equal to one; its double Dirichlet series and the interior kernel follow by subtraction. | 2 | independently proved; see packet intake note |
| SZ2-PKT-014 | For a number field, the norm-shifted ideal series has an entire correction to the Dedekind zeta function for shift modulus below one, hence the same sole pole and residue. | 2 | independently proved; see packet intake note |
| SZ2-PKT-016 | A positive nonintegral norm shift cannot be an ordinary integer-base Dirichlet series, since the unit ideal supplies the nonintegral smallest base. | 2 | independently proved; see packet intake note |
| SZ2-PKT-017 | The two zeros form a Boolean algebra with the supported zero as its internal multiplicative unit; its inclusion in the ambient semiring is generally nonunital. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-018 | The units remain the original ring units, and multiplication by u fixes the new zero together with the annihilator of u−1. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-019 | Over a domain, a nonidentity unit fixes exactly the two zero elements. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-020 | At a zeta zero, the scalar zeta(s)−1 equals −1 and has the Boolean fixed pair; this pointwise construction alone does not record multiplicity. | 2 | independently proved; see packet intake note |
| SZ2-PKT-021 | On a closed discrete support, arbitrary coordinate products form a sheaf with the prescribed stalks and terminal stalks elsewhere. | 2 | independently proved; see packet intake note |
| SZ2-PKT-022 | The finite-support presheaf on a closed discrete divisor sheafifies to the product of its skyscraper fibres. | 2 | independently proved; see packet intake note |
| SZ2-PKT-023 | The divisor support sheaf has a Boolean cube at each zero and the reduced support sheaf has one Boolean factor there. | 2 | independently proved; see packet intake note |
| SZ2-PKT-024 | The free rank-m Boolean semimodule is the power set of m coordinates, with union as addition. | 2 | independently proved; see packet intake note |
| SZ2-PKT-025 | Coordinate join and the diagonal split the Boolean cube onto its reduced Boolean factor. | 2 | independently proved; see packet intake note |
| SZ2-PKT-026 | The Boolean stalk cardinality recovers the divisor multiplicity; the reduced and multiplicity sheaves agree exactly for a reduced divisor. | 2 | independently proved; see packet intake note |
| SZ2-PKT-027 | Adding effective divisors concatenates Boolean coordinates and gives the product of their divisor sheaves. | 2 | independently proved; see packet intake note |
| SZ2-PKT-028 | The reduced Boolean support sheaf is the coordinatewise fixed sheaf for the scalar −1 on the zero-adjoined coefficient fibres. | 2 | independently proved; see packet intake note |
| SZ2-PKT-029 | A holomorphic germ of multiplicity m generates the same local ideal as the mth power of a local parameter. | 2 | independently proved; see packet intake note |
| SZ2-PKT-030 | The ideals of the length-m truncated polynomial ring are exactly the powers of its parameter, forming a chain of m+1 elements. | 2 | independently proved; see packet intake note |
| SZ2-PKT-031 | Taking the least terminal segment containing a subset and the largest terminal segment it contains gives the two order adjoints to the chain inclusion. | 2 | independently proved; see packet intake note |
| SZ2-PKT-032 | The Artin ideal chain embeds in the Boolean cube with explicit upper and lower adjoints and finite fibres. | 2 | independently proved; see packet intake note |
| SZ2-PKT-033 | Except in the smallest multiplicities, the Artin ideal chain and Boolean cube have different cardinalities and are not isomorphic. | 2 | independently proved; see packet intake note |
| SZ2-PKT-034 | The coordinate chain and Boolean constructions form sheaves of posets with finite stalks; their sections need not be finite posets. | 2 | finite-stalk formulation independently proved; literal finite-sections wording corrected |
| SZ2-PKT-035 | The chain inclusion and its two adjoints extend coordinatewise to sheaves of posets; finiteness applies to stalks rather than all section objects. | 2 | correctly typed sheaf statement independently proved |
| SZ2-PKT-036 | Products of truncated polynomial rings form the Artin divisor sheaf with the expected local quotient algebra stalks. | 2 | independently proved; see packet intake note |
| SZ2-PKT-037 | Coefficient support gives a pointed retraction from truncated jets to the Boolean cube, with nonempty fibres products of multiplicative groups; cancellation prevents additivity. | 2 | independently proved; see packet intake note |
| SZ2-PKT-038 | A nonzero additive group of jets cannot be isomorphic as an additive monoid to an idempotent Boolean cube. | 2 | independently proved; see packet intake note |
| SZ2-PKT-039 | Dividing a derivative-enhanced jet by the selected parameter takes its terminal line to the socle of the ordinary Artin quotient. | 2 | independently proved; see packet intake note |
| SZ2-PKT-040 | A germ vanishing to exact order m has a nonzero terminal Taylor class, and its shifted class generates the Artin socle. | 2 | independently proved; see packet intake note |
| SZ2-PKT-041 | The divisor of zeta supplies a product Boolean sheaf and a coordinatewise leading-jet section whose occupied slot records the zero multiplicity. | 2 | independently proved; see packet intake note |
| SZ2-PKT-042 | The finite-support rule on neighborhoods of infinity, combined with unrestricted products away from infinity, satisfies the sheaf axiom. | 2 | independently proved; see packet intake note |
| SZ2-PKT-045 | The unrestricted product sheaf and the skyscraper tail quotient are flasque because their restrictions are coordinate projections or identity maps. | 2 | independently proved; see packet intake note |
| SZ2-PKT-046 | The Boolean compactification stalk is the pointed product modulo eventual equality. | 2 | independently proved; see packet intake note |
| SZ2-PKT-047 | The vector tail exact sequence specializes to the Artin divisor fibres, giving the product/direct-sum quotient at infinity. | 2 | independently proved; see packet intake note |
| SZ2-PKT-048 | The infinite zero divisor gives nonzero Boolean and leading-jet tail classes. | 2 | independently proved; see packet intake note |
| SZ2-PKT-049 | Coordinate transport along base symmetries defines equivariance over those homeomorphisms and satisfies the cocycle equations. | 2 | independently proved; see packet intake note |
| SZ2-PKT-050 | The claimed symmetry maps must be interpreted as sheaf equivariance over the corresponding homeomorphisms, not as endomorphisms over the identity base. | 2 | base-map distinction independently checked |
| SZ2-PKT-052 | Boolean polynomial-algebra points realize the Boolean cube; substitutions for diagonal and join compose to the identity because addition is idempotent. | 2 | independently proved; see packet intake note |
| SZ2-PKT-053 | Adjoining a basepoint to the unit circle gives a pointed phase decoration that splits onto Boolean support; a simple derivative supplies its phase section. | 2 | independently proved; see packet intake note |
| SZ2-PKT-091 | The integer zero-adjoined semiring embeds in the complex one and identifies their two-element fixed pairs, with the same unital-inclusion qualification. | 1 | duplicate of foundation material; not rechecked here |
| SZ2-PKT-115 | A bijection of the correctly restricted packet sets transports the corresponding product Boolean sheaves by reindexing; it asserts no new operator-theoretic equivalence. | 2 | independently proved; see packet intake note |
| SZ2-lem-rouche | The explicit uniform Rouche inequality controls one simple zero throughout each parameter slab and, with nested endpoint discs, certifies continuous joined branches. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-bernoulli-endpoint | The entire quotient-sheet defect has the stated Bernoulli-polynomial values and logarithmic-Gamma derivative, including the corrected endpoint value D_t(0)=t. | 2 | proved; independent check and proof exposure recorded separately |
| SZ2-prop-clt-not-modulo | A normalized Gaussian central limit theorem and bounded perturbation control alone do not imply modulo-two equidistribution, as explicit rounded-normal counterexamples show. | 2 | proved; proof exposure and independent check recorded separately |
| SZ2-prop-dedekind-all-shifts | For every fixed nonnegative shift the Dedekind ideal series differs from the Dedekind zeta by an entire function, so the two-family congruence series has residue twice the Dedekind residue. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-degree | A specified sum of rank-one arithmetic characters has degree-one local Euler factors, while coefficient-field rationality alone neither supplies that realization nor bounds its degree. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-deitmar | The contracted new-zero monoid algebra of the integers is Z times Z[C2][x_p], preventing a finite-type Deitmar zeta for the full monoid and giving the stated finite-generator approximation instead. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-fibers | At an occupied signed coefficient c, effective dimensions are \|c\|+2r with r>=0 for c nonzero and 2r with r>=1 for c zero, while absent weights have zero dimension. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-fusion-pair | A finite group's fusion rules define the stated idempotent support semiring and lax monoidal group diagram, whose effective parity refinement is surjective and whose realized local degrees are representation dimensions. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-monoid-spectrum | The prime ideals of the pointed multiplicative monoid of Z0 are the new-zero singleton and the ideals indexed by arbitrary subsets of rational primes, giving infinite dimension and non-Noetherianity. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-packet-jet-support | The coefficient-support map on truncated jets is a retraction of pointed sets but is not additive, and coordinate division identifies the last jet line with the socle of the truncated local algebra. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-packet-stabilizer | The invariant pushforward of a product sheaf on a discrete finite-group orbit space has each fibre equal to the corresponding stabilizer invariants, with diagonal fibres in the permutation-only case. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-packet-tail-exact | For the product vector-space sheaf on a closed discrete subset of the complex line, extension by zero fits the stated tail exact sequence and has vanishing positive cohomology. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-quotient-apoint-bound | The exact supremum of zero real parts for the weighted quotient series is determined by zeta(2 sigma)/zeta(sigma)=u/(1+u), while the separated sheet uses zeta(sigma)=(2^sigma+1)/(2^sigma−1). | 2 | proved as a direct application of the cited theorems; source approximation1.78 for the separated sheet corrected |
| SZ2-prop-quotient-log-jets | The first two parameter logarithmic derivatives of the shifted quotient-zeta path are the stated expressions in the multiplicative Dirichlet coefficients of zeta(s+r)/zeta(s). | 2 | proved; independent check and proof exposure recorded separately |
| SZ2-prop-quotient-shift-remainder | For a coefficient series of finite absolute-convergence abscissa, nonnegative quotient-cardinality shifts preserve that abscissa, admit the stated holomorphic Taylor remainders, and differ by an entire function when the unshifted series has only a simple pole at one. | 2 | proved; independent check and proof exposure recorded separately |
| SZ2-prop-rescaled-hurwitz | For Re(a)>0, the Hurwitz zeta is an exponential prefactor times an absolutely convergent ordinary Dirichlet series with first coefficient1 exactly when a is the reciprocal of a positive integer. | 2 | proved; guided check versus statement-only residue derivation distinguished |
| SZ2-prop-shift | The shifted quotient series zeta(s,1+t) satisfies the stated Taylor expansion and parameter derivative, has constant residue one, and has no absolutely convergent integer-frequency Dirichlet representation for 0<t<1. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-smash | Support fibre products and pointed smash products multiply reduced cardinalities, so the ordinary product of shifted counts is not their cardinality rule. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-tail | At infinity the direct-image stalk of the product sheaf on a closed discrete set is the tail of sequences modulo finite agreement, while extension by zero has the trivial stalk. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-zero-ode | A simple shifted-zeta zero has a unique local holomorphic continuation with velocity rho*zeta(rho+1,1+t)/partial_s zeta(rho,1+t), without a forced critical-line constraint. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-prop-zero-phase | The initial velocity of a simple Hurwitz-sheet zero has the stated exact Hardy-phase expression, including its arctangent correction, and modulo-two phase equidistribution implies a half-share of right-movers. | 2 | proved; proof exposure and independent check recorded separately |
| SZ2-prop-zero-tangency-residue | For a real symmetric deformation at a simple critical-line zero, initial horizontal velocity is the negative residue of the antisymmetric deformation quotient, with the displayed positive-residue Hurwitz specialization. | 2 | proved; guided check versus statement-only residue derivation distinguished |
| SZ2-thm-divisor | The finite-support divisor presheaf on a closed discrete zero set sheafifies to the product of Boolean multiplicity fibres, whose reduction is a retract and is an isomorphism exactly at simple zeros. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-thm-paths-main | Five explicitly specified zeros of zeta(s) continue as distinct simple zeros of zeta(s,1+t) for every t in [0,1], with certified endpoint discs and two endpoints strictly to the right of Re(s)=1. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-thm-quotient-main | Finite kernel-congruence quotients of the zero-adjoined integers have cardinality series 2*zeta(s)-1, and weighting the kept-zero family by u gives (1+u)*zeta(s)-u with the stated a-point interpretation. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-thm-sign-main | The effective sign-Tate semiring surjects onto the zero-adjoined Laurent semiring by recording occupied support and signed trace, while effective Euler products and dimension unimodality do not descend but trace properties do. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ2-thm-witt-main | The signed local big-Witt products at odd primes give an injective semiring homomorphism with the prime-2 factor omitted, whereas including that ramified sign factor breaks multiplicativity. | 2 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ3-001 | R0 is the zero-adjoined inverse semiring of FGJM Definition 3.6; its semimodules have inverse additive monoids. | 1 | background |
| SZ3-002 | For a nonzero ring the new-zero singleton is prime, and adjoining the old zero gives a prime when R is a domain. | 1 | referred to Paper1 |
| SZ3-003 | The negative augmentation of a free rank-r lattice has kernel A_(r−1), with partial-sum basis coordinates. | 3 | proved |
| SZ3-004 | Characteristic-vector linearization sends a finite support J to a vector of negative augmentation −\|J\|. | 3 | proved with scope qualification |
| SZ3-005 | The quotient Qp/Zp× is the positive-end compactification Z∪{∞} via valuation. | 3 | proved |
| SZ3-006 | The diagonal Z-action on (Z∪{∞})×R is free proper and has the circle-plus-spiral quotient. | 3 | proved |
| SZ3-007 | The finite local boundary unit maps to −1 in increasing logarithmic orientation. | 3 | independently re-proved |
| SZ3-008 | The reflection crossed product is a half-line matrix algebra with diagonal endpoint; each character has boundary −1. | 3 | independently re-proved |
| SZ3-009 | The formal balancing row is the codiagonal of the local boundary rows, retaining both real labels. | 3 | proved |
| SZ3-010 | Fixed orthogonal multiplier isometries construct a stable balancing extension with negative-sum boundary and K0=Z^(n+1), K1=Z^n. | 3 | independently re-proved |
| SZ3-011 | The generic semilocal stratum has free proper action with quotient K_P×R. | 3 | independently re-proved |
| SZ3-012 | Each finite edge is proper with boundary the mapping torus of p on Yp and explicit cross-stratum convergence. | 3 | independently re-proved |
| SZ3-013 | The real edge is T_P×R and its boundary T_P is the free sign quotient of K_P. | 3 | independently re-proved |
| SZ3-014 | The action on the union of all one-zero edges is nonproper. | 3 | independently re-proved |
| SZ3-015 | The natural one-zero algebra has an exact generic-boundary crossed-product extension. | 3 | independently re-proved |
| SZ3-016 | Finite boundary K-groups are rotation invariants and coinvariants; the real boundary contributes sign-even functions. | 3 | independently re-proved |
| SZ3-017 | The complete boundary row is negative pullback from all finite orbit quotients and the real sign quotient. | 3 | independently re-proved |
| SZ3-018 | Haar averaging identifies profinite-rotation coinvariants with locally constant functions on Y/H valued in union d_U^−1 Z. | 3 | separate statement-first root proof reported |
| SZ3-019 | For rational prime rotation on finitely many other local unit groups, its closure is open and its index and denominator group have explicit order formulas. | 3 | separate statement-first root proof reported |
| SZ3-020 | The natural K0 and boundary cokernel reduce to a finite odd-difference matrix and a countable free summand. | 3 | proof and independent finite-group checks |
| SZ3-021 | For P={2,3,5}, K0 has rank7 and boundary cokernel and K1 have torsion Z/2⊕Z/4. | 3 | two independent matrix methods; hand lattice proof |
| SZ3-022 | The compact-unit quotient gives an injective scalar-to-natural extension map with constant unit-fibre ideal map. | 3 | root independently confirmed core construction |
| SZ3-023 | The old-stratum sector for new primes R is G_R×W_P×K_R with the old group acting diagonally on all units. | 3 | proved; separate root targeted proof inspection found no mismatch |
| SZ3-024 | Complementary-prime stabilizations give strictly composing scalar and natural extension inclusions with prescribed generic ideal maps. | 3 | proved; separate root targeted proof inspection found no mismatch |
| SZ3-025 | For the specified local transports the stable Cuntz-sum balancing extension embeds coherently in the natural extension via an exact Busby identity. | 3 | proved; exact Busby identity and coherent target maps inspected by root |
| SZ3-026 | The two real character projections become equal rank-one K0 classes in the natural real boundary. | 3 | independently re-proved |
| SZ3-027 | The constant-label comparison has kernel Z(e+−e−), and its balancing kernel has rank \|P\|. | 3 | independently re-proved |
| SZ3-028 | The full natural K1 is the cokernel of the explicit map B combining odd differences with rotation coboundaries. | 3 | proved; separate statement-only annulus/Mayer–Vietoris reconstruction by circuits; root targeted unitary-proof inspection |
| SZ3-029 | The full K-groups are kernel and cokernel direct limits of finite integer B matrices with ordinary pullback transition maps. | 3 | proved; explicit finite-matrix direct system; follows from independently reconstructed presentation |
| SZ3-030 | A direct-sum classification or splitting criterion for the explicit full K1 presentation is undecided for arbitrary P. | 3 | undecided |
| SZ3-031 | The additive group completion of any idempotent monoid is zero, so the support augmentation lattice is not that completion. | 3 | refutes group-completion interpretation; refined SZ3-004 |
| SZ3-032 | The natural one-prime generic ideal is not Morita equivalent to the scalar generic ideal. | 3 | refutes unit-fibre deletion; refined SZ3-011 |
| SZ3-033 | The unified primitive-defect claims give no defined functor among semiring support, C*-boundaries, CUE, fusion and elliptic surfaces. | 3 | excluded as unified theorem; exact typed components separated |
| SZ3-034 | The generic ideal in the natural one-zero algebra is essential, so the middle algebra identifies with the literal pullback of its Busby map. | 3 | corollary of the faithful expectation and density proof; targeted checks already recorded |
| SZ3-035 | The specified stabilized local scalar edges map injectively to the natural edge extensions with an exact multiplier/corona compatibility identity. | 3 | proved by the compact quotient and coherent local transports; targeted geometric check and separate abstract Busby check |
| SZ3-036 | Each proper finite middle edge has zero K0 and a K1 short exact sequence from the generic functions modulo its invariant pullback to the finite rotation coinvariants. | 3 | consequence of the independently checked injective finite boundary map; full K1 presentation further refines the extension |
| SZ4-001 | The zero adjunction R0=R⊔{tau} is the construction of FGJM Definition 3.6. | 4 | background |
| SZ4-002 | Z0[x1,...,xn] is the free commutative inverse semiring with exponent-set idempotents. | 4 | background |
| SZ4-003 | R0[M] is the inverse semiring of finite subsets S⊂M with coefficient groups R^S and convolution. | 4 | proved |
| SZ4-004 | Allowed-monomial groups over monotone Boolean functions form a lax monoidal functor and a surjective quotient Tn. | 4 | proved |
| SZ4-005 | One variable-input arithmetic gate list returns its Boolean function and formal polynomial in Tn. | 4 | proved |
| SZ4-006 | At tau-off-support integer inputs a circuit returns tau iff the Boolean shadow is false and otherwise the active-monomial sum. | 4 | proved |
| SZ4-007 | A nonnegative polynomial computes fG exactly when all monomial supports contain an edge and every edge occurs as an exact support. | 4 | proved |
| SZ4-008 | Syntactic line-degree equals marked total degree of the nonnegative formal polynomial in the variable-input model. | 4 | proved |
| SZ4-009 | Monotone Boolean size of fG is min over P∈Sup(G) of variable-input nonnegative arithmetic size. | 4 | proved |
| SZ4-010 | For every nonempty C4-free simple graph the exact arithmetic size of HG is \|E\|+vc(G)−1. | 4 | proved |
| SZ4-011 | Neighborhood disjunctions on sets with pairwise intersections≤1 require sum(\|Si\|−1) OR gates even with arbitrary AND gates. | 4 | proved |
| SZ4-012 | A useful degree-one dependent circuit computing a bipartite edge function has no OR of a dependent and pure-side wire. | 4 | proved |
| SZ4-013 | Relevant first mixed AND gates in a C4-free degree-one circuit have centers forming a vertex cover. | 4 | proved |
| SZ4-014 | Transposing the degree-one dependent circuit produces neighborhood sums with at most P_OR+M−\|X\|+1 OR gates. | 4 | proved |
| SZ4-015 | A C4-free bipartite graph has degree-one monotone size exactly \|E\|+vc−1 with separate OR≥\|E\|−1 and AND≥vc bounds. | 4 | proved |
| SZ4-016 | Any bipartite counterexample to the exact graph bound has syntactic degree≥2 on both sides. | 4 | proved |
| SZ4-017 | R0 embeds in R×B as (0,0) together with all (r,1), giving ring and monotone circuit coordinates. | 4 | proved |
| SZ4-018 | Formal supported coefficient zeros and semantic supported output zeros are distinct notions. | 4 | proved |
| SZ4-019 | For final-output-zero-free F2_0 circuits, monotone Boolean size≤C0≤3 times monotone Boolean size. | 4 | proved |
| SZ4-020 | Unrestricted F2_0 arithmetic circuit size is within constant factors of Boolean AND/OR/NOT size. | 4 | proved |
| SZ4-021 | Forbidding the old zero at every useful gate permits only conjunctions and constants, so that reading of the monotone-equivalence claim is false. | 4 | refuted with refinement SZ4-019 |
| SZ4-022 | Polynomial-size Boolean clique circuits are equivalent to polynomial-size unrestricted F2_0 circuits, while final-output-zero-free circuits inherit Alon–Boppana bounds. | 4 | proved |
| SZ4-023 | Every size-s Boolean k-slice function has a monotone circuit of size O(s+n^3), hence polynomial final-zero elimination. | 4 | proved as explicit weak simulation |
| SZ4-024 | A lifted F2 parity sum is tau, old zero or one according as the count is zero, positive even or odd. | 4 | proved |
| SZ4-025 | The Boolean pair {tau,e} is closed under operations with own unit e, but its inclusion in F2_0 is not unital. | 4 | proved |
| SZ4-026 | The maps N[M]→Z0[M]→B[M] preserve semiring operations and the first image has no supported coefficient zeros. | 4 | proved |
| SZ4-027 | Effective sign coefficients N[C2×M] map surjectively to Z0[M] by dimension support and trace. | 4 | proved |
| SZ4-028 | Coefficient cancellation and Boolean exponent identification are independent losses, witnessed by x−x and x²y. | 4 | proved |
| SZ4-029 | Every arbitrary Sup(G) lift of a C4-free bipartite graph requires \|E\|+vc−1 gates. | 4 | undecided |
| SZ4-030 | The exact \|E\|+vc−1 Boolean lower bound holds for all girth≥5 graphs. | 4 | undecided |
| SZ4-031 | The exact \|E\|+vc−1 Boolean lower bound holds for all C4-free graphs. | 4 | undecided |
| SZ4-032 | Line-degree-two circuits obey the historical (incidences−2N)/48 bound. | 4 | background not independently verified |
| SZ4-033 | The exact graph count is verified by exhaustive truth-table circuit enumeration for every nonempty C4-free graph on at most four vertices. | 4 | computation verified |
| SZ4-034 | Every positive-integer-coefficient quadratic polynomial with the edge support of a nonempty C4-free simple graph needs at least \|E\|+vc−1 variable-input gates; HG attains it. | 4 | proved; separate-worker statement-only reproof completed |
| SZ4-035 | The smallest-degree homogeneous part of a positive variable-input circuit polynomial has a circuit of no larger size. | 4 | proved |
| SZ4-036 | For every nonempty C4-free simple graph the minimum witness-read-1 Boolean size is \|E\|+vc−1. | 4 | proved; separate-worker statement-only reproof completed |
| SZ4-037 | For nonempty E2, r missing quadratic edges give size≥\|E2\|+vc(G2)−1+2 when r=1 and +3 when r≥2; full bound for r≤1 and for r=2 with cover drop≤1. | 4 | proved; separate-worker statement-only reproof completed |
| SZ4-038 | Exact full-truth-table SMT synthesis finds no circuit below the star count for C5; four larger instances time out unknown. | 4 | computation verified; no formal UNSAT certificate |
| SZ4-039 | If the quadratic part is nonzero and an edge lacks a quadratic witness, lower-envelope extraction removes an addition and a multiplication. | 4 | proved; separate-worker statement-only reproof completed |
| SZ4-040 | For the ideal J(P) generated by coefficient-free monomials, P∈Sup(G) iff sqrt(J(P)) is the squarefree edge ideal. | 4 | proved as dictionary translation |
| SZ4-041 | If at least two edges lack quadratic witnesses in a C4-free graph and the quadratic part is nonzero, canonical lower-envelope extraction and pruning discard at least three gates. | 4 | proved; separate-worker statement-only reproof completed |
| SZ4-042 | The path example has exactly2 discarded gates for1 missing edge; d(a+(sum of t leaves)^2) has t+1 discarded gates for t missing edges, sharp at t=2,3. | 4 | proved by expansion; original two examples computed; root independently checked the three-leaf and general gate count |
| SZ4-043 | A girth5graph with12vertices and14edges has a19gate valid circuit with r2,cover drop2,and only3discarded gates; thus discarded≥r+coverdrop is false. | 4 | proved; root statement-only derivation and independent4096-input/girth/cover recomputation completed; full comparison agreed |
| SZ4-044 | Every C4-free edge circuit with at most two missing squarefree quadratic witnesses meets the full \|E\|+vc(G)−1 gate bound. | 4 | proved; separate-worker statement-only reproof completed; mutual comparison agreed |
| SZ4-045 | For every nonzero commutative ring R, Boolean τ/1-output circuits allowing +,×,unary inverse obey Cmon≤C0,R≤4Cmon; intermediate old zeros allowed. | 4 | proved; root targeted check agreed |
| SZ4-046 | Equality in the weighted C4-free quadratic bound forces every edge coefficient to be1 and every nonoutput gate to have fanout1, with a minimum-cover partition into stars. | 4 | proved; root statement-only independent reproof communicated |
| SZ4-047 | If at least three C4-free graph edges lack quadratic witnesses and P2 is nonzero, canonical extraction/pruning removes at least four gates. | 4 | proved; separate-worker derivation using checked auxiliary results completed |
| SZ4-048 | A product of k old-neighborhood linear forms has an induced matching of r missing edge supports, with k≥2^r; equality forces all matching transversals as factors. | 4 | proved; foundation fresh statement-only reproof and operator corroboration completed |
| SZ4-049 | For a nontrivial commutative semiring P, its nonzero indicator is a Boolean homomorphism iff P is zero-sum-free with no zero divisors iff P0→P has a unital section iff all circuit shadows detect nonzero outputs. | 4 | proved in intake; targeted source comparison, not fresh statement-only check |
| SZ4-050 | For an F2_0 lift, final old-zero inputs are exactly the shadow majorant minus the true inputs; N(z)=1+z satisfies N²(z)=z+e and N³=N. | 4 | proved by two-coordinate and three-value calculation; source credited |
| SZ4-051 | For n≥3 the canonical formal R0 determinant with exactly permutation occupied exponents needs at least binom(n,floor(n/3)) binary gates, even with scalar constants and unary inverse. | 4 | proved; fresh foundation statement-only proof completed and fully compared |
| SZ4-052 | For valid cubic products UVD_i with two fixed old-neighborhood factors U,V and all remaining factors old-neighborhood linear forms, all missing edge supports share one vertex. | 4 | proved; fresh foundation statement-only derivation completed and fully compared |
| SZ4-053 | Four valid old-neighborhood cubic products U_i B D_j for i,j in{1,2} have at most3 distinct missing exact edge supports. | 4 | proved; root fresh statement-only derivation completed and fully compared |
| SZ4-054 | For a C4-free graph, a variable-input circuit in Sup(G) with nonzero quadratic part and at least4 missing quadratic edge witnesses loses at least5 gates under canonical extraction and pruning. | 4 | proved; complete targeted separate-worker check after a durable partial fresh attempt; a further fresh full attempt is incomplete and parked, not a completed check |
| SZ4-055 | Two independent old-form products UV and WX with mandatory old cross contexts A,B,L,M supply at most2 missing edges in UVL+WXM+UVWX under the stated C4-free validity hypotheses. | 4 | proved; separate-worker statement-only derivation and full comparison; earlier quartic-equality background and elementary parent reduction disclosed |
| SZ4-056 | In the four-deletion two-product/two-cut normal form f=(A+alpha UV)W, zero cross coefficient and a nonzero direct context of UV force at most2 missing edges; optimality is unnecessary. | 4 | proved; separate-worker statement-only derivation and full comparison; previously checked normal form and055 are disclosed background |
| SZ4-057 | In the one-affected-input two-product/two-cut normal form with zero cross coefficient, zero direct first context, optimal quadratic remainder and exactly3 missing edges, vc(G)≤vc(H)+1. | 4 | proved; separate-worker statement-only derivation and full comparison; no full r3 theorem claimed |
| SZ4-058 | Two valid old-neighborhood quartics ABCD and ABCE have at most2 missing exact edge supports in their union. | 4 | proved; root separate statement-only derivation completed and fully compared |
| SZ4-059 | For valid old cubics UVL,UVD,ABD with nonzero a supported in A∩B and aL supported on H, the first two together have at most1 missing edge and all3 together at most2. | 4 | proved; separate-worker statement-only derivation and full comparison; exact circuit hypotheses checked |
| SZ4-060 | In an optimal four-deletion frame with products g=UV,f=gW, zero cross coefficient and r3, the graph cover gain is at most1. | 4 | proved; root separate statement-only derivation completed and fully compared |
| SZ4-061 | With three missing quadratic edges and exactly four deleted gates, one of them a product, an optimal quadratic remainder forces vc(G)≤vc(H)+1. | 4 | proved; completed separate statement-only derivation and full comparison with disclosed auxiliary exposure |
| SZ4-062 | With nonempty quadratic support H, exactly three missing edges and exactly four deletions, an optimal quadratic remainder forces vc(G)≤vc(H)+1. | 4 | proved; completed separate statement-only derivation and full comparison with disclosed auxiliary exposure |
| SZ4-063 | With nonempty H and exactly three missing edges, cover gain≥2 forces size≥\|E(H)\|+vc(H)+4; the full star bound follows for gain≤2 and one below it for gain3. | 4 | proved; completed separate statement-only derivation and full comparison with disclosed auxiliary exposure |
| SZ4-064 | With nonempty H, exactly three missing edges and exactly four deleted gates, the missing-edge graph has cover number≤2 without any optimality assumption; a gain3 one-gate deficit requires five deletions and an optimal remainder. | 4 | proved; completed separate statement-only derivation and full comparison with disclosed auxiliary exposure |
| SZ4-065 | Every nonempty simple graph with at most three edges has Boolean edge-circuit complexity \|E\|+vc(G)−1, without a witness restriction; this settles the empty-quadratic three-missing case. | 4 | proved; foundation fresh statement-only proof and full comparisons completed |
| SZ4-066 | The specified two-product expression gL+fM+alpha g²+beta gf+gamma f², with the six allowed dependent or independent f forms and arbitrary nonnegative affine contexts, cannot compute a three-edge matching. | 4 | proved; fresh foundation statement-only proof and full comparisons completed; the circuit-to-template reduction is separately proved as067 |
| SZ4-067 | For a positive variable-input circuit of minimum output degree2, at most two deleted products admit a Boolean-equivalent, exact-quadratic-frame-preserving polynomial P2+gL+fM+alpha g²+beta gf+gamma f² in the six-form template, with arbitrarily many deleted additions. | 4 | proved; fresh foundation statement-only derivation and complete author comparison; minimum output degree2 explicit |
| SZ4-068 | In the nonempty-H, three-missing, cover-gain3, five-deletion optimal-frame residual, neither four products plus one cut nor three products plus one cut and one private equal-degree addition can occur. | 4 | proved; complete fresh root statement-only proof and full mutual comparison |
| SZ4-069 | The nonempty-H, three-missing, cover-gain3, optimal-frame five-deletion residual cannot consist of three products and two unequal-degree cuts. | 4 | proved; fresh foundation derivation and complete mutual comparison, plus full circuits and root targeted audits |
| SZ4-070 | For every nonempty C4-free simple graph, any positive variable-input binary circuit in Sup(G) missing at most three quadratic edge witnesses has at least \|E\|+vc(G)-1 gates; the star circuit attains the class minimum. | 4 | proved; root fresh conditional synthesis saved before author access, dependency closure and full comparison completed20:13:52UTC; unrestricted four-or-more-missing problem remains open |
| SZ4-071 | An induced missing matching of three edges is compatible with five deleted gates and an optimal quadratic frame: an11-vertex C4-free example has H10edges cover5, G13edges cover6, and19gates retaining14. | 4 | proved; statement-only independent derivation and all2048truth assignments, exact extraction and cover/C4 checks completed; maximal-gain residual unaffected |
| SZ4-072 | For any simpleG and nonzero quadraticH, a six-vertex induced matching of three G-edges with H[T]empty forces at least three deleted multiplication gates, without C4, optimality, cover-number or deleted-addition assumptions;071 is sharp. | 4 | proved; separate operator statement-only synthesis and full comparison completed |
| SZ4-073 | Setting k distinct occurring variables to zero in a constant-free monotone binary circuit with nonzero restricted output removes at least k gates under zero propagation, bypass and pruning. | 4 | proved; fresh operator statement-only derivation and full bidirectional comparison; circuits targeted comparison completed |
| SZ4-074 | Every nonempty C4-free simple graph with at most four edges has monotone Boolean edge complexity \|E\|+vc(G)-1, with no restriction on its arithmetic witness degrees or quadratic part. | 4 | proved; fresh operator statement-only derivation and full bidirectional comparison; empty-quadratic four-missing boundary closed |
| SZ4-075 | For any simple graph, nonzero quadratic support and eight vertices inducing four disjoint missing edges with no old edge, canonical extraction deletes at least six total gates; no C4, cover, optimality or deleted-addition assumptions. | 4 | proved; fresh circuits derivation saved before new author proof or route-summary exposure, disclosed older069background; full bidirectional comparison and root targeted audit completed |
| SZ4-076 | For exactly four missing quadratic witnesses in a C4-free graph, any saving has nonempty H and only (d;D,e)=(2;5,0),(3;5,0),(3;5,1),(3;6,0),(4;6,0),(4;6,1),(4;7,0); these are necessary pairs, not existence claims. | 4 | proved; separate root targeted arithmetic and maximal-cover-gain check completed, earlier author-ledger exposure disclosed; unrestricted r4 theorem remains open |
| SZ4-077 | For C4-free G with nonemptyH, exactly four missing quadratic edges, cover gain4, optimal extracted quadratic frame and exactly six deletions, the deleted gates cannot be four products and two additions. | 4 | proved; fresh circuits proof saved before new author access, disclosed075background; full bidirectional comparison and root targeted check completed; other residual profiles remain open |
| SZ4-078 | For any simpleG and nonzero quadraticH, an induced missingr-edge matching with exactly one deleted addition forces at least2^r−2deleted products and2^r−1total deletions. | 4 | proved; root fresh statement-only derivation and full bidirectional comparison; arbitrary fanout and feedback included |
| SZ4-079 | For C4-freeG with nonemptyH, r missing edges, maximal cover gainr and an optimal extracted quadratic frame, at least r deleted gates are multiplications, with arbitrarily many deleted additions. | 4 | proved; complete fresh circuits derivation saved before new author access, admitted background disclosed; full bidirectional comparison and root audit; earlier p3/a3 case attempt remains separately partial |
| SZ4-080 | For four missing witnesses, the maximal-gain optimal-frame D6 case is impossible; remaining necessary pairs are d2:(5,0),d3:(5,0),(5,1),(6,0),d4:(6,1),(7,0), and the last optimal D7case has onlyp4/a3 orp5/a2. | 4 | proved; separate targeted synthesis checks; no existence assertion for remaining pairs and no unrestrictedr4claim |
| SZ4-081 | At maximal cover gain4 with optimal total quadratic frame, seven deleted gates cannot be five products plus two additions; onlyp4/a3 remains in the optimalD7row. | 4 | proved; fresh circuits proof saved21:44:24before new author access; full bidirectional comparison completed; other gain/excess cases remain open |
| SZ4-082 | The maximal-gainr deleted-product bound holds if the extracted quadratic frame has exactlyvc(H)multiplications, without any optimality requirement on retained additions or total frame size. | 4 | proved; separate foundation derivation before new-author access conservatively targeted, full mutual comparison and circuits targeted check; no claim excluding all excess-one cases |
| SZ4-083 | At maximal cover gain r with an optimal total quadratic frame, exactly r deleted products force at least r deleted additions. | 4 | proved; separate derivation before new author access with broad route-label exposure disclosed, full mutual comparison and root targeted audit |
| SZ4-084 | The equality addition bound p=r implies a>=r holds with exactly vc(H) retained products and unrestricted retained additions. | 4 | proved; separate full strengthened-scope derivation before new author access with admitted predecessor-proof exposure, full mutual comparison and root audit |
| SZ4-085 | At maximal cover gain four with exactly vc(H) retained products, at most five deleted products and at most two deleted additions are impossible, regardless of retained addition count. | 4 | proved; complete separate new-scope derivation before author access, full mutual comparison and root targeted audit; direct-g case explicit |
| SZ4-086 | For four missing edges at maximal cover gain four, a minimum-product quadratic frame forces at least eight deleted gates and the full star count; only the extra-retained-product subcase remains in maximal-gain excess-one residual. | 4 | proved; separate synthesis before new author access, full mutual comparison and root audit; lower-cover-gain rows and extra-retained-product case remain open |
| SZ4-087 | A pruned positive quadratic C4-free edge circuit with K products and exactly m+K−1 total gates has coefficient-one output and an edge partition into star trees with an outer addition tree; centers may repeat and same-center leaves are disjoint. | 4 | proved; separate circuits derivation saved22:10:19before new author access, admitted predecessor equality background disclosed; full author and reverse comparison; describes but does not close the extra-product residual |
| SZ4-088 | For a C4-free graph with H-cover C and matching outside C, an old product AL and a safe gL with a complementary-pair witness force a two-point outside context L to have no additional cover vertex. | 4 | proved; foundation statement-first proof and full restricted author comparison, root and circuits targeted checks; no normalization claim |
| SZ4-089 | At maximal four-edge cover gain, a pruned quadratic frame with K=vc(H)+1 products and m(H)-1 additions cannot have four deleted products and two deleted additions. | 4 | proved; operator fresh proof saved22:58:01before new author access; full comparisons; circuits k3 transcription corrected23:00:56, conclusion unchanged; p3/a3 remains open |
| SZ4-090 | A safe sum of three independent quadratic products times affine-linear contexts, with pairwise product terms, has at most three matching-edge witnesses; no dependent-circuit normalization is claimed. | 4 | proved; foundation statement-first derivation and full mutual comparison, circuits targeted comparison; square terms absorbed only in support/Boolean sense |
| SZ4-091 | With nonempty quadratic support H and exactly vc(H) retained multiplications, at most one deleted multiplication implies vc(G)<=vc(H)+1 for C4-free G; all additions and missing-witness counts are unrestricted. | 4 | proved by separate statement-first derivation and full targeted comparisons; original author restriction-based replacement route has an explicitly preserved gap and is replaced |
| SZ4-092 | A twelve-gate tree example has one deleted product, cover gain two, and four retained products versus vc(H)=2; the minimum-product hypothesis in091 cannot be omitted. | 4 | proved and independently recomputed by a different method; above the full star count, so no unrestricted counterexample |
| SZ4-093 | With minimum output degree two, pairwise nonancestral original deleted products admit exact-frame normalization to P2+sum giLi+sum cijgigj; at most three such products cannot realize an induced missing four-edge matching. | 4 | proved after full mutual comparison; no normalization of dependent private products |
| SZ4-094 | At most one deleted multiplication implies cover gain d<=min(2,K-vc(H)+1) for arbitrary retained multiplication count K; the universal bound2 is sharp. | 4 | proved; separate scoped derivations before new-author access and full mutual comparisons; sharpness asserted only for universal2 |
| SZ4-095 | A safe literal chain of three product signals with affine contexts and pairwise signal terms witnesses at most two matching edges; the abstract bound is sharp. | 4 | proved in exact stated scope; separate proofs and full comparisons recorded |
| SZ4-096 | Exactly four missing edges, cover gain at least3and minimum retained multiplication count force at least3deleted products, with all additions unrestricted. | 4 | proved in exact stated scope; separate proofs and full comparisons recorded |
| SZ4-097 | Every literal multiplicative-operand ancestry on at most three signals with affine contexts and quadratic signal terms witnesses at most three matching edges; an abstract example attains3. | 4 | proved in exact stated scope; separate proofs and full comparisons recorded |
| SZ4-098 | With four missing edges, cover gain at least3and minimum retained products, exactly one deleted addition requires at least6deleted products. | 4 | proved in exact stated scope; separate proofs and full comparisons recorded |
| SZ4-099 | Three exact shared-nonlinear-sum fork/chain/join templates witness at most3matching edges via14/14/11clause bounds; no general ancestry normalization or extra gate charge. | 4 | proved in exact stated scope; separate proofs and full comparisons recorded |
| SZ4-100 | For four missing quadratic edges and cover gain at least3, exactly one deleted addition requires at least6deleted products, with arbitrary retained product and addition counts. | 4 | proved in stated scope; foundation new-scope event targeted, operator statement-first proof chronology separate; now a specialization of101 |
| SZ4-101 | With exactly one deleted addition and r>=1missing quadratic edges in a C4-free graph, those edges form an induced matching and p>=2^r-2; if the cut retains degree2then p>=2^r-1, with arbitrary retained counts and cover gain. | 4 | proved in stated scope; separate foundation proof saved00:10:12before author access, full mutual comparisons passed |
| SZ4-102 | For every C4-free G and P in Sup(G) with nonempty quadratic support, at most one original deleted addition forces the full star lower bound, with arbitrary missing-witness count and retained frame. | 4 | proved; complete circuits separate proof saved00:27:31before root-author access00:29:40, full mutual comparison passed |
| SZ4-103 | A safe product of old-neighborhood forms with at least3missing edge witnesses has one H-neighbor adjacent to every missing endpoint; in girth at least5there are at most2such witnesses, also for every one-deleted-addition circuit with nonempty H. | 4 | proved; complete separate proof saved00:27:31before root-author access00:29:40, full mutual comparison passed; no sharpness claim |
| SZ4-104 | For g=UV,h=(A+g)W,z=XY, every safe matching expression gP+hB+zC+delta*g*z+eta*h*z with affine contexts has at most3matching witnesses; both cross terms are allowed and the abstract bound3is sharp. | 4 | proved in exact displayed template; full separate proof and mutual comparison passed; arbitrary three-product normalization remains open |
| SZ4-105 | With r4, cover gain>=3, minimum retained product count and outside graph P4 disjoint K2 or K3 disjoint K2, at most3deleted products and at most2deleted additions are impossible; in the minimum-product gain3/D5 residual only outside3K2or P3 disjoint2K2remain. | 4 | proved at original p<=3,a<=2scope; now a corollary of separately checked106; original separate proof and comparisons preserved |
| SZ4-106 | For r4, cover gain>=3, minimum retained products and outside graph P4 disjoint K2 or K3 disjoint K2, at least3original additions are deleted, with arbitrary deleted multiplication count. | 4 | proved in stated scope; minimum retained products and exceptional outside graph retained; induced-matching outside branches and extra-product frames remain open |
| SZ4-107 | The displayed three-product template with a two-sided first dependency has at most3matching witnesses, allowing all third-product earlier-signal coefficients and cross terms; abstract3is sharp. | 4 | proved in exact algebraic template; no general circuit normalization or gate-budget sharpness |
| SZ4-108 | On an induced outside P3 plus2K2 with empty H restriction, a safe old-factor expression gL+fM+qgf with at most3factors in g and2in f cannot witness all4edges, including affine contexts and isolates. | 4 | proved in displayed template; circuit synthesis separately proved as109 |
| SZ4-109 | For any C4-free G and nonempty quadratic support H, an induced outside P3 plus2K2 with H[T] empty cannot occur with exactly3deleted products and2deleted additions; no cover-gain or retained-count hypothesis. | 4 | proved with disclosed075classification and108background; removes path outside shape, leaves3K2with fourth missing edge meeting C in minimum-product gain3/D5 |
| SZ4-110 | The displayed different-low fork x=UV,y=(A+x)B,z=(C+x)D has at most3matching witnesses with arbitrary affine contexts and quadratic readout. | 4 | proved in exact algebraic template; no original circuit normalization inferred alone |
| SZ4-111 | Every safe three-product topological recursion with linear-plus-earlier-product operands and affine/quadratic readout has at most3matching witnesses; abstract3is sharp. | 4 | proved unconditionally after110dependency closure; original-circuit consequence via112is separately115 |
| SZ4-112 | For any finite number of deleted products, exact full-carrier erasure gives topologically recursive linear-plus-earlier-product operands and an exact P2 plus affine-context and quadratic-private-product output, preserving the entire quadratic frame and gate bound. | 4 | proved unconditionally; arbitrary recursion and addition counts included; four-matching consequence now separately proved as115 using111 |
| SZ4-113 | With exactly4missing quadratic edges and cover gain4, every C4-free edge circuit has at least its star count, with arbitrary retained multiplication and addition counts. | 4 | proved in full maximal-cover-gain-four scope; lower-gain four-witness cases remain open |
| SZ4-114 | In the minimum-product gain3/D5 p3/a2 case with outside3K2, the fourth missing edge crosses the old cover; if its outside endpoint has a matching mate then the corresponding old mate edge exists. Girth>=5leaves only an outside-isolate attachment. | 4 | proved in exact stated frame and gate profile; isolated attachment remains open |
| SZ4-115 | Any induced four-edge matching with empty quadratic restriction forces at least4original deleted multiplication gates; no C4, cover, retained-count or deleted-addition assumption. | 4 | proved for every finite simple graph with nonzero quadratic part; lower bound on products rather than total deletions |
| SZ4-116 | An essential variable outside an induced missing three-matching and absent from every quadratic edge excludes at most3deleted products and at most2deleted additions, with arbitrary retained counts. | 4 | proved in exact scope; excludes new pendant attachment but not an outside endpoint with old neighbors |
| SZ4-117 | For four specified missing targets hz,zzprime,ab,cd with the last three inducing a matching and empty quadratic restriction, no safe independent pair gL+fM+qgf with at most3and2old factors witnesses all four; arbitrary other h-edges are allowed. | 4 | proved in exact algebraic template; arbitrary old closing triangle permitted; no original-circuit normalization asserted alone |
| SZ4-118 | An induced missing three-edge matching and a fourth missing edge attached to one matching endpoint exclude at most3deleted products and at most2deleted additions, without retained-count, cover-gain or total-missing-count assumptions. | 4 | proved in exact scope including arbitrary old h edges; minimum-product gain3/D5 residual now requires outside-isolate attachment with an old neighbor; lower-gain rows remain open |
| SZ4-119 | A safe independent pair gL+fM+qgf with at most3and2old factors cannot witness four pairwise vertex-disjoint missing edges, even when their eight endpoints have arbitrary old or new cross edges. | 4 | proved in exact algebraic template; inducedness of all eight endpoints is not assumed |
| SZ4-120 | An induced missing three-edge matching plus a disjoint fourth missing edge excludes at most3deleted products and at most2deleted additions, with arbitrary retained counts and cross edges. | 4 | proved; together with118excludes every further missing edge beyond an induced missing three-matching in the p3/a2profile |
| SZ4-121 | With exactly4missing edges, cover gain3 and exactlytau(H)retained multiplications, canonical extraction deletes at least6gates, with arbitrary retained additions. | 4 | proved; removes d3(D,e)=(5,0)and forces the remaining d3(5,1)case to have one extra retained product and minimal retained additions; other rows remain open |
| SZ4-122 | For any retained frame, an induced missing P4 plus K2 or K3 plus K2 excludes at most three deleted products and at most two deleted additions. | 4 | proved in exact induced-graph scope; arbitrary retained counts and other missing edges |
| SZ4-123 | For an optimal extracted frame whose minimum star-center cover avoids an induced matching of all four missing edges, at most four deleted products and two additions imply cover gain at most two. | 4 | proved; excludes only the stated outside-four-matching four-product/two-addition profile |
| SZ4-124 | With four missing edges and cover gain at least three, at most three deleted products and two additions are impossible for arbitrary retained counts; the remaining gain3 five-deletion excess1 row has exactly two products and three additions. | 4 | proved; two-product/three-addition residual remains open |
| SZ4-125 | An induced H-empty P4 or triangle forces at least three deleted additions, with arbitrary private product and retained counts. | 4 | proved in full stated induced-path/triangle scope; private p3/a3 and other residual profiles remain open |
| SZ4-126 | An induced H-empty P4 plus K2 or triangle plus K2 excludes at most2nonancestral private products and at most3additions when every deleted addition is a visible unequal-degree cut, with arbitrary retained counts. | 4 | proved in exact nonancestral/all-visible scope; dependent and hidden/private-addition branches remain outside this proposition |
| SZ4-127 | An induced H-empty P4 plus K2 or K3 plus K2 excludes two dependent deleted products and three additions when every deleted addition is a selected visible cut, with arbitrary retained counts. | 4 | proved in exact all-visible scope; hidden-cut case is outside the statement |
| SZ4-128 | For arbitrary simple G, one selected visible cut and p deleted products imply at most2^p+1 maximal independent sets on every induced H-empty nonempty target; at most2^p if the cut retains degree2. Hidden additions and retained counts are unrestricted. | 4 | proved; at p<=2 excludes exceptional induced targets only in the one-visible-cut branch |
| SZ4-129 | At most two deleted additions force maximum degree at most two in the missing-edge graph, with arbitrary multiplication and retained counts. | 4 | proved; subsumed in shape by132, retained as proof ingredient |
| SZ4-130 | A hidden-cut two-product/three-addition circuit realizes the induced exceptional target: expanded23gate example has H13edges,tau5,G17edges,tau7,18retained gates and one extra product; smaller18gate example has optimal13gate frame and zero cover gain. | 4 | verified; expanded circuit equals star count, smaller is one above; no saving-row counterexample |
| SZ4-132 | For any C4-free graph with nonempty quadratic support, at most two deleted additions force every nontrivial missing-edge component to be K2 or P3; products, retained counts and cover gain unrestricted. | 4 | proved necessary shape condition; no realization claim or full numerical-row closure |
| SZ4-133 | The normalized hidden-dependent network g=UV,t=C+g,f=tW with exactly two visible insertion cuts and four missing edges satisfies tau(G)<=K+1 for arbitrary retained product count K. | 4 | proved in exact normalized network; no general hidden-addition normalization; sharp via130 |
| SZ4-134 | With four missing quadratic edges, two deleted products and three additions, exactly two visible cuts, and a hidden original unequal-degree addition, K<=tau(H)+1 forces cover gain at most two. | 4 | proved hidden-unequal profile; hidden homogeneous branch separate |
| SZ4-135 | An induced H-empty P4 plus K2 or triangle plus K2 cannot be realized by two nonancestral private products reading one pure private linear sum and two visible insertion cuts, with arbitrary retained counts, sharing and squares. | 4 | proved in exact pure-linear/nonancestral profile; broader homogeneous synthesis separate |
| SZ4-136 | An induced H-empty P4 disjoint K2 or K3 disjoint K2 cannot occur after exact-frame carrier erasure with at most two useful private products, three additions, exactly two visible cuts and a hidden equal-minimum-degree addition; arbitrary retained counts and affected full operands allowed. | 4 | proved exact hidden equal-minimum-degree branch; no cover or retained-count assumption |
| SZ4-137 | For four missing quadratic edges, cover gain at least3 and K<=tau(H)+1, at most two deleted products and three additions are impossible. This removes the complete d3(D,e)=(5,1) saving row. | 4 | proved after136dependency closure; only d2(5,0) and d3(6,0) remain necessary numerical possibilities |
| SZ4-138 | At cover gain at least3 with four missing edges and minimum retained product count, an exceptional outside graph P4 disjoint K2 or K3 disjoint K2 requires at least four deleted products if every deleted addition is visible and private products are pairwise nonancestral. | 4 | proved exceptional-outside/all-visible/nonancestral minimum-product scope only |
| SZ4-139 | If four missing edges have only K2/P3 components, safe old products ABCL,DEM,ABCDE cannot jointly witness all four; scalar/zero contexts and shorter factors satisfy the explicit independent-high corollary. | 4 | proved exact algebraic template, no exhaustive private-circuit normalization asserted |
| SZ4-140 | No disjunction of selected outputs among three recursive old-form products computes an H-empty induced P4+K2 or K3+K2, allowing unsafe unselected intermediates. Consequently the minimum-product/gain>=3 exceptional-outside all-visible profile requires at least four deleted products, without ancestry restrictions. | 4 | proved precise algebraic template and exceptional-outside/all-visible consequence; hidden additions and other outside shapes separate |
| SZ4-142 | At cover gain at least3 with four missing quadratic edges, minimum retained product count and exceptional outside graph P4+K2 or K3+K2, pairwise nonancestral original private products require at least four deleted additions, with arbitrary deleted product and retained addition counts. | 4 | proved original nonancestry and arbitrary-addition placement scope; dependent products and other outside graphs remain separate |
| SZ4-143 | With four missing edges, exactly two deleted products and three deleted additions, two visible cuts and one originally unequal hidden addition, vc(G)<=K+1 for arbitrary retained product count K. | 4 | proved arbitrary-K hidden-unequal profile; hidden equal-degree and all-visible arrangements separate |
| SZ4-144 | With minimum retained products, cover gain at least3, four missing edges and exceptional outside graph P4+K2 or K3+K2, at most three private products force an original deleted addition with both input minimum degrees1; other additions and product ancestry unrestricted. | 4 | proved original minimum-degree-one sum requirement, not full operand homogeneity; exceptional-outside/minimum-product scope |
| SZ4-145 | With exactly four missing quadratic edges in a C4-free graph, at most three deleted products and at most two deleted additions are impossible, with arbitrary retained counts and cover gain. | 4 | proved global four-missing two-addition profile; remaining gain-two saving has p2/a3 |
| SZ4-146 | At most two original nonancestral deleted products and at most three deleted additions, all visible unequal-degree cuts, permit at most three missing quadratic edges in any C4-free edge circuit. | 4 | proved global all-visible/nonancestral profile; no cover/outside/retained-count hypothesis |
| SZ4-147 | On an H-empty induced P4+K2 or K3+K2 in a C4-free graph, a safe product of one arbitrary homogeneous linear form and any positive number of old linear forms witnesses at most two of the four target edges. | 4 | proved exact algebraic target restriction; arbitrary factor count and isolates, no frame or cover hypothesis |
| SZ4-148 | At minimum retained multiplication count and cover gain at least3, an exceptional outside target P4+K2 or K3+K2 cannot have at most three deleted products, three additions and exactly one visible cut. | 4 | proved exceptional minimum-product/gain-three one-visible profile; the complementary two-visible original1+1 profile is subsequently excluded by152 |
| SZ4-149 | With four missing edges, at most two private products and three private additions all visible, vc(G)<=K+1 for arbitrary retained product count K. | 4 | proved arbitrary-K all-visible cover bound; optimal-frame gain-two all-visible branch excluded |
| SZ4-150 | With four missing edges and p2/a3, exactly two visible cuts and one hidden equal-original-degree sum, full-current-carrier erasure leaves that sum purely homogeneous linear with two old operands. | 4 | proved exact two-visible normalization only; original full operands need not be homogeneous; pure sum and one-visible placements not excluded |
| SZ4-151 | Two original nonancestral private products using old forms and one pure private old-linear sum, with two visible insertion cuts, permit at most three missing quadratic edges globally. | 4 | proved global pure-linear/nonancestral/two-visible profile; dependent and one-visible configurations separate |
| SZ4-152 | At minimum retained multiplication count and cover gain at least3, an exceptional outside target P4+K2 or K3+K2 cannot have at most3 deleted products,3 additions, exactly2 visible cuts and one hidden original1+1 addition; full operands and ancestry unrestricted. | 4 | proved precise exceptional two-visible profile; with140/144/148 removes exceptional p3/a3 allocation, not the full D6 row |
| SZ4-153 | A safe old quartic grid EF(A1+A2)(B1+B2) has at most three exact missing-edge witnesses in a C4-free graph, with arbitrary full supports and repetitions. | 4 | proved pure algebraic grid bound; no circuit/count/cover assumption |
| SZ4-154 | A two-visible-cut two-product network with original product ancestry and a hidden pure sum of old linear forms has at most three missing quadratic edges globally. | 4 | proved dependent pure-linear two-visible branch; with149-151 leaves exactly one visible cut/two hidden additions in d2/D5 |
| SZ4-155 | Two safe old-factor products witnessing four distinct missing edges of vertex-cover number at least three require at least eight distinct factor supports in their union. | 4 | proved distinct-support union count; no circuit normalization or cover exchange claimed |
| SZ4-156 | With four missing edges of cover number at least three and p4/a2, neither exactly one visible cut nor two visible cuts with all four products ancestral to the first high is possible. | 4 | proved exact two boundary profiles for arbitrary retained counts; other two-visible allocations and p3/a3 remain separate |
| SZ4-157 | With exactly four missing edges, p2/a3 and exactly one visible cut, vc(G)<=K+1 for arbitrary retained products K and arbitrary original hidden-addition degrees. | 4 | proved arbitrary-K one-visible/two-hidden cover bound; combines with145/143/149-151/154 to exclude entire d2/D5/e0 row |
| SZ4-158 | With four missing edges, at most four private products, two visible cuts, multiplicative old-boundary high networks and zero independent-symbol cross coefficient, vc(G)<=K+2. | 4 | proved arbitrary-K exact unaffected/zero-cross cover bound; excludes that p4/a2 gain-three optimal-frame branch only |
| SZ4-159 | In the exact two-symbol quadratic frame, an old cubic high with two direct missing witnesses and a second high R OR gT with at most three old factors in R force vc(G)<=K+2, even with positive mixed coefficient. | 4 | proved precise cubic-high cover bound; arbitrary K, q>=0 and polynomial T; no general two-cut normalization |
| SZ4-160 | In the original two-visible frame, g=UVW old cubic and f=C(A OR g)(B OR g) with actual low/context inclusions imply vc(G)<=K+2 for four missing edges and arbitrary q>=0. | 4 | proved precise two-affected-factor cover bound, arbitrary K and q; positive-q profile impossible; no general normalization |
| SZ4-161 | An old cubic first high followed by a product of three old-or-first-cut-affected boundaries in the exact two-visible frame gives vc(G)<=K+2 for four missing edges, arbitrary q and retained K. | 4 | proved precise three-boundary cover bound for all affected subsets; proper private-ancestor inputs and other factor allocations remain separate |
| SZ4-162 | A monotone circuit on linear boundary clauses with at most3 ANDs and2 ORs has at most6 positive CNF clauses or is a union of3 products of at most2 original clauses; hence p<=3/a<=3 with exactly one visible cut cannot realize an induced H-empty P3+2K2. | 4 | proved abstract DAG dichotomy and exact one-visible P3+2K2 exclusion; arbitrary retained counts, hidden degrees and total missing-edge count; other visible allocations remain open |
| SZ4-163 | In the exact two-visible frame, a first high Boolean-equivalent to at most4 old linear factors and a second high with2 old-or-first-cut-affected boundaries imply vc(G)<=K+2 for four missing edges, arbitrary q and retained K. | 4 | proved exact Boolean old-quartic/two-boundary cover bound; original arithmetic degrees and actual contexts remain fixed; proper private-ancestor input and general p4/a2 normalization remain separate |
| SZ4-164 | For all four global missing edges forming induced H-empty P3+2K2, at most3 deleted products and3 additions with all additions visible and original pairwise nonancestral products imply vc(G)<=K+2 for arbitrary retained K. | 4 | proved arbitrary-K original-product cover bound; minimum-product gain-three all-visible nonancestral P3+2K2 branch excluded; dependent or hidden products remain separate |
| SZ4-165 | Raw old-product divisors of an at-most-four-factor high have no four missing witnesses of cover number three; actual-frame cover bound K+2. | 4 | proved; complete separate derivation and mutual comparisons; inserted |
| SZ4-166 | The exact raw quadratic ancestor/two-boundary two-cut template has missing cover at most two and total cover at most K+2. | 4 | proved; complete separate derivation and mutual comparisons; inserted |
| SZ4-167 | Under at most4private products/2additions and tau(G)>K+2, exact original-operand reduction gives the Boolean-quadratic/four-boundary residual, retaining the original square case and all low/context relations. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-168 | The exact quadratic-first/four-old-or-affected-boundary template has missing cover at most two and total cover at most K+2. | 4 | proved; complete separate derivation and mutual comparisons; inserted |
| SZ4-169 | On induced missing P3 disjoint two edges, two unaffected zero-cross highs using at most three joint products and one extra linear boundary give cover at most K+2. | 4 | proved; complete separate derivation and mutual comparisons; inserted |
| SZ4-170 | Safe old product-first/quadratic-union-second template cannot supply four selected missing edges forming P3 plus two disjoint edges; extra global missing/ambient edges allowed. | 4 | proved; full separate derivation and mutual comparisons; inserted |
| SZ4-171 | At most4deleted products and2deleted additions with four missing edges imply tau(G)<=K+2 for arbitrary retained K; hence the sole d3/D6/e0 saving row has only p3/a3. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-172 | Two unaffected highs jointly using at most3 products and one arbitrary linear preparation on induced P3+2K2 imply tau(G)<=K+2 for arbitrary cross coefficient and retained K. | 4 | proved; full separate derivation and mutual comparisons; inserted |
| SZ4-173 | At most3 common-quadratic-ancestor chain/fork high occurrences cannot safely witness induced H-empty P3+2K2; precise old/raw-only original profile consequence. | 4 | proved; full separate derivation and mutual comparisons; inserted |
| SZ4-174 | In the specified minimum-product gain3 matching-attachment p3/a3 profile, no original deleted addition has both input minimum degrees1. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-175 | The exact literal-join three-visible profile u=AB,v=CD,w=uv on induced global missing P3+2K2 has tau(G)<=K+2 for arbitrary original retained K. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-176 | At least two affected OLD base boundaries after prepared high Z(U OR V), in the exact two-visible frame, give tau(G)<=K+2 for arbitrary q,K. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-177 | The exact one-affected-old-boundary prepared high at zero cross gives tau(G)<=K+2 for arbitrary retainedK on the four-global-missing induced path-plus-two-edges target. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-178 | The exact single-affected-old-boundary prepared high with positive cross cannot witness induced H-empty P3+2K2; other global missing edges allowed. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-179 | A shared raw-linear-preparation exact template has at most7 positive clauses and cannot witness induced H-empty P3+2K2. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-180 | Two distinct earlier g insertions affecting both inputs of a common product, with third high hC or h(C OR g), cannot witness the four induced path-plus-two-edge targets. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-181 | With at most3 deleted products and3 additions, exactly one visible cut and at least4 global missing edges, every H-independent induced graph has at most7 maximal independent sets. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-182 | The exact three-visible literal old/raw highs u=AB,t=uC,v=DE, one occurrence each, give tau(G)<=K+2 for the four-global-missing induced P3+2K2 target. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-183 | An exact shared-first-cut/both-affected-second-high/raw-third-multiplier three-visible template cannot safely witness induced global missing P3+2K2. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-184 | A Boolean linear first high with at least one affected factor among three second-high clauses gives at most7 positive clauses, excluding induced H-empty P3+2K2 in that exact frame. | 4 | proved; complete separate proof and full mutual comparison; inserted |
| SZ4-185 | The exact nested both-affected three-visible original template cannot safely witness all four induced P3+2K2 missing edges. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-186 | Two independent earlier cuts entering both sides of a join give vc(G)<=K+2 in the exact three-visible original frame; contexts linear or zero. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-187 | Prepared first high AB(U OR V), with at least one affected old base in the second high, gives vc(G)<=K+2 in the exact two-visible frame. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-188 | A three-clause first high with one old factor and an affected two-factor second high gives vc(G)<=K+2, retaining actual low/context identities. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-189 | Every literal old/raw original private network with at most3 products and3 visible additions on the induced four-missing P3+2K2 target satisfies vc(G)<=K+2. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-190 | In the original at-most3-product/3-addition two-visible path target, a sole hidden old-linear preparation ancestral to the first high gives vc(G)<=K+2 after exact whole-carrier erasure. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-191 | An old-product first high with at most3 factors and a later union of old linear forms cannot supply the four induced path-plus-two-edge missing witnesses in the exact bounded two-visible template. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-192 | For the exact original three-occurrence path target g=UV, h=(A OR g)(B OR g), f=h(C OR lambda*g OR mu*h), a safe contribution with all actual low/context identities cannot witness all four missing edges, for every nonnegative coefficient and compatible scalar/zero context. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-193 | The exact hidden quadratic join g=UV,h=AB,f=Z(g OR h) cannot supply four induced H-empty P3+2K2 missing witnesses; original two-visible scope retained. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-194 | The exact unaffected-later-preparation f=S(B OR g), with g at most3 old factors and S a linear old-form union, gives vc(G)<=K+2. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-195 | The exact raw-quadratic hidden preparation f=AB(C OR UV) cannot safely supply the four induced path-plus-two-edge missing witnesses; no hidden normalization is asserted. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-196 | A25-gate C4-free original literal mixed circuit has14 old edges,4 missing P3+2K2 edges,K=vc(H)=6,vc(G)=8,and exactly3 deleted products/3 visible additions; scoped K+2 bound sharp. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-197 | In the all-visible at-most3-product/3-addition path target, all original private gates survive erasure; highs are original products, operands are raw products or old linear plus earlier original occurrences, and original ancestry survives. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-198 | The exact hidden quadratic-join first high UV OR WX with at least one affected old base in the later product gives vc(G)<=K+2. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-199 | An unaffected first hidden join of original old quadratics with an old-quadratic second high gives vc(G)<=K+2. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-200 | The original at-most3-product/3-addition two-visible profile whose first high is the sole hidden join of two original old quadratic products has vc(G)<=K+2, with second high unrestricted within the budget. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-201 | A first hidden join with all original private operands old or raw can be formally reassociated into three visible cuts preserving the full output and retained K, yielding vc(G)<=K+2. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-202 | A safe Q OR UV(L OR F), with Q at most4 old factors and F a subproduct of at most3 listed Q factor occurrences, cannot witness all four induced H-empty P3+2K2 missing edges. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-203 | An independent quadratic inside the later preparation f=Z(C OR AB), with first high UV and exact two-visible contexts, gives vc(G)<=K+2. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-204 | For the exact original three-occurrence path frame g=UV,h=(A OR g)B,f=h(C OR lambda*g OR mu*h), safety and four global missing witnesses imply vc(G)<=K+2 for arbitrary retained K and all actual degree/low/context identities. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-205 | The exact later preparation f=Z(C OR AB OR UV), retaining an old quadratic lower-support part and original frame, gives vc(G)<=K+2. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-206 | In the original at-most3-product/3-addition two-visible path target, the sole hidden sum of original private-product outputs itself being the first visible high gives vc(G)<=K+2, including repeated and comparable inputs. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-207 | For the exact original three-visible path frame g=UV, h=gA and f=(B OR epsilon*g OR delta*h)(C OR epsilon2*g OR delta2*h), safety and four global missing witnesses imply vc(G)<=K+2 for arbitrary retained count K, with all actual low/context identities. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-208 | For the exact original two-visible path frame g=UV and f=(A OR alpha*g)(B OR beta*g)((C OR D) OR gamma*g), at least one affected factor, safety and four global missing witnesses imply vc(G)<=K+2 with all actual common-low/context identities and arbitrary retained K. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-209 | The exact raw shared quadratic ancestor after an unequal preparation g=Z(C OR u), f=u(A OR epsilon g), gives vc(G)<=K+2 for all cross choices. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-210 | The exact original three-visible g=UV,h=WX,f=g(C OR h) configuration has vc(G)<=K+2 for arbitrary retained K. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-211 | For the exact original all-visible p<=3/a<=3 induced P3+2K2 four-global-missing frame with vc(G)>K+2, p=a=3. Three distinct highs have no raw operands and exactly the stated necessary affected-type table; two distinct highs are comparable and the uninserted product has exactly R1/R2/R3, retaining all occurrence coefficients and the common-singleton index restriction when both R3 inputs are affected. Every private product satisfies214; no realization or numerical closure is asserted. | 4 | proved; full separate derivation and qualified mutual comparison; explicit post-author local count correction4-to6 preserved; inserted |
| SZ4-212 | In the minimum-product gain3 three-matching attachment profile with three private products and additions, an original deleted1+1 addition forces a unique crossing center whose full old outside leaf support is a nonempty partial matching transversal, containing the mate when the attachment is matched; no other center has such a support. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-213 | In the exact original p3/a3 two-visible induced path frame, vc(G)>K+2 forces the sole hidden addition to be an unequal degree-one/raw-product sum, or exactly the second high with degree-one selected low and no other use, admitting an exact reassociation preserving the current erased/pruned polynomial, frame and K. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-214 | With exactly three original private products, zeroing any one at every original use preserves the entire selected quadratic frame but loses a witness in every induced three-matching restriction with zero quadratic support; on the path target each product is true on an isolated edge or both path arms, without distinct-witness or first-true claims. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-215 | In the exact original p3/a3 two-visible induced path frame, a hidden unequal preparation and first high with literal actual inputs u=UV,S=C+u,g=SZ and nonzero old homogeneous linear U,V,C,Z force vc(G)<=K+2 for arbitrary retained K, with no further restriction on the third product or second high. | 4 | proved; complete separate derivation and full mutual comparison; inserted |
| SZ4-216 | For N=3K2 or P3+2K2, u=UV,s=C OR u, and f the product of two operands u,s or A OR alpha*s, the expression sL OR fM OR qsf cannot equal the edge function, with arbitrary affine L,M and all zero/repeated cases. Consequently the exact original p3/a3 two-visible literal u=UV,S=C+u,first high g=S*S branch is impossible after whole-current-carrier erasure, with arbitrary third product/second high and no K bound; no other hidden normalization claimed. | 4 | proved; full separate derivation and qualified mutual comparison; squarefree-P2 explanation disclosed post-fresh; inserted |
| SZ4-217 | For exact original p3/a3, two visible cuts, literal old u=UV,S=C+u and first high g=Su or g=u*u, no circuit can realize an H-empty induced3K2 or P3+2K2 target. Full actual third-product/second-high input census, degree-two first selected low, affine contexts, raw fanout and squares are included; arbitrary retained counts and no other hidden normalization. | 4 | proved; complete separate fresh derivation and full mutual comparison; inserted |
| SZ4-218 | For exact original p3/a3, two visible cuts, literal old u=UV,S=C+u and first high g=uA on four global missing edges inducing P3+2K2 with H[T] empty, no circuit exists for arbitrary K. The third product/second high and relative S/first-cut order are initially unrestricted; complete original census and all actual contexts are proved. This is the stronger impossibility statement; original weaker cover-bound proof is preserved. | 4 | proved; complete separate fresh derivation and full mutual comparison; inserted |
| SZ4-219 | For the exact original all-visible p3/a3 literal R2 family g=UV,u=AB independent,f=u(C+sum delta_i g_i),with n=1or2 original g occurrences and3-n f occurrences,on four global missing edges inducing P3+2K2 with H[T] empty,vc(G)<=K+2 for arbitrary K. Both highs must be T-unsafe,all selected lows degree1,same-high pair coefficients0;positive mixed coefficient and n=2 are impossible. The remaining n=1/q=0 allocation has a full original-context cover charge. No other operand normalization or numerical-row closure. | 4 | proved; complete separate pre-author proof and full mutual comparison; inserted |
| SZ4-220 | For the exact original p3/a3/two-visible induced P3+2K2 four-global-missing frame, literal u=UV,S=C+u,g=AB with old nonzero homogeneous linear factors and independent original old-quadratic first high g implies vc(G)<=K+2 for arbitrary retained K. The initially unrestricted third product is the second high and has exactly Su,Sg,S^2,or S(D+alpha g) as its surviving literal inputs,with all original identities,degrees,fanout,selected lows and context coefficients retained. Raw alternatives are impossible; the nonraw alternatives satisfy the full original-product cover charge. No other unequal preparation or saving-row closure is asserted. | 4 | proved; complete separate pre-author derivation and full mutual comparison; full proof inserted |
| SZ4-221 | The exact original all-visible p3/a3 R1 network u=UV,g=uA,f=(B+sum beta_i g_i)(C+sum gamma_i g_i),with both coefficient sums positive,n=1or2 actual g occurrences and3-n f occurrences,cannot supply the four global missing witnesses inducing P3+2K2 with H[T] empty. All scalar/zero contexts,actual same/mixed occurrence coefficients and original degrees/fanout are preserved; arbitrary K. Single-affected R1 and other networks remain outside this impossibility. | 4 | proved; complete pre-author separate derivation and full mutual comparison; pre-author wording clarification preserved; inserted |
| SZ4-222 | The exact original p3/a3/two-visible induced P3+2K2 four-global-missing family with literal old u=UV,S=C+u and first chronological visible high the original source u itself is impossible for arbitrary retained K. The two remaining products and second high are initially unrestricted; their connected product/high/input inventory is derived, preserving every original node,minimum degree,wire repetition,coefficient,fanout,selected low and context. No ordering of S beyond the actual DAG or longer-raw-input/general unequal-hidden classification is assumed. | 4 | proved; complete pre-author separate derivation and full mutual comparison; full proof inserted |
| SZ4-223 | For the exact original p3/a3/two-visible induced P3+2K2 four-global-missing frame with sole hidden literal u=UV,S=C+u and full nonzero old homogeneous linear U,V,C, vc(G)<=K+2 for arbitrary retained K. Both visible highs and the two other private products are initially unrestricted. The original first-high/remaining-product/high-boundary census is derived with all minimum degrees,full carriers,fanout,repetitions,coefficients,lows and contexts fixed. No longer raw input,affected C or general hidden normalization is claimed. | 4 | proved; complete separate proof and full mutual comparison with exact disclosed precision history; full proof inserted |
| SZ4-224 | For the exact original all-visible p3/a3 induced P3+2K2 four-global-missing family u=UV,g=uA,f=C(B+sum beta_i g_i), with full old factors,one affected final input,n=1or2 actual g occurrences and3-n f occurrences,vc(G)<=K+2 for arbitrary retained K. All original minimum degrees,occurrences,lows,context coefficients,fanout and retained-product incidences are preserved. Together with221 this removes all R1 from the gain-three minimum-retained row; nonraw three-high table,R3 and other numerical cases remain outside this claim. | 4 | proved; complete separate pre-author derivation and full mutual comparison; full proof inserted |
| SZ4-225 | For the exact original p3/a3/two-visible induced P3+2K2 four-global-missing frame, let the sole hidden sum be S=R+u, u=UV with full unaffected old homogeneous linear U,V, and actual degree-one R=C+beta*g, beta>0, where g is the first visible high and C its nonzero old selected part, not necessarily an available wire. With both highs and the other products initially unrestricted, vc(G)<=K+2 for arbitrary retained K. All original minimum degrees, occurrences, coefficients, fanout, lows, contexts and retained-product incidences are preserved. Longer or affected raw sources and other hidden placements are not normalized. | 4 | proved; complete separate pre-author derivation and full mutual comparison; full proof inserted |
| SZ4-226 | For the exact original all-visible p3/a3 induced P3+2K2 four-global-missing R3 family g=UV,u=(A+sum beta_i*g_i)(B+sum gamma_i*g_i),f=u(C+sum delta_i*g_i), with full old nonzero linear factors,n=1or2 actual g occurrences and3-n actual f occurrences,and no u insertion,vc(G)<=K+2 for arbitrary retained K. At least one middle input is affected; if both are affected,their positive index sets are the same singleton. All actual temporal restrictions,minimum degrees,coefficients,squares,crosses,lows,contexts,fanout and original retained-product incidences remain fixed. Together with219/221/224 this excludes all repeated-high alternatives of211,leaving the nonraw three-distinct-high table and other hidden/matching cases open. | 4 | proved; complete separate pre-author derivation and full mutual comparison; full proof inserted |
| SZ4-227 | For the exact original p3/a3/two-visible induced P3+2K2 four-global-missing frame, suppose the sole hidden addition has literal inputs S=R+u with actual retained degree-one boundary R=C+beta*g,beta>0,first visible high g,and nonzero full old selected part C not necessarily available as a wire. The source u is any raw original private-product output with initially unrestricted inputs,minimum degree and ancestry. Then vc(G)<=K+2 for arbitrary retained K. Every original node,degree,occurrence,coefficient,fanout,low,context and retained-product incidence is preserved. The unaffected-input case with a longer/affected raw source,remaining all-visible types and matching attachments are not classified. | 4 | proved; complete separate pre-author derivation and full mutual comparison; full proof inserted |
| SZ4-228 | In the exact original three-private-product/three-private-addition frame with two visible cuts, four global missing edges inducing P3+2K2 and nonempty H with H[T] empty, let the sole hidden addition have literal inputs S=C+u, where C is an actual full unaffected nonzero old homogeneous linear input wire and u is a raw private-product output of original minimum degree at least two. If u is a proper surviving original descendant of the first visible high g, then vc(G)<=K+2 for the arbitrary original retained product count K. All original node/input/insertion identities, minimum degrees, coefficients, fanout, lows, full contexts and retained-product incidences are preserved. Source inputs and the second high are initially unrestricted; either possible actual order of the first insertion and S is allowed. No retained optimality, Boolean-identity wire replacement, or numerical-row closure is inferred. | 4 | proved; complete separate pre-exposure author/checker proofs and entire readbacks; full mutual comparison PASS; full author proof inserted |
| SZ4-229 | In the exact original three-private-product/three-private-addition frame with two visible cuts, four global missing edges inducing P3+2K2 and nonempty H with H[T] empty, let the sole hidden addition have literal inputs S=C+u, with C an actual full unaffected nonzero old homogeneous linear input wire and u a raw original private-product output. If the first visible high is the SAME ORIGINAL product node u, then vc(G)<=K+2 for arbitrary original retained K. The source inputs, minimum degree, ancestors and second high are initially unrestricted; no order between the first insertion and S is imposed. All original nodes/occurrences, minimum degrees, coefficients, fanout, lows, full contexts and retained-product incidences, including scalar/zero cases and repeated inputs, stay fixed. The old-quadratic case invokes223 only after its literal original-input hypotheses hold. No228 dependency or numerical-row closure is claimed. | 4 | proved; complete separate pre-exposure author/checker proofs and entire readbacks; full mutual comparison PASS; full author proof inserted |
| SZ4-230 | In the exact original three-private-product/three-private-addition frame with two visible cuts, four global missing edges inducing P3+2K2 and nonempty H with H[T] empty, let the sole hidden addition have literal inputs S=C+u, where C is an actual full unaffected nonzero old homogeneous linear input wire and u is any raw original private-product output of original minimum degree at least two. Then vc(G)<=K+2 for the arbitrary original retained product count K. Source inputs, minimum degree, ancestry and first/second-high identities are initially unrestricted. All original nodes, operand and insertion occurrences, coefficients, fanout, selected lows, full contexts and retained-product incidences are preserved, including repeated inputs and scalar/zero context cases. The old-quadratic, same-first-high and proper-descendant theorems are applied only at their exact original-input hypotheses; every other source relation is covered by the complete original-node inventory. No retained optimality, Boolean-support wire replacement, all-visible normalization, matching-attachment or numerical-row closure is inferred. | 4 | proved; complete separate pre-exposure author/checker proofs and entire readbacks; full mutual comparison PASS; full author proof inserted |
| SZ4-231 | For a positive variable-input circuit on finite simple C4-free G, with nonempty squarefree quadratic support H and exactly four GLOBAL missing edges xy,xz,ab,cd inducing H-empty P3 disjoint2K2, keep the exact original selected quadratic frame and arbitrary retained multiplication count K. If canonical extraction/pruning deletes exactly three ORIGINAL multiplication nodes and three ORIGINAL addition nodes, all additions visible, then vc(G)<=K+2. All original ancestry, raw/affected operands, minimum degrees, repeated high values or high nodes across distinct insertion occurrences, compatible scalar/zero contexts, actual cross coefficients, full lows/paths/contexts and retained-product incidences are initially unrestricted and preserved. Boolean support identities create no wire, identify no original node and change no original degree or counted gate. This proves the whole all-visible path-target family, not hidden additions, matching attachments, other outside shapes, empty H or the unrestricted numerical row. Combined with admitted232 in the saving row, it excludes the path outside shape; three-matching attachments remain open. | 4 | proved; Separate complete author/fresh proofs and ENTIRE readbacks preceded same-claim exchange; both full comparisons and entire comparison readbacks PASS. Checker complete v2 used admitted<=229 only; later233/234/235 clean-statement reads were comparison-phase exposures. Author used admitted233/234/235 and full inline row proofs; no236 proof dependency. Part D transcription clarifies minimum-degree-two, already correct in Part A; original proofs unchanged and no mathematical repair. No new230 proof route used. Complete original-author-route statement and proof inserted; final source/page QA separately recorded. |
| SZ4-232 | In the exact original three-private-product/three-private-addition frame with two visible cuts, four GLOBAL missing edges inducing P3+2K2 and nonempty H with H[T] empty, arbitrary retained K and the stipulated whole-current-carrier-erased/pruned polynomial P*, if vc(G)>K+2 then the unique hidden addition is the single-use second visible high S=u+v with raw private-product operands and original degree-one selected low a. The exact arithmetic reassociation a+(u+v)=(a+u)+v gives an all-visible circuit with the same P*,quadratic frame,H,K and product nodes; two additions replace two additions. The original first high,u,v remain distinct insertion occurrences even when nodes or Boolean values coincide. Equivalently either vc(G)<=K+2 or this exact all-visible representative exists. No retained optimality, identity of addition DAGs, equality to the unerased higher polynomial, all-visible/matching/numerical closure is inferred. This checked synthesis of213/227/230 earns no additional mathematical-movement credit beyond actual review30. | 4 | proved; complete separate pre-exposure proofs and entire readbacks; full mutual comparison PASS; complete corollary proof inserted; no additional mathematical movement |
| SZ4-233 | For a positive variable-input circuit on finite simple C4-free G with nonempty squarefree quadratic support H, exactly four GLOBAL missing edges xy,xz,ab,cd inducing P3+2K2 on T with H[T] empty, a fixed original selected frame with arbitrary K retained products, exactly three deleted original products and three visible deleted additions, three distinct product highs inserted once apiece, and every private operand of original minimum degree one with nonzero old homogeneous base plus compatible earlier insertions: (A) each actual private-product value is true on at least two distinct target edge assignments, with no unique/first-true or injective allocation claim. (B) If all original pairwise occurrence coefficients are zero, vc(G)<=K+2 for the exact patterns g=UV and (h,f) equal (AB,(C OR g)D), (AB,D(C OR g OR h)), (AB,(C OR g)(D OR g)), (AB,(C OR g)(D OR g OR h)), ((A OR g)B,CD), ((A OR g)(B OR g),CD), or ((A OR g)(B OR g),(C OR g)D). All old forms are full nonzero homogeneous forms and may repeat; coefficients, original nodes/degrees/occurrences, selected lows, fanout, full contexts and retained incidences remain fixed. No other cell, positive-cross allocation, full231 or numerical-row closure is inferred. | 4 | proved; complete separate pre-exposure proofs and ENTIRE readbacks; both full comparisons PASS without repair; full theorem/proof inserted; source/page QA separately recorded |
| SZ4-234 | For a positive variable-input circuit on a finite simple C4-free G with nonempty ordinary squarefree quadratic support H, exactly four GLOBAL missing edges xy,xz,ab,cd inducing H-empty P3 disjoint2K2 on T, a fixed original selected frame with arbitrary retained-product count K, exactly three original private products and three visible private additions, three distinct product highs inserted once each, and every original private-product input of minimum degree one with nonzero old homogeneous base plus compatible earlier original insertion contributions: (A) all three original high Boolean functions are globally unsafe on G, each true on a G-independent assignment. (B) If any original high v_k implies both v_i and v_j for distinct insertion occurrences i,j, the actual pair coefficient q_ij is zero; k may equal i or j. Neither A nor B assumes vc(G)>K+2. (C) The entire double/split cell g=UV, h=(A OR g)(B OR g), f=(C OR g)(D OR h OR epsilon*g), epsilon0/1 with all actual q initially unrestricted, satisfies vc(G)<=K+2. All full old forms, original nodes/degrees/cuts/coefficients/lows/paths/fanout/contexts and retained incidences remain fixed; support absorption changes no counted gate. The auxiliary proof openly changes its own H to H-prime; only the final cover proof charges the original K. No full231, other row, matching-attachment or numerical closure. | 4 | proved; Complete separate author/fresh proofs and ENTIRE readbacks preceded author exchange; both full comparisons PASS without repair. Admitted233 background disclosed. A/B have no cover inequality; complete original C proof retained. Complete author-route statement/proof inserted; source/page QA separately recorded. |
| SZ4-235 | For a positive variable-input circuit on a finite simple C4-free G with nonempty ordinary squarefree quadratic support H, exactly four GLOBAL missing edges xy,xz,ab,cd inducing H-empty P3 disjoint2K2 on T, a fixed original selected frame with arbitrary retained-product count K, exactly three original private products and three visible private additions, three distinct product highs inserted once each, and every original private-product input of minimum degree one with nonzero old homogeneous base plus compatible earlier original insertion contributions: The entire double-affected-middle row h=(A OR g)(B OR g), g=UV, satisfies vc(G)<=K+2 for all four exact last-product cells f=CD, (C OR g)D, C(D OR h OR epsilon*g), (C OR g)(D OR h OR epsilon*g), epsilon0/1. Every actual q12,q13,q23 is initially unrestricted. All full nonzero old forms may repeat; actual affected-boundary, degree, low/context, coefficient, occurrence, fanout and original retained-product incidences remain fixed. Optional g coefficients remain recorded despite Boolean absorption. The proof uses admitted233 exact necessity and old-factor/context facts, not234 or230. Only this entire middle row is removed; independent/single-affected rows, matching attachments, full231 and the numerical saving row remain open. | 4 | proved; Complete separate author/root proofs and ENTIRE readbacks preceded235 author exchange; both full comparisons PASS without repair. Limited related234 strategy-label exposure was disclosed and not used; no pristine isolation from every related hint is claimed. Neither234 nor230 is a proof premise. Complete author-route statement/proof inserted; source/page QA separately recorded. |
| SZ4-236 | For the exact original three-private-product/three-private-addition all-visible frame on a finite simple C4-free G with nonempty H and exactly four GLOBAL missing edges xy,xz,ab,cd inducing H-empty P3 disjoint2K2, arbitrary retained-product count K, three distinct original product highs inserted once each and minimum-degree-one original product inputs, let independent old quadratics g=UV,h=AB precede f of type OG,OJ,GG,GH or GJ: (C OR g)D, D(C OR g OR h), (C OR g)(D OR g), (C OR g)(D OR h), or (C OR g)(D OR g OR h). With every actual q12,q13,q23 initially unrestricted, full contribution gL OR hN OR fM OR q12gh OR q13gf OR q23hf safe and supplying all four witnesses implies vc(G)<=K+2. All full old bases, original nodes/degrees/occurrences/coefficients/lows/paths/fanout/contexts and retained incidences remain fixed; old bases need not be standalone wires. This independently excludes the entire independent-middle row, not the single-middle, matching or unrestricted numerical family. | 4 | proved; Separate complete operator author and foundation fresh proofs and ENTIRE readbacks preceded exchange; both full comparisons and entire readbacks PASS without repair. Foundation pre-author partial correction is preserved. Root236 attempt remains explicitly INCOMPLETE partial and receives no complete fresh-proof credit; root acted as editor only. No231 premise. Complete original-author-route statement and proof inserted; final source/page QA separately recorded. |
| SZ5-cor-hecke-word-localization | A nonzero ambient coordinate minor of a rational word basis certifies a localization of the integral Hecke word order that is free on those words. | 5 | proved; separate statement-only proof and targeted comparison recorded |
| SZ5-lem-positive | The first two displayed dimension tables have nonnegative Laurent coefficients, dominate the trace coefficientwise in absolute value, and agree with it modulo two. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-lem-table | The displayed scalar and two-by-two matrix realization gives the complete rank-three product table through word-reduction exponents and the three bottom polynomials. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-bottom-shift-obstruction | For dimension algebras B and C, arbitrary additions of the old bottom vector to every cell vector and an arbitrary complementary bottom vector force at least one upper and one lower bottom supported-zero weight in any effective transformed table. | 5 | proved; independently derived same-sign obstruction and checked two-extreme consequence |
| SZ5-prop-character-support | Prescribed class functions at present grades come from unique genuine finite-group representations exactly when all irreducible character multiplicities are nonnegative integers, and all zero-adjoined character evaluations together are injective. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-class-collapse | Allowing the old zero as an ideal-class multiplier collapses every nontrivial ideal class, while restriction to nonzero fraction-field multipliers recovers the ordinary fractional ideal class semigroup. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-cover-local-system | Monomial rank-n local systems are equivalent to degree-n finite covering local systems equipped with a rank-one local system, yielding the split-complex interpretation and cycle-factorized determinants. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-criterion | An effective associative sign-Tate structure with prescribed trace exists for a dimension table exactly when that table is associative, coefficientwise dominant in absolute value, parity-compatible, and has the prescribed strict unit. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-fixed-diagram-obstruction | No fixed finite family of endomorphisms, even with arbitrary word-dependent inserted operators and an added constant line, can realize all sequences c(q^n+2+q^(−n))^k with c nonzero and q>1. | 5 | proved; separate statement-only proof and explicit inserted-trace qualification |
| SZ5-prop-height-neutrality | A weighted adelic height descends to projective space exactly when its logarithmic defect vanishes, while trivial places are neutral and the three metric states form the stated incidence chain. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-initial-data | Support, valuation and initial graded class do not determine a valued element, as witnessed by t and t+t^2 in a Laurent-series field. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-lattice-cycles | For a nonzero ring the lattice extension has monomial invertible matrices, while determinant, characteristic and trace-word supports are the corresponding lattice joins of matchings and cycle or walk products. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-lattice-profiles | Unimodular vectors over a finite bounded-distributive-lattice coefficient extension have the stated support-profile classification and finite-field orbit count ((q+ell-1)^N-ell^N)/(q-1). | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-matrix-higgs-support | For arbitrary matrix Higgs data on a monomially presented vector bundle, split characteristic coefficients glue as sections of the appropriate split tensor powers and distinguish absence from supported cancellation. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-points | Unimodular coordinate vectors over a zero-adjoined finite field modulo common units have count ((q+1)^(n+1)-2^(n+1))/(q-1), with the stated positive Tate expansion. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-poles | A finite graded trace-of-powers sequence has a rational generating function with only simple nonzero poles, excluding a fixed Frobenius interpretation of a Hilbert series with a pole of order at least two. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-rank4-word-minor | The displayed114 Hecke words and coordinate rows define a nonzero determinant norm in Z[D] for which the rank-four word order is free after localization. | 5 | proved from specified primary dimension with independently recomputed nonvanishing certificate |
| SZ5-prop-rees-support-quotient | The multiplicative Rees quotient of M times the Boolean monoid by M times its zero is exactly the monoid M with one new absorber. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-rescaling-obstruction | None of the five constructed dimension algebras can acquire the fixed exact bottom supports by fixing the unit, individually rescaling the cell basis vectors over Q(q), and arbitrarily replacing the complementary bottom basis vector. | 5 | proved; independent foundation derivation before operator proof |
| SZ5-prop-semimodule | The underlying semimodule of each rank-three lift is the finite-support semilattice diagram U maps to Z^U, with extension-by-zero transport and scalar convolution. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-split-torsor | A simply transitive W-set with two adjoined fixed points has action groupoid equivalent to two copies of BW and one terminal groupoid, with the corresponding product support map. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-unimodality | The displayed rank-three coefficient in Mulmuley's Figure 2 has positive factor with coefficients (1,1,3,2,3,1,1), refuting its asserted unimodality under that normalization. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-valuations | A unital subsemiring of K0 containing both zero states and at least one of each nonzero inverse pair is exactly a zero-adjoined valuation ring, with the stated classification for Q. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-prop-zero-bottom-tradeoff | Every associative strict-unit rank-three support lift with exact bottom trace supports has at least sixteen nonbottom supported-zero weights in the eight ordered first-cell/bottom products, and any effective refinement has at least sixteen corresponding cancelling pairs. | 5 | proved; independent check and proof exposure recorded separately |
| SZ5-thm-adeles-main | The restricted product of zero-adjoined rational completions is the pair semiring of adelic amplitudes and arbitrary place supports, its units are the ideles, and a support satisfies the rational product formula only when empty or full. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-thm-bottom-main | Under the stated rank-three trace coefficients and preservation of the bottom ideal, associativity forces the bottom coefficient support to reach exponents at least 3 and at most -3, producing at least two supported-zero weights. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-thm-global-weights | For every global field, an arbitrary real family of weights annihilates all normalized principal logarithms if and only if it is constant on the standard places. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-thm-hecke-word-descent | For every rank, the nonstandard Hecke generator word span is a finite torsion-free Z[D]-order whose Laurent scalar extension is faithful, whose rational word coefficients descend to Q(D), and whose regular characteristic polynomials lie in Z[D]. | 5 | proved; separate statement-only proof and targeted comparison recorded |
| SZ5-thm-lifts-main | The five displayed effective associative rank-three lifts have the independently verified zero-weight and cancellation counts, including a 38-zero-weight lift and a wholly unimodal 42-zero-weight lift. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-thm-measured-defect | The measured logarithmic defect is a Boolean valuation extending to a linear transform with the stated nondegenerate quotient pairing, and localization at full zero amplitude leaves the measured Boolean support algebra. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-thm-minimal-basis-rank-main | Three is the least strict-unit free basis rank at which an associative algebra over the zero-adjoined Laurent semiring can fail to lift to the effective sign-Tate semiring. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-thm-no-bottom-main | The specified ten-element rank-three trace basis admits an associative strict-unit inverse-semiring lift with exact bottom trace supports and no bottom supported-zero weights, at the cost of losing the bottom-ideal property. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZ5-thm-nonliftable-main | The same rank-three trace algebra admits an associative support lift whose output relation has no associative assignment of positive finite real multiplicities and hence no effective sign-Tate refinement. | 5 | proved in stated framework; check coverage and proof exposure recorded separately |
| SZG-Deitmar-correction | The proposed single Euler factor for the full multiplicative monoid of Z_0 is not Deitmar's finite-type zeta construction. | 2 | refuted, with refined statement SZ2-prop-deitmar |
| SZG-UFS-correction | The old zero of Z_0 cannot be factored into its signed-prime irreducibles, refuting unique factorization when that requirement includes every non-new-zero nonunit. | 1 | refuted, with refined statement SZG-factorization |
| SZG-additive-noncancellation | The additive monoid of every R_0 is noncancellative because adding the old zero identifies its two distinct additive idempotents. | 1 | proved or reduced to an already checked statement |
| SZG-adele-embedding-correction | The full-support copy of the adele ring preserves addition and multiplication but not the semiring zero, whereas its zero adjunction embeds as a unital zero-preserving semiring. | 5 | refuted as a zero-preserving semiring embedding; corrected form proved |
| SZG-adjunction-correction | Zero adjunction is not a left adjoint to the inclusion of rings into semirings; its valid unit-fiber adjunction is the one specified by FGJM's constructions. | 1 | refuted, with refined statement prop:unitfiberadjunction |
| SZG-associates | Two elements of Z_0 generate the same principal ideal if and only if they differ by multiplication by an old unit. | 1 | proved by direct cases |
| SZG-augmentation | The augmentation of the contracted monoid algebra sends each old monoid basis element to one and is projection onto the central-idempotent Z factor. | 2 | proved by multiplying with the old-zero basis idempotent |
| SZG-blueprint | The canonical blueprint of R_0 retains its new zero and the additive relations of R, while identifying the two zeros recovers the canonical blueprint of R. | 1 | proved after contraction and canonical-semiring convention |
| SZG-boolean | The two-zero pair is the Boolean semiring with unit the old zero, and differs from the two-element field because its addition is idempotent. | 1 | proved or reduced to an already checked statement |
| SZG-boolean-base | The contracted integral monoid algebra of the multiplicative Boolean monoid is Z. | 2 | proved by its one nonzero monoid generator |
| SZG-boolean-unit-correction | The two-element pair consisting of the two zeros has multiplicative unit equal to the old zero, so its claimed absence of a unit is false. | 1 | refuted, with refined statement SZG-boolean |
| SZG-cancellation-correction | The old zero is not a cancellative multiplier in Z_0, so cancellation by every element other than the new zero is false. | 1 | refuted, with refined statement SZG-cancellative |
| SZG-dimension | For a nonzero ring of finite Krull dimension, zero adjunction increases Krull dimension by one. | 1 | proved with the nonzero-ring convention |
| SZG-divisibility | Divisibility among old nonzero integers in Z_0 is ordinary integer divisibility, every element divides the new zero, and the old zero divides precisely the two zeros. | 1 | proved by direct cases; manuscript integration in progress |
| SZG-evaluation | Evaluation of an old integer monoid basis element at that integer gives a surjective ring map from the contracted monoid algebra to Z distinct from augmentation. | 2 | proved directly on basis products |
| SZG-factorization | The old zero of Z_0 has no finite factorization into irreducibles, so a factorization convention requiring such a factorization for every non-new-zero nonunit fails. | 1 | proved with explicit factorization convention |
| SZG-fraction-conventions | Inverting every old element of R_0 identifies all of them with the unit and gives the Boolean semifield, whereas inverting only regular elements of a domain gives its fraction field with a new zero. | 1 | proved; monoid and semiring conventions distinguished |
| SZG-ideal-zeta | The Bourne-quotient norm series of the nonzero ideals of the zero-adjoined ring of integers is the ordinary Dedekind zeta function. | 2 | proved after specifying the quotient norm |
| SZG-idempotents | The additive idempotents of R_0 are the new zero and the old zero, while its multiplicative idempotents are the new zero and the old ring idempotents. | 1 | proved or reduced to an already checked statement |
| SZG-monoid-Noetherian-correction | The infinitely generated free commutative prime monoid and the multiplicative monoid of Z fail the ascending-chain condition on ideals. | 2 | refuted, with refined statement SZ2-prop-monoid-spectrum |
| SZG-monoid-base-correction | Base change of the multiplicative monoid of Z_0 gives Z times an infinite polynomial group algebra, not Z. | 2 | refuted, with refined statement SZ2-prop-deitmar |
| SZG-monoid-ideals | Multiplicative monoid ideals of Z are upward closed for divisibility and need not be principal, while the positive integers form the free commutative monoid on the primes. | 2 | proved by unique factorization |
| SZG-monoid-integral | The pointed multiplicative monoid of Z_0 has no product of old elements equal to the new absorber, but is not cancellative because of its old zero. | 2 | translated with qualification |
| SZG-monoid-spectrum-correction | The monoid spectrum of Z_0 is neither one-dimensional nor homeomorphic to its two-dimensional semiring spectrum. | 2 | refuted, with refined statement SZ2-prop-monoid-spectrum |
| SZG-not-Boolean-algebra | For a nonzero ring R there is no unital semiring homomorphism from the Boolean semifield to R_0, since its unit is not additively idempotent. | 1 | proved or reduced to an already checked statement |
| SZG-number-field-spectrum | The zero-adjoined integer ring of a number field has Krull dimension two and its Bourne-quotient norm series is the Dedekind zeta function. | 2 | proved; geometric component in Paper 1 prop:localization |
| SZG-presentation-correction | A monoid-semiring presentation of R_0 must contract the generator of the new zero to the empty sum; additive identity relations on nonempty sums alone are insufficient. | 1 | refuted, with refined statement in prop:contracted-presentation |
| SZG-prime-omission-correction | The old zero is divisibility-prime in Z_0, so the source list containing only the signed rational primes is incomplete. | 1 | refuted, with refined statement SZG-prime-elements |
| SZG-residue-monoid | The residue pointed monoid at the maximal monoid ideal of Z_0 is the two-element sign group with a zero adjoined. | 2 | proved by removing all nonunits |
| SZG-semifield-correction | Q_0 is not a semifield because its old zero is a non-new-zero nonunit. | 5 | refuted by the old zero |
| SZG-spectrum-reflection | The ring reflection Z_0 to Z induces the inclusion of the old closed Spec(Z) into Spec(Z_0), lowering its finite dimension from two to one. | 1 | proved or reduced to an already checked statement |
| SZG-topology | For Z_0 the closed sets are the whole spectrum, the old Spec(Z), finite sets of closed rational-prime points, and the empty set. | 1 | proved as the integer specialization |
| SZG-unit-action | Multiplication by units acts by automorphisms of the additive monoid of R_0 and is generally not a unital semiring automorphism. | 1 | proved or reduced to an already checked statement |
| SZG-units | The units of R_0 are precisely the units of R. | 1 | proved or reduced to an already checked statement |
| SZG-zero-ring-boundary | The units of R_0 agree with those of R, but absence of new-zero divisors also holds when R is the zero ring. | 1 | refuted, with refined statement SZ1-002 |