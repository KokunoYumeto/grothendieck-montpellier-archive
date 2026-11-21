# H9 source record

Run: JAC1964-20261121. Agent: /root/h9_height. Model: GPT-6 Astra Pro;
reasoning effort not exposed. All source references below were actually read
in this run, with the limits specified. No entire external proof was formally
checked. Original attached results are taken as source hypotheses where the
task directs this.

## Attached sources

* `sources/ARCHIVE_44_scan004.tex`, Th. 5 and its margins: **algebraically**
  equivalent to zero; geometrically integral fibres; uncorrected formula.
  Read entire file. No scan image was supplied, so no palaeographic claim.
* `sources/ARCHIVE_44_scan002.tex`, Th. 3--4: domain of algebraic cycles and
  claimed canonical autoduality. Read entire file.
* `sources/ARCHIVE_44_scan008.tex` and `scan009.tex`, letter to Serre:
  primitive qualification and correspondence divisor. Read entire files.
* `sources/WARGAME_MATH_HUNCHES_20261112.md`, H9(a),(b): read entire H9.
* `sources/HODGE_BRIDGE_SKETCH_20261121.md`, Route 3, 3.4--3.5: read relevant
  entire section. These are unchecked proposals, not background theorems.
* 032 Corollary 8.4 is used only through the root agent's independent reading
  of the attached source. The H9 agent has not reread that PDF and therefore
  does not claim a source check of it.

## External primary sources and exact locators

