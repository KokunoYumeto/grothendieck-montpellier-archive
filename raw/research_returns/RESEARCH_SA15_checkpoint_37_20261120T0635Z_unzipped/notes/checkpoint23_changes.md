# Checkpoint 23 mathematical changes

This checkpoint is an incomplete research dossier. The credited producer is
GPT-6 Astra (OpenAI, ChatGPT Pro mode), and no priority is claimed. The original
manuscript scans remain unavailable; the supplied AI transcriptions are the
witnesses. Michel Hua's project has not been used.

## A.4: degree three on every fixed nonordinary principal surface

The complete system |9Θ| on every fixed principally polarized abelian surface
of two-rank zero or one in characteristic two now has geometric and arithmetic
monodromy GL80(F2) on its rank-eighty relative unit local system. This includes
every nonproduct surface, without a generic-modulus assumption. The previous
degree-one and all-product results remain in force.

The proof has several independently checked inputs. A nonordinary genus-two
curve cannot have a degree-three map with three distinct totally ramified
points. One proof is a direct normal-form calculation: an actual 3Q pencil
reduces two further total fibres to a separable quadratic remainder, and its
two roots force an affine singularity. A separate Galois-closure proof treats
the cyclic and S3 possibilities and computes a bijective Cartier operator in
both. Each has a universal polynomial certificate, independently rerun with
the original outputs preserved. The no-triple statement requires no isotropy
of a subgroup killed by three.

For such a subgroup, tangent identifications on the theta curve are excluded
by its canonical map and the two geometric two-torsion cases. Consequently
every individual theta norm is integral nodal, with exactly two nodes per
unordered nonzero type. A nonproduct polarized (3,3)-neighbour exists for
every nonproduct nonordinary target: in rank zero, Cartier excludes every
product quotient; in rank one, uniqueness of each elliptic type and the
principal-degree-one retraction argument show that at most one maximal
isotropic subgroup can give a product quotient.

The three eigensystems for a nonzero three-torsion translation descend to
ample (1,3) line bundles. A complete fixed-divisor argument excludes a base
curve, and the nine-point theta-kernel orbit contradicts the intersection
number six if a base point remains. Their morphisms are finite. The chord
incidence then gives two-transitivity of each eighteen-node cover. The theta
difference cover is quadratic in characteristic two; its reduced branch
support has class 2Θ and no nonzero odd translation stabilizer. Its isolated
shifted branches give transpositions in each node type separately, hence the
full product of four S18 factors.

The gluing proof retains the source boundary's stable-rank drop. A generic
splitting modulo the translation kernel is a section of a finite etale
Artin--Schreier torsor over a normal Lang scheme. It extends over every
component by finite birational normality. At each selected pair collision,
constant component torsors have common strict-henselian local trivializations,
so the inertia image is exactly the corresponding graph line, including in
the inseparable-residue case. The source graph relation produces a target
vertex-star vector with eight ones and ten zeroes in each type. The full node
permutation group then forces every type heart into the translation kernel.
The independently proved clopen-closure graph criterion gives irreducibility
and the full linear group.

These arguments establish multiplier three. No arbitrary odd-kernel theta
nodality or full image in every higher degree is inferred. The degree-two
and powers-of-three extensions under investigation are not treated as proved
unless their separate promoted proofs are explicitly included below.

## A.3: the primitive polarization reduction

For a mixed abelian surface, let a and b be the integral ordinary and
local-local polarization indices of an ample line bundle M. Over algebraic
closure it has an actual maximal root H^(2^r)=M, r=min(a,b), with indices
a-r,b-r. The proof uses the complete finite group scheme A[2^r], the fppf
quotient, torsionfreeness of Hom, and the full characteristic-two symmetric
homomorphism/line-bundle descent in AV Proposition 11.2 and Corollary 11.3.
Divisibility in Pic0 corrects the result to an actual line-bundle identity.

