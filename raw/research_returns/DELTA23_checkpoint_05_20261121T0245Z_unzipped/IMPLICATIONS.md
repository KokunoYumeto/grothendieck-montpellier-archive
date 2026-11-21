# Implications of the findings

This file is updated during the run. It describes only consequences of
checked statements; open comparisons remain open.

## Two–three reciprocity

D23.L1 supplies an explicit Hilbert-symbol realization of the two compressed
frame parities. Its definition already uses those parities. It establishes
the requested product identity with the correctly typed expression
`(-1)^Δ`, rather than identifying an additive bit with a multiplicative
Dirichlet-character value.

D23.L2–L3 separate this encoding from a new arithmetic constraint. The E.58
mixed pair is represented by `(5,3)`: its negative symbols occur at 3 and 5.
It obeys the global product formula. Requiring a rational quaternion class
supported only at 2 and 3 is precisely the equal-parity condition; without an
independent construction of that restricted support, reciprocity restates the
main gate. D23.L6 refutes the explicit splitting-normalized Kubota test of the
corrected integral matrices. It does not claim that every possible local
construction is impossible.

The full arithmetic frame comparison D23.C5 and image calculation D23.C6
identify the complete normalized adelic arithmetic constraint, subject to the
supplied E.58/E.65 and field-intersection inputs. The gentle frame image is the
product of the two normalized norm-one tori; the Galois image has index two,
cut out by equality of the two finite parities. Thus even retaining every
congruence level of these two frames yields only the known relative bit Δ.
This does not settle which part of that image is reached by full GT.

## Order five and level six

D23.T1–T2 and D23.F1–F2 repair the missing order-five target map by using a
six-point stabilizer and a uniquely normalized lift to five-strand braids.
The resulting norm-one character is an actual group homomorphism. The
construction keeps the distinguished pole and therefore does not assume the
false descent of the symplectic representation to the five-point sphere group.
The arithmetic normalization has the explicit quadratic twist by ζ₅−1.
D23.F5 rules out identifying the common arithmetic 3-bit directly with a
quadratic character of the genuine fifth-fibre Tate image: the supplied exact
triple field intersection excludes it.

D23.F6–F7 replace the unknown inner conjugator in the level-six comparison by
a canonical frame and two explicit free-group equations. Their truth on all
relevant elements, and their relation to Δ, still require proof. D23.F8 and
D23.L7 prevent a literal identification of the rational Atkin–Lehner matrix
algebra with either proposed division-quaternion explanation.

## Grothendieck's manuscripts: exact reading convention

The primary Montpellier PDFs include an unnumbered cover before the numbered
archive scans. We distinguish the one-based PDF page from the printed scan
number. This avoids the one-page ambiguity in the supplied run's references.

Primary source: cote 145, *Printemps 81 (vieille rédaction)*,
<https://grothendieck.umontpellier.fr/145.pdf>. Directly inspected here:
PDF pages 7, 11, 12, 22, and 28, corresponding to numbered archive scans
6, 10, 11, 21, and 27. Scan 6 treats normalized actions and conjugating
elements. Scans 10–11 discuss the additional numerical parameter and its
written relation; the latter relation is the one used by DELTA_ON_GT
B.24–B.25 to distinguish the manuscript's numerical β from a modern CM frame
coordinate. Scans 21 and 27 concern sections and chosen stabilizers. These
pages supply the historical context for keeping the marking and conjugator
data explicit. They do not state the new Hilbert-symbol identity or prove the
pentagon parity comparison.

The new results sharpen that distinction: a conjugating frame, its scalar
compression, a matrix lift, and a local splitting are different specified
objects. The proofs above identify their relations only where a complete
comparison has been given. In particular a numerical parameter in the
manuscript is not relabelled as Δ because it uses the same letter as a modern
frame.

Cote 143, *Paradigmes des courbes algébriques (version provisoire)*,
<https://grothendieck.umontpellier.fr/143.pdf>, was downloaded and its cover
verified (33 numbered scans, plus cover). No uninspected page of that
manuscript is used as a theorem or an exact mathematical locator in this
version. The supplied run's Longue Marche §47 reference is cote 140–3,
folios 415–420, scans 229–240 (DELTA_ON_GT A.14/A.60–A.64); that reference
is retained as a source-run locator rather than presented as a new scan
inspection.

## P versus NP through geometric complexity theory

None of the checked results proves a circuit lower bound, constructs a
representation-theoretic obstruction separating the permanent from the
determinant, or establishes an algorithmic reduction from such a separation
to the value of Δ. The objects actually controlled here are continuous
characters and specified finite representations of profinite groups. The
supplied prompt gives no theorem converting this character calculation into
the required complexity bound. Accordingly, neither a vanishing nor a
nonvanishing answer for Δ alone would, by the results proved here, settle
P versus NP. No conclusion about that problem is claimed.

The Alpöge theorem is accepted in the stipulated sense of the prompt. Its
attached note mentions metaplectic reciprocity in connection with steps 3 and
5 and the Gauss-sum discussion on page 3 (including footnote 3). Those
analytic uses do not identify the two profinite frames. D23.L2 specifically
shows why a global product formula cannot supply that missing identification
by itself. No Lean statement is invoked in any proof of this run, so there is
no invented Lean-file locator or claimed formal check.

## Further checked comparisons before checkpoint01

D23.F9 identifies the precise order-five scalar on the arithmetic subgroup: C5=(-1)^kappa5 Omega5. Its proof fixes the positive periodic braid, the order-five deck transformation and the normalizing square-root twist. The quotient of these characters gives a relative character on the multiplier-one full GT group, but its triviality there is still a separate question.