1. Bruno Kahn, *Refined height pairing*, arXiv:2009.00533v7 (6 Dec 2023),
   later Algebra & Number Theory 18 (2024), 1039--1084.
   https://arxiv.org/pdf/2009.00533
   Read Definition 2.2 (admissibility), Proposition 2.8 and equation (2.9)
   (descent of intersection pairing), Theorem 5.6 (algebraically trivial
   cycles admit admissible lifts up to isogeny), Theorem 5.10 (elliptic
   normalization is the opposite of Silverman's), plus introduction's
   explicit comparison caveat. Web references available to root after its
   own open: `turn853292442view0`, `turn844745141view1`,
   `turn844745141view2`, `turn844745141view4`.
   Downloaded `work/h9/kahn_refined.pdf` for local reference; no need to
   redistribute this PDF in the final package.

2. Tetsuji Shioda, *On the Mordell--Weil lattices*, Comment. Math. Univ.
   St. Pauli 39 (1990), 211--240; Theorem 8.6, equations (8.11)--(8.15),
   printed p. 228. Original scan:
   https://rikkyo.repo.nii.ac.jp/record/10027/files/AA00610867_39-02_05.pdf
   Downloaded and rendered PDF page 18; image `work/h9/shioda_p18.png`
   was actually inspected. Theorem 8.6 verifies the inverse intersection
   matrix and the negative geometric sign. Web search ref:
   `turn853471825search35`; web open was rate limited but direct download
   succeeded. Do not use OCR alone for mathematical signs.

3. SGA 7 II, LNM 340, original scan:
   https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-2.pdf
   Downloaded `work/h9/sga7_ii.pdf` (444 PDF pages). The programme-audit
   agent directly rendered/read:
   * XVII 2.2: definition of Lefschetz pencil (EGA IV 17.13.7 for transverse
     axis is cited there). Our quadric proof directly verifies its conditions.
   * XVIII 5.3.2 p. 287, 5.3.4--5.3.5 p. 288: condition (A).
   * XVIII Proposition 6.2 p. 319: (A) iff nontrivial inertia at every
     singular fibre.
   * XX Theorem 4.1 p. 355 and Remark 4.3 p. 356: Griffiths-group obstruction
     for high-degree pencils. Original pages are in `work/programme/`.
   * XV 3.3.3--3.3.6 pp. 191--192: the vanishing generator is the image of
     either generator of the primitive exceptional-quadric quotient; the
     odd-dimensional Picard--Lefschetz coefficient is (-1)^(r+1) when the
     relative dimension is 2r+1. H9 personally inspected the original p. 192
     in this run; programme audit inspected both pp. 191--192.
   The H9 agent relies on the programme audit for the other direct image checks;
   a modern online transcription was used only to locate pages, because
   there are detectable degree errors in some of its adjacent sections.

4. Shou-Wu Zhang, *Positivity of heights of codimension 2 cycles over function
   field of characteristic 0*, arXiv:1001.4788, Theorem 1 and Remarks 2.
   https://arxiv.org/pdf/1001.4788
   Read entire four-page extracted text. It motivated the explicit
   orthogonality gate but is not required in the proofs delivered here.
   Web ref `turn853292442view1`. Do not list it as a theorem used if the final
   paper omits this alternate approach.

5. Damian Rössler and Tamás Szamuely, *A generalization of Beilinson's
   geometric height pairing*, Documenta Math. 27 (2022), 1671--1692,
   DOI 10.4171/dm/x15, author PDF
   https://pagine.dm.unipi.it/tamas/beilpairing7.pdf
   Search retrieved Proposition 6.1, Corollary 6.2, Remark 6.3, for smooth
   models; not invoked for singular pencils. It is an alternative
   cohomological approach, not a claimed proof of the full Bloch/Beilinson
   comparison. Web refs `turn968503326search24`, `turn968503326search26`.

6. SGA 7 I, LNM 288, original scan:
   https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf
   Local copy is `work/programme/sga7_i.pdf`. H9 personally inspected the
   original IX 9.2 pp. 419--421 and Theorem 10.4 p. 444. The theorem gives
   a single integral monodromy pairing common to all primes, and its
   positivity for a genuine polarization. Programme audit additionally
   inspected IX 10.3.5 p. 443 (ramified base change multiplies by e>0).
   IX 12.5 and 12.7 explicitly compare the curve Picard--Lefschetz formula
   with IX 9.2; these sections were read in the online transcription.
   The ordinary M,M' in IX 9.2 and the underlined M,M' of IX 5.5 use the
   opposite order for the original and dual character lattices. H9-L2
   now specifies the IX 5.5 convention. VIII 4.12.1 defines the line-bundle
   biextension used here; VIII 2.3.11 states the anticommutative comparison
   with Cartier-duality evaluation. Exact sections of those online pages
   were read, but H9 does not claim an original-image check of VIII.
   Modern transcription links:
   https://grothendiecksga.com/read/sga7/fr/9-5.html
   https://grothendiecksga.com/read/sga7/fr/9-9.html
   https://grothendiecksga.com/read/sga7/fr/9-10.html
   https://grothendiecksga.com/read/sga7/fr/9-12.html
   https://grothendiecksga.com/read/sga7/fr/8-2.html
   https://grothendiecksga.com/read/sga7/fr/8-4.html
   The 9-9 transcription contains incorrect dual symbols in some formulas;
   the original pp. 419--421 govern those formulas.

## Approaches tried and their outcomes

1. Treating geometrically integral fibres as eliminating all corrections:
   **refuted**, H9-C1. Integral cones contain middle-dimensional vertical
   cycles with nonzero intersection. Each of the two cones contributes +1
   in signed normalization.
2. Defining the height from arbitrary homologically trivial generic cycles
   by raw intersection of any closures: **not valid** without admissible
   lifts. Repaired by H9-T1, exact Schur-complement formula and radical
   compatibility condition.
3. Strengthening integral-fibre to nonzero vanishing cycles/condition (A):
   **proved**, H9-T2, sufficient to eliminate corrections on ambient
   primitive cycles. It gives an isometry between primitive algebraic
   cohomology of an abelian X and the geometric-height quotient R/R0 under
   032 Corollary 8.4. No abelian-Jacobian target is needed.
4. Replacing homological triviality by algebraic triviality silently:
   **refuted as a domain assertion**, explicit E^4 primitive cycle and SGA7
   XX 4.1. The defining map for an algebraic representative cannot be
   applied to that restriction.
5. Identifying primitive classes with a subgroup of J(K)/trace solely from
   a positive polarization: **invalid** without injectivity and height
   comparison. H9-T3 proves the exact quotient assertion once these maps
   exist. The quadric example has nonzero primitive classes in the kernel.
6. Deriving full H9(b) from corrected geometric height via a larger
   intermediate Jacobian or projection: **unresolved** as an arithmetic
   abelian-variety statement. The construction cited in cote 44 has only
   the algebraically trivial domain. For general homologically trivial
   cycles one must retain the full normal-function/motivic extension,
   not assume an unspecified map to P^m.
7. Applying 032 directly to J(C) times a hyperplane section Y:
   **unjustified**, because Y need not be abelian. H9-T4 instead transfers
   the fixed primitive class to J(C) times the ambient abelian X and
   proves the exact identity with positive factor b!. This proves the
   fixed primitive incidence polarization in all characteristics.
8. Killing the variable incidence factor using one finite-field fibre:
   **proved as a conditional criterion**, H9-T5. Absolute irreducibility
   forces a nonzero factor to realize all variable cohomology; good
   reduction and abelian Frobenius integrality force slopes in [m-1,m].
   A witnessed slope outside that interval forces the factor to vanish.
   No automatic existence of such a witness is asserted.
9. Deducing a real sign from one Q_l-square:
   **insufficient**. The successful replacement H9-T6 uses ALL primes,
   SGA IX's one integral monodromy pairing, and absolute irreducibility.
   End^0(B)=Q yields one rational incidence scalar c. The rank-one formulas
   give q0/(e c) in Q_l^{*2} for all l other than the characteristic, with
   q0>0 rational and e>0 independent of l. H9-L1 proves that this rational
   number is a rational square, hence c>0. This closes the variable sign
   problem under T6's explicit generic-monodromy hypotheses. Together
   with T4 it proves the full primitive incidence polarization for those
   generic sections, but does not repair H9(b)'s homological-cycle domain.
10. Extending ambient positivity to the entire generic-fibre height group:
    **proved as an exact reduction**, H9-T7. Chow localization and the
    codimension-two blowup formula express every generic cycle using the
    ambient variety and the axis. An algebraic inverse to L_h^2 produces
    the adapted pair. The separate vertical-cohomology lemma proves
    injectivity without assuming positivity of the axis. The entire
    height quotient is canonically the orthogonal sum of primitive
    algebraic classes on X and the kernel of axis Gysin, with exceptional
    minus sign. Its remaining sign is exactly the axis Hodge-standard
    sign. In codimension two the axis is a surface and H9-T8 closes that
    gate using the classical surface Hodge index theorem in every
    characteristic. The quotient radical is precisely the image of
    global homologically trivial cycles.
11. Removing condition A in the abelian pencil setting:
    **proved by the programme/root follow-up JAC-P07**, independently
    whole-read here. The variable dimension is h^n minus the Catalan
    number C_n, which is positive because h^n=n!h0(L). SGA vanishing-cycle
    spanning and conjugacy then make every local cycle nonzero. This
    applies to genuine Lefschetz pencils in even ambient dimension;
    it does not rescue the general quadric assertion.
12. Removing the axis sign gate at a geometric generic axis:
    **successful source route under programme/root integration**.
    Katz--Pandharipande, *Inequalities related to Lefschetz pencils and
    integrals of Chern classes*, Corollary 3, author PDF pp. 1--3, gives
    full orthogonal monodromy for degree d>=3 sections of an odd-dimensional
    ambient variety of dimension at least three, apart from the linear
    P3 cubic exception. H9 directly read these pages; no characteristic
    restriction occurs in Corollary 3 (the characteristic-two exception
    belongs to the separate Theorem 4). A geometric-generic algebraic
    cycle has a finite Galois orbit, so its variable class is fixed by
    the connected SO group and is zero. Application and full proof are
    owned by programme audit as JAC-P09. No assertion for every fixed
    k-valued axis or for a Zariski-open set of such axes is made.

## Status and novelty labels for later extensions

H9-C1's final proof works over every algebraically closed field. In
characteristic 2, the generic odd quadric remains smooth because its only
possible gradient radical does not lie on it; the two nodal local forms
are split nondegenerate quadratics in 2m variables. The conic ruling
family is a rescaled Veronese parameterization in every characteristic.
This strengthening is an explicit deduction checked here, not an assertion
about an undisclosed archival theorem.

H9-T4, T5 and T6, and the proof arrangements H9-L1 and L2, are deductions
written in this run. No historical originality is claimed. H9-L1 is an
elementary known local-square principle with its proof included. H9-L2
is a rank-one consequence of the cited SGA monodromy theorem with the
sign convention spelled out. H9-T6 is conditional only on its displayed
monodromy/projector/incidence hypotheses; applying it to a named pencil
requires verifying those hypotheses. The programme-audit agent has read
the entire T6 proof and reported a successful check; that is independent
mathematical review, not formal verification or a reproof of SGA.

H9-T7 and H9-T8 are further deductions written in this run. The root
reported an independent whole-proof pass. Their classical blowup input is
Fulton, *Intersection Theory*, Proposition 6.7(e); H9 checked its explicit
direct-sum form against the primary research exposition Shen--Vial,
*The motive of the Hilbert cube*, Proposition 2.10 proof, equation (10),
printed p. 15, but does not claim a direct full reading of Fulton's book.
The surface input is SGA 6, XIII, Theorem 7.1, printed p. 662, personally
inspected in `work/programme/sga6_probe-665.png`. Numerical divisor
triviality versus algebraic triviality up to a multiple is SGA 6, XIII,
Theorem 4.6, pp. 645--646, originally inspected by the programme auditor.

Primary links for these later source checks:
https://www.math.uni-bielefeld.de/~vial/X3.pdf
https://library.slmath.org/nonmsri/sga/sga/pdf/sga6.pdf
https://web.math.princeton.edu/~nmk/Inequalities15.pdf

## Transcription conclusion

The quadric contradiction does not justify changing the reading
`fibres sont géom. intègres`. It establishes that the stated mathematical
hypothesis is insufficient. A corrected theorem needs admissibility or
condition (A), or explicit local correction terms. There is no supplied
manuscript image supporting a textual replacement.


## H9-T9 and H9-T10 follow-ups

H9-T9 (`H9_incidence_height.tex`) proves the corrected height/trace
statement on the algebraically trivial domain. Kahn's degree-zero
correspondence adjointness (Proposition3.8 pp19–20; Theorem4.14 p31)
is applied only after an explicit product-with-projective-space
reduction. The incidence kernel then pairs to zero. The algebraic
identity T_L phi_L=−(d−1)!chi(L) id, proved by translation and
Albanese rigidity, converts Kahn Theorem6.6's unconditional curve-base
negativity into positive definiteness modulo trace. Theorem6.2 supplies
the exact Lang–Neron factorization. Root and programme each independently
whole-read and passed this proof; no general higher-cycle Neron–Tate
comparison is asserted. Rational-point denominators are explicitly
cleared. This does not extend the incidence map to all homologically
trivial cycles.

H9-T10 (`H9_regular_threefold.tex`) proves the corresponding rational
primitive polarization for the ACTUAL regular algebraic representative
of a generic threefold section of an abelian fourfold, accepting032.
Its variable assertion applies to any fourfold with algebraic lowering;
for a complete-intersection fourfold it is the entire actual Ab²
assertion and does not use032. The key normalized-miniversal realization
is injective by its splitting through the regular quotient and the
codimension-two Bloch injection. The source for existence over imperfect
K=k(t) is ACMV, A functorial approach to regular homomorphisms, Algebraic
Geometry10(2023)87–129, Theorem2 p89 and Theorem6.1 p114. Theorem8.1 p119
and Proposition8.2 p120 give the Bloch/realization statements. The
original publisher PDF was directly read and downloaded here:
https://api.algebraicgeometry.nl/Article/19846/2023-1-003.pdf .
ACMV Astérisque455(2025) §1.3, Lemmas1.3–1.4 pp6–7 and Proposition8.1
pp41–42 supply the miniversal and pointed-family compatibilities used
in the proof. No integral purely inseparable base-change theorem,
standard torsion assumption, or surjectivity onto all H³ is inferred.

Both are deductions assembled in this run; no historical originality
or formal verification is claimed. The field-scope repair in T10
uses the injective realization to test nonconstant geometric curves,
so it does not silently identify the geometric universal regular
object with an integral base change over an imperfect field.

Independent arithmetic checks added: programme JAC-P10 local smooth
tail chart and Hodge-lattice determinant bound passed a whole-proof
check. Liu's Example10.4.39 pp548–549 and Proposition10.4.37 p547 were
directly read in the primary book PDF text. Proposed translated
torsion-grid and Jensen inequalities for the archimedean theta
certificate were checked conceptually; no numerical certificate or
Gram code was checked at that event.

## H9-T11 through H9-T13

H9-T11 (`H9_elliptic_reduction.tex`) gives a conditional numerical
Hodge-standard reduction from primitive incidence polarization on
X times an elliptic curve. The Poincare-family calculation and the
test against every complementary middle cycle are included in full.
It proves nonnegativity with zero space exactly numerical equivalence;
strict positivity on cohomology requires the separately identified
numerical/homological equality. For abelian X, accepted032 supplies
this equality. The file now proves that implication using the
algebraic primitive decomposition and explicit positive complementary
test class, rather than silently assuming D(X). Root whole-read the
final proof and reported PASS. This does not transfer032 to a
nonabelian fixed axis or infer anything about all CH(N).

H9-T12 (`H9_base_change.tex`) separates three exact finite-extension
statements. Purely inseparable restriction is a rational Chow
isomorphism with inverse degree-normalized corestriction. Every finite
extension has an orthogonal restriction/norm-zero decomposition on
Kahn's admissible domain. Covers unramified above the critical values
admit the full homologically trivial group by the smooth-model and
specialization argument. The algebraically trivial primitive domain
has the polarization/trace theorem over all finite extensions, with
unchanged fixed trace factor. Kahn Proposition3.9 pp20–23,
Proposition4.12(c) p30 and Theorem4.14(b) p31 are the precise base-change
inputs; root and programme each directly rechecked those passages and
whole-read this proof. Positivity on new norm-zero homological cycles
over separable extensions is not asserted.

H9-T13 (`H9_complete_intersections.tex`) extends primitive incidence
polarization to generic odd complete intersections in an abelian
variety, with only the last section required to vary in a genuine
Lefschetz pencil. For total codimension c, the algebraic fixed inverse
is (L^c)^-1 k_*, the primitive exponent after the parameter-Jacobian
lift is b+c, and the positive transfer coefficient is
(b+c-1)!/c!. It uses032 on the abelian product and the already checked
all-characteristic odd-fibre monodromy argument. SGA7II XVII2.5.1 p217
supplies degree-d pencils for d>=2; XVIII6.6–6.7.2 pp323–327 supplies
the terminal even-ambient monodromy. Programme whole-read and passed
the proof. The actual Ab² conclusion uses exactly the field-scope
checked ACMV inputs recorded for T10. The final paragraph exhibits the
failed transfer for a fixed axis: kappa_*w=0 kills the elliptic family
in the abelian ambient cohomology, and the defining divisor classes
are not ample along the elliptic factor.

## Later independent arithmetic checks

Programme P13–P14 (`work/programme/fermat_motive_structure.tex`) passed
a whole-proof check by this agent. The exact Chow argument uses
commuting realization-zero idempotents and the stated Kimura
finite-dimensionality consequence, then the functorial symmetric
power description of an abelian motive. These source theorems are
carried as cited background, not reproved here. The resulting equality
N=h³(J)^G and the determinant action of M3(Q(i)) are at Chow level.
They show that the full abelian-endomorphism orbit of the Fermat class
is its existing two-dimensional CM plane, without bounding CH²(N).

The AR15 proposed algebraically-trivial radical argument was checked
conceptually using the Hodge types of N, pointed curve correspondences,
functorial Abel–Jacobi, and Abel's theorem for divisors. This is a
targeted proof check of that argument, not an assertion of injectivity
for the higher Abel–Jacobi map or of positivity on the full complement.

## H9-T14 and the constant finite-field domain

H9-T14 (`H9_constant_finite_field.tex`) combines programme JAC-P15
with an explicit spreading lemma. If CH^r_num(X0)_Q=0 over an
algebraically closed base k0, then over every extension F/k0 the
numerically, geometrically homologically and algebraically trivial
rational cycle groups coincide. The numerical proof pushes the
refined intersection with each fixed complementary cycle to a
codimension-zero class d_w[S] on the connected parameter space.
Both the original generic point and a k0-valued closed point become
F-rational parameter points. Thus the algebraic-equivalence witness
already exists over F, including imperfect F; no standard conjecture
D(X) is needed in this spreading step.

JAC-P15 supplies the hypothesis for geometric abelian-type varieties
over Fbar_p, using accepted032 Corollary8.3 and Kahn2003 Theorem1.10,
published p982. For constant odd-dimensional abelian varieties,
accepted032 Corollary8.4 and the primitive polarization theorem then
give the height statement on the entire homological group whose
incidence image is primitive. The exact radical is the inverse image
of B(k)_Q, and the quotient is Hom_k(J(C),B) tensor Q. A constant
trace variety does not mean that all K-points are constant. The
normalization gives height 2 deg(f*ell_B). No rational=num statement
over transcendental extensions or arithmetic full-CH(N) result is
claimed.

The parameter-space source was directly read at
https://www.math.uni-bielefeld.de/~vial/abtriv.pdf : Definition3.1 and
Proposition3.5 pp4–5, Lemma3.8 p6, Lemma3.9 pp6–7, Theorem4.11 and
Lemmas4.14–4.15 pp14–16, TheoremA.1 pp17–18 (author pagination).
Root and programme independently whole-read the earlier final theorem;
this agent whole-read the strengthened numerical variant as well.

## H9-T15 and the Katz source-scope repair

H9-T15 (`H9_conductor_selmer.tex`) proves the conditional rank-one
Bloch–Kato Selmer implication for the Fermat character at5 using its
actual conductor (1+i)^4. Castella's Section5 standing assumption
of exact divisibility by the different fails at this conductor; the
proof therefore uses the arbitrary-conductor reciprocity construction
in Theorem4.2.1, not an unqualified application of Theorem5.2.1.
The nonzero Katz value produces a nonzero Bloch–Kato class. Rubin's
full unnormalized twisted elliptic-unit Euler system has a base class
that is a nonzero unit multiple of its normalized specialization;
Castella p16 explicitly chooses the invertible auxiliary factor.
Rubin's strict-dual bound and Poitou–Tate then give dimension1.
The excluded bad prime may have conductor exponent4; it is retained
in the Euler-system bad-prime ideal. No Chow-generation or higher
Abel–Jacobi injectivity assertion follows.

Sources directly read: https://web.math.ucsb.edu/~castella/Katz.pdf ,
Section4.2 printedp16 and the printedp24 proof (also visually read);
https://swc-math.github.io/aws/1999/99RubinES.pdf , ChapterII
Theorem2.3/Remark2.4 p24, ChapterVI Definition3.1/Theorem3.5 pp92–93;
https://discovery.ucl.ac.uk/id/eprint/10067153/1/1710.04956v2.pdf ,
Theorem2.5 and Proposition2.8 pp2–3. Arithmetic and root independently
whole-read and passed T15 with these established inputs.

## AR19 and JAC-P16 independent checks

The final AR19 proof was independently whole-read and passed. BK
Definitions3.8–3.9 pp41–42 give the measure normalization; its
period formula p40 gives the exact Lambda^5/[rho0(a)Na^2]=1
cancellation. The fourth-order theta coefficient is exactly
-256(1+i) after summing the two ray classes, a5-adic unit. The
exact SymPy script `work/arithmetic/fermat_katz_coefficient.py`
was independently executed successfully. BK Theorem3.11 p44 and
Castella Theorem2.2.1 p7 were visually inspected: the Euler factors
match under inverse character, including the conjugate prime hidden
inside BK's imprimitive L-function. Compatible periods and the dense
critical component identify the values. The resulting unit proves
the Katz input of T15; it is not a Chow-rank theorem.
Primary BK: https://arxiv.org/pdf/math/0610163 , v4 (2007), local
`BK2007.pdf/.txt`; source passages also include equation15 p15,
Theorem1.17 p17, Corollary2.17 p30, Definition3.2 p36.

Programme JAC-P16 (`work/programme/abelian_type_lefschetz.tex`)
passed this agent's whole-proof check. Accepted032 D for all abelian
products transfers to all Hom spaces and direct summands by the
categorical trace test. Jannsen semisimplicity and faithful realization
then give algebraic Lefschetz inverses, with exact normalized lowering
formulas and finite inseparable norm descent. Jannsen's complete
original paper, Invent.Math107(1992)447–452, was directly read;
Theorem1 and Lemma1 are on p448, semisimplicity proof p449.
Primary: https://epub.uni-regensburg.de/26642/1/jannsen10.pdf .
The proof does not supply Hodge-standard positivity for an arbitrary
abelian-type variety's own primitive form.

A final T14 refinement permits a geometric isogeny to the constant
finite-field abelian variety. The isogeny descends to a finite
extension, and the already proved rational norm argument descends
algebraic triviality back. Consequently odd-dimensional isotrivial
abelian varieties over k(C) also have the full homological primitive
height domain and the exact actual K/k-trace radical. Their primitive
factor need not be constant; the Hom(J(C),B) formula is retained only
in the genuinely constant case. This refinement has its own targeted
proof event and uses no additional source theorem.

## H9-T16 through H9-T18: degeneration and the finite-cover sign

H9-T16 (`H9_semistable_axis.tex`) records the semistable degeneration
attack in full. Degree-one elliptic product line bundles have a fixed
component, so degree-at-least-two divisors are needed. The initial SNC
central fibre also fails the normal-bundle condition; the explicit
xy=tz small resolution replaces its leaves by blowups and keeps W×E.
Its weight complex contains the nondegenerate middle block
Hmid(W) tensor H1(E), killed by N. Torsion attaching points make the
Poincare family glue in rational operational Chow by envelope descent.
Under the explicit global generic finite-index irreducibility and
rank>2 hypotheses, it cannot lift as a family with the same elliptic
parameter: a nonzero rank<=2 map would land in the variable system.
The source comparison is deliberately only generic-to-special.
Primary Saito2003 Cor2.2.4 p21, Prop2.2.6 pp23–24 and Prop2.4.4
pp35–36 were read at https://www.ms.u-tokyo.ac.jp/~t-saito/pp/wmr2r.pdf ;
Ito Theorem1.1 p2 at https://arxiv.org/pdf/math/0308141 supplies E2
degeneration for arbitrary residue fields. Stacks42.22.4 supplies the
envelope exact sequence. A final support-preserving incidence-locus
argument shows that keeping all products Z_i×E gives zero below-middle
cohomology, and in the explicit elliptic-coordinate example the
individual product cannot lie in any such smooth ample CI at all.

H9-T17 (`H9_threefold_cover_sign.tex`) directly checks the entire
Zhang1001.4788 note. Theorem1 pp1–2 requires BOTH vertical
orthogonality and Alb(hz)=0 for a threefold fibre. It does not prove
all-homological admissibility or positivity without that condition.
Kahn6.1/6.2/6.6 give the rational orthogonal splitting into the
Albanese-primitive part and h Pic0, with negative form on the latter
modulo trace. An explicit cover C=E→P1 unramified over the pencil's
critical values supplies norm-zero classes hD and (a2-a3)D with heights
-12d^3 and 4d and mixed pairing0. The first fails Zhang's primitive
condition; the second satisfies it. Both the involution cover and a
prime-to-characteristic degreeN pencil in |N·0| work in every
characteristic, with exact norm0. Thus full all-homological positivity
after separable cover is refuted, while the primitive statements
remain intact. Root and programme independently whole-read T17 and
reported PASS; the all-characteristic and positive-plane refinements
have separate scoped check events.

H9-T18 (`H9_cover_variable_gate.tex`) proves the positive-characteristic
Albanese-primitive cover question is equivalent to the Hodge-standard
sign on Alg²(X) intersect ker(H4(X)→H6(A×C)) for the smooth incidence
fourfold X. The fixed primitive norm is explicitly
b beta0² -3b h² alpha² + eta²h, and the curve transfer for the last
term has positive coefficient g!, with b=degree cover and g=genus C.
Accepted032 proves every fixed sign. The Zhang vertical correction
is made algebraic and cohomologically primitive using the actual
Lefschetz inverses on A×C and on the hyperplane threefold, plus the
ordinary divisor index theorem. The converse uses Kahn negativity
to remove only a constant trace Picard component without changing
the global variable class. No motive decomposition or generic full
orthogonal monodromy is asserted for the new variable block of this
rank-two incidence family.