When 0<a<=b, this identifies |M^(3d)| with an even exponent in the previously
proved ordinary-index-zero case. The relative stable rank is therefore
9χ(M)d²-2 in every positive degree. Together with the a=0 theorem, this
strictly reduces the remaining mixed nonproduct case to primitive a>0,b=0.
The a=1 odd-degree sector was already exact. The actual root need not descend
to the original field; the conclusion concerns geometric generic rank.

The further restricted Petri statement is an exact equivalent test. It uses
the symmetric cup-wedge map on H1(Q-dual), restricted to the actual determinant
direction space. Its common radical vanishes exactly when an invertible
trace-zero variation exists. The annihilator is H1(KP)-dual, with the twist P
essential. No lower bound for that restricted map is asserted. In particular,
this equivalent reformulation is not counted as new mathematical movement.

## B.4: cyclic-level counterexamples beyond minimal ramification

The exact value ν_min(p,p-1,2)=1 for every p>=5 was proved after review 14 and
is now recorded in actual review 15. It covers both irreducible and reducible
residual inertia, including non-CM groups. The first-level counterexample
makes the p² recovery theorem sharp.

B62 supplies a separate new family. For p>=5, n>=2, h>=2, and every multiple
e of p-1 satisfying p^(2n-3)<e<p^(2n-2), there are actual height-h BT groups
with isomorphic p^n truncations and unequal prime-to-p special characters.
Thus ν_min(p,e,h)>=n. In particular e=2(p-1) has index at least two, and
e_n=p^(2n-3)+p-2 gives an unbounded sequence of lower bounds with p not dividing
e_n. No matching upper bound or exact next index is claimed.

The complete construction specializes the integral Hopkins--Gross formal
group with v1=u,v2=1, takes the exact iterated torsion equation on the arc
u=X^b, and obtains an Eisenstein DVR with a cyclic tame action fixing a marked
point of exact order p^n. A finite rank-one extension is lifted through every
level by Kummer theory, prime-to-p averaging and compatible cocycles. The
comparison group has a composition series with potentially good rank-one
graded pieces, precisely as the manuscript permits; its whole extension is
not claimed potentially good. The unequal trace is the explicit nonzero
product -(ζ-1)(ζ^p-1).

## Actual checks and retained finite computations

The root records in outputs/root_post_cp22_audits.json and
outputs/root_degree_three_and_b62_audits.json give the full assertion-by-
assertion proof and source checks, exact input hashes, and isolated rerun
outputs. Candidate files remain unchanged next to promoted canonical files.

- Root's direct trigonal program passed at 19:29:03.255153 UTC in
  0.07541732899699127 seconds, checking nine universal identities over F2.
  The independent OC rerun took 0.08843783400516259 seconds; the monodromy
  rerun took 0.07797064899932593 seconds.
- The Galois/Cartier certificate reconstructs the four Cartier columns,
  invariant basis, determinant and separability resultant. The author run
  took 0.06777819900162285 seconds; root's isolated run took
  0.06526876300631557 seconds; RD's took 0.055814325001847465 seconds.
- The degree-three graph program checks all 81 sum-zero translating triples
  of F3². It gives graph dimension 76, partial-normalization kernel 72,
  four-heart dimension 68, total heart span 75, type-constant constraint
  rank four and the eight-one/ten-zero star. Author, root and RD runtimes
  were 0.012680367006396409, 0.014382761997694615 and
  0.013090728003589902 seconds respectively.
- B62's certificate checks 15,556 arithmetic cases, 94,756 iterate weights,
  14,592 logarithm monomials, 40 directly recursively calculated
  multiplication coefficients, 24 character identities and 264 first
  thresholds. Its exact range is primes 5 through 101 and levels 2 through
  12, with all n=2 admissible e and the specified first/last/middle windows
  at larger levels. Direct coefficients through p² are checked for
  p=5,7,11,13. Author, root and OC runtimes were
  0.1291674740059534, 0.13728927899501286 and
  0.12315898900124012 seconds.