D23.F12 shows, conditional on the supplied E.58 lifting input, that every pronilpotent level-six test can be simultaneously blind to one actual mixed-sign gentle element. Thus a successful comparison using that subgroup must use information beyond its pronilpotent action.

D23.P6,F13,C9-C10 give an actual five-point finite matrix test which retains the cubic sign and a perfect SU3(3) component. This closes the applicability of the earlier nilpotent-second-derived no-go for this particular new representation. It does not yet decide the equality of the two signs.

## Checked developments before checkpoint02

D23.P10 replaces the order1944 cubic detector by an order216 quotient and the joint order46656 source by order5184. There remain twelve necessary actual-source values, six mixed. P7-P9 and C15 show why the particular Krammer pentagon and mixed-perfect Nielsen tests do not by themselves remove those values: every reduced solution has a common-word realization and passes the checked closure. None is promoted to an actualfullGT element.

D23.F22 and P13 give an actual cubic descent with a3(D_E h)=Psi3(h)/2 and a2(D_E h)=a2(h). Consequently the harmonic comparison defect is exactly Delta(D_E h). This is a new structural relation between the two descent constructions. Its vanishing on fullGT is still a question. C14 makes the associated cubic cover diagram explicit, with the two different puncture fillings that would have to be compared. D1-D2 show that all cyclic distribution equations in one fixed finite target do not force that comparison.

D23.F18 strengthens the level-six limitation: everygentleH action is inner on the entire congruence completion, so all its congruence Atkin-Lehner defects vanish. A successful proof of the full marked comparison must use noncongruence information. F21 and P11-P12 record additional precise failures of the tested cyclic and Hurwitz representations. These results do not create a bridge to a circuit lower bound or change the stated historical scan interpretation.

## Orbital and Hurwitz additions before checkpoint03

D23.C16-C20 distinguish exact five-point compatibility from the weaker affine covariance. Both orbital pentagons and all their path corrections are proved, but their periodic conjugacy becomes an identity after the existing affine covariance and does not imply the missing parity equality. This is a concrete limit on the proposed reciprocity mechanism.

D23.P17-P18 instead supply a finite Hurwitz representation retaining both marked detectors with a kernel proved invariant under multiplier-one fullGT. The proof uses the standard genus-zero braid action and an isolated finite orbit, with exact locators in Lochak-Schneps1994 sec5 Prop10 and Harbater-Schneps sec0.1eq1/sec3Lemma1. No unproved higher-genus or arbitrary-cover compatibility is inserted. It creates a justified finite test, not yet a decision ofA84. None of these additions supplies a representation-theoretic bridge to GCT or changes the previously stated PversusNP implication boundary.

## Orthogonal Hurwitz and raw-cover findings

D23.P18 and H6 establish actual multiplier-one full-GT stability of a finite Hurwitz quotient and its product-fixed raw cover. C23-C24 and F30 identify the twelve orthogonal blocks and their independent simple factors. P19 derives the exact quadratic form from relative cup product and proves its orientation scaling in the free profinite setting. H3-H4 and P21-P22 then give a complete finite necessary-conjugator list, with36 remaining after F34. These results use the standard genus-zero braid action, not an unproved compatibility with a higher-genus lego rule.

The arithmetic normalization H2 uses actual Galois elements and coprime Kummer extensions. It is a symmetry reduction of the main question. Finite candidates, ordinary common-word realizations, and actual full-GT elements remain distinct. In particular, the current first/mixed common-word computation addresses only F12 and R34; it does not establish the other pentagon evaluations or the free gentle relations. The raw cover retains additional cyclic deck information, but its full-image kernel is not assumed to be just the constant cyclic deck group.

These finite computations have fixed group parameters. They supply no asymptotic complexity lower bound, no reduction from a GCT obstruction problem, and no bridge theorem to P versus NP. Their relevance to the cited Grothendieck passages remains the explicit profinite and geometric comparison described above. The historical cotes and scan boundaries in the earlier sections are unchanged; no new historical claim is inferred from the orthogonal group identification.

## Strict necessary reductions after checkpoint04

F36,H8,P26 now eliminate candidates inside the fixed actual-GT Hurwitz test, reducing36 necessary conjugators to6 and18 fullpairs. The rejected raw pentagons have nonconstant ordertwo fiber defects, so allowing a global deck scalar would not repair them. C30-C31 then give three existential normalforms by actual-source operations: cubing and conjugation by complex conjugation. This is a smaller main gate, while A.84 remains open.

C28,C29,H9/F38 resolve a different question: each surviving finitepair has one ordinary commutator word realizing allfivevalues and allmixedorientations. P28 also supplies the relevant finitepureframes for every existentialnormalform. Consequently these finiteword and frametests cannot finish the proof. The missing step is actualprofinite compatibility or a new necessary obstruction. The orderfiveframe in the larger sphericalNielsen action is being investigated separately. None of these statements changes the stated complexity or historical implications.

C33 further reduces that existence question to two explicit finiteforms,(1,0) and(27,2), using the actual odd product h(chc)h. The distinction between an existential normalform and an individual exclusion is retained: all eighteen full oddclosures pass the finite test.

P29,F39,P30 show why the orderfivepureframe condition in this particular fullsphericalcover still cannot comparethetwo signs: the purefiniteimage has sixtyindependentsimplefactors, its remaining quotient hasorderprimetofive, and its orderfivecohomologyset is trivial. This is a limitation of thisspecifiedfiniteimage; it doesnot trivialize orderfiveframes in the profinitegroup.

F40-C34 now force the tuple action and the braid evaluations to use the same associator. Their complete finite gentle test excludes the second existentialform and leaves only(1,0) aftercubing. This is a strict necessary reduction ofA.84; the remaining finiteform has notbeen realized or excluded in actualfullGT.