No finite calculation substitutes for the geometric, infinite formal-group,
or cocycle-lifting proofs. Every executed mathematical source and output,
including isolated rerun modifications, is retained. A packaging-only
JavaScript wrapper initially failed to parse while writing the consequence
promotion and review assessment. Its complete failed wrapper and error are
retained; the failure occurred before any file write, mathematical execution,
or actual review. The corrected wrapper succeeded.

## Actual review and remaining work

Actual hourly review 15 occurred at 19:51:33.282447 UTC against review 14
at 18:53:07.274754 UTC. It records qualifying movement in A.3, A.4 and B.4
and a consecutive no-movement count of zero. The next actual review is due
20:50:40 UTC. Source searches, equivalent formulations and packaging were
not counted as movement.

The general A.3/A.4 structural questions, the primitive mixed rank gate,
higher-dimensional B.3 thresholds, and B.4 exact indices at other
ramification/height values remain explicit open rows. Checkpoint 23 is to
be archived only at or after 20:05:40 UTC; no early save is authorized.

Typesetting counts and actual final-page visual inspections will be appended
after the final build. A pending check is not represented as completed.

### Late completed proofs: every power of three and fixed degree two

The complete multiplier-three induction is now independently checked by root and monodromy, giving geometric and arithmetic GL_(9d²−1)(F2) for every fixed nonordinary principal surface and every d=3^j. The uniform proof includes the group-cohomology calculation, many-theta graph lemma, actual norm-line translation, full node product, gluing hearts, normal Lang extension and transvection classification. Its finite supplement checks graph arithmetic at m=3,5,9,27, heart spans only at m=3,5,9 using explicitly retained shifts, and eight group-order cases; it makes no universal inference from numerical samples. Root rerun at20:01:50.258648UTC passed in0.5836126449939911s with author output unchanged. Full record: outputs/root_powers_three_degree_two_audits.json.

The full degree-two theorem is independently checked by root and obstruction/crystal: for every fixed nonordinary principally polarized abelian surface of two-rank f=0 or1, the relative rank is33+f and the geometric and arithmetic image is Hom(F2^(1+f),F2^32) semidirect GL32. The proof includes restricted-curve jet strata, the characteristic-two labelled-transposition inertia argument, the full sum-zero wreath group, all gluing columns including ambient columns, common six-theta comparison across rank drop, irreducibility of the32-dimensional covector kernel and the full stabilizer argument. Root's exact doubled-K6 graph rerun passed in0.0001489850037614815s at20:01:50.258648UTC and preserved the author output. The supplementary finite calculation proves only the specified graph and rank identities.

These proofs close additional fixed-surface degree cases; they do not settle A.4 generally. Its remaining fixed nonordinary nonproduct degrees are even d>=4 and odd d>=5 not powers of3. Actual review15 predates these promotions and is unchanged. All failed packaging wrappers and the first two actual LaTeX build failures are retained; final build and visual QA counts follow below.

### Final checkpoint verification

The frozen paper has 538 pages and 3829086 bytes, with 637 numbered statements, 44 new identifiers since checkpoint22 and no removed identifier. Every new identifier has an explicit check event and a final statement number. The paper bibliography has 157 entries; the source census has 162 rows. The export currently contains 367 agent program/output files. All 113 literal printed program paths resolve. Any later candidate computation before archiving is also exported, without silently promoting its statement.

There were 4 actual builds and 2 failed compilations. The actual logs of every attempt, including both failed compilations, are parsed separately from stale summaries. The maximum across all actual attempts was 74.57727pt. The first successful build (attempt3) had 1 boxes above2pt and the final build has zero; the final maximum is 0.41342pt. The final build took 55.448 seconds. All 46 selected final images were actually opened and visually reviewed, covering all ten newly included subsections, the residual overflow page, earlier material and the bibliography. No clipping, overlap, missing glyph or citation/tag defect was observed. The complete actual build inputs and logs are retained.

Checkpoint23 is archived only at or after20:05:40UTC. Actual hourly review15 was recorded19:51:33.282447UTC, with movement and zero no-movement streak. The next actual review and checkpoint24 are due20:50:40UTC. No early review or early archive is represented as completed.
