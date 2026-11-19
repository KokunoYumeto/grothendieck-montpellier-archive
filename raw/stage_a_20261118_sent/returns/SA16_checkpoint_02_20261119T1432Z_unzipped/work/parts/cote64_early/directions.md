# Research directions from cote 64, scans 2–77

These are proposed follow-up tasks. Their mathematical inputs were checked during consolidation; the additional tasks below have not been developed here. “A few hours” describes a plausible first result, not a promise to finish an unrestricted theorem.

| Rank | Direction | Interest | Plausible progress in one short run |
|---|---|---|---|
| 1 | Formulate the correct tangential Kummer category | High mathematical value | Exact fixed-group categories, necessary compatibility and a full-faithfulness test |
| 2 | Compare level-four data with the symmetric pinning normalization | High connective value | Explicit comparison of the two maps and a precise list of remaining scalar choices |
| 3 | State the relative structured-octahedron theorem | High mathematical and editorial value | A concise theorem and proof over arbitrary bases with 2 invertible |
| 4 | Give the almost-cartesian square a relative universal property | Medium to high value | The correct smooth branch object and a test over a nonnormal base |
| 5 | Package the central lifting obstruction in the manuscript’s relative category | High expository value | Explicit cocycle, lift groupoid and compatibility with the octahedral dictionary |
| 6 | Render the complete finite square/cube dictionary | Medium expository value | A certified subgroup diagram and explicit feature maps |
| 7 | Prepare a boundary and differential comparison only after its other sources are supplied | Conditional value | A precise comparison question and a list of required additional objects |

## 1. Correct tangential Kummer data

**Sources:** SA16-289–293; C-SA16-289–293 and C-SA16-391; MP-SA16-95. The relevant passage is `MPL_64_040-077_transcription.tex`, scans 71–74, physical lines 744–811.

The listed target category permits the inertia embedding to be chosen independently of the torsor class. The saved C₂² example disproves essential surjectivity with every written hypothesis satisfied. A useful theorem must instead identify the embedding with the actual tangent inertia, describe the allowable pointed descent data and specify morphisms, especially when the ramification index changes.

SGA1 XIII §2 supplies the tame local framework; Stacks03PK gives root-line objects and their automorphisms. The quadratic Legendre specialization is established by the local proof here and the labelled atlas in AntieauMeier2020, Definition 4.4 and Proposition 4.5. These results do not by themselves settle the unrestricted varying-group formulation.

**First concrete step:** fix one finite étale group G and one ramification index n, write the two categories and the comparison functor explicitly, and calculate its automorphism groups before attempting essential surjectivity. Only then enlarge the morphisms to varying groups. The expected result is a theorem with checkable compatibility conditions, rather than a silent repair of his text.

## 2. Level four and symmetric pinning

**Sources:** SA16-283, SA16-286–288, SA16-295–299; C-SA16-286 and C-SA16-295–298; MP-SA16-97; continuation C-SA16-515 and C-SA16-535. Both sides were read: early scans 66–77, lines 638–910, and `MPL_64_078-115_transcription.tex`, scan 93, lines 382–391.

ConradLevel Proposition 3.2 already gives a canonical ordinary Legendre structure from a 2-torsion point and an appropriate 4-torsion point. Negating the latter negates its differential. Conrad’s Remark 2.8 also excludes a natural ordinary S₃ action on the usual atlas. The remaining manuscript question concerns the additional symmetric square and μ₄ normalization; it must not be inflated into the claim that no canonical level-four construction is known.

**First concrete step:** put the zero-sum reference basis and Conrad’s two selected torsion points into the same local Legendre equation, evaluate both differentials, and compute their ratio under the six permutations of J and the central sign. This would identify the exact normalization statement to be proved in the continuation.

## 3. Relative octahedral correspondence with opposition retained

**Sources:** SA16-261–267; C-SA16-261–267 and C-SA16-363; MP-SA16-89–90. The passage is scans 45–53, lines 168–343.

The bare six-point stabilizer jumps from 24 to 120 in characteristic 5. Retaining the regular opposition gives a finite étale structured group of rank 24 whenever 2 is invertible. The present proof uses explicit projectivities and étale descent; it includes characteristic 3, where Beauville2010’s prime-to-characteristic convention cannot simply be invoked for S₄. Hua2026 §42 verifies the field exception but expressly leaves the relative theorem and the orientation refinement unproved.

**First concrete step:** assemble the proved local constructions into one theorem with three precisely defined groupoids: faithful Klein subgroups on conics, regular structured octahedra, and the corresponding four-covers. State separately what is canonical about the orientation identification and what would be additional chosen data. The scan check of the uncertain insertion remains an editorial prerequisite for attributing any exact wording to him.

## 4. The meaning of “almost cartesian” over a general base

**Sources:** SA16-275; C-SA16-275; MP-SA16-92. The passage is scans 61–62, lines 528–542.

Geometrically, the raw local fiber product has equation v²=u², and its two smooth branches give the required comparison. Absolute normalization over a nonnormal base is a different operation and need not commute with arbitrary base change. The phrase should therefore be replaced in commentary by an exact relative construction and universal property, with the geometric normalization statement recorded as a consequence.

**First concrete step:** write the canonical two-branch algebra over an arbitrary base ring with 2 invertible, then identify the property that characterizes it among smooth relative curves mapping to the raw fiber product. Test the formulation over a small nonnormal base. This is a clarification of the relative theorem, not a new assertion that the unqualified normalization already has all required base-change properties.

## 5. Central obstruction in geometric terms

**Sources:** SA16-244–248; C-SA16-244–246; MP-SA16-88. The passage is scans 37–38, lines 1581–1633.

The finite reduction is resolved: the D₈ extension has factor set c(g)d(h), so the obstruction is c∪d. Its vanishing permits lifts, whose groupoid is acted on by C₂-torsors; the universal group extension remains nonsplit. MerkurjevScavia2024, §1.1 and Example 1.4, gives the exact profinite cup criterion. The site argument in the proof supplement keeps the obstruction-gerbe qualification rather than assuming that one Čech cover computes arbitrary H².

**First concrete step:** express the two characters directly through the manuscript’s diagonal and codiagonal torsors, then show compatibility with the mod-four/projective correspondence under base change. A compact statement would make the author’s reduction usable later without importing an unverified arithmetic interpretation.

## 6. A finite atlas of the square and cube constructions

**Sources:** SA16-217, SA16-220–230 and SA16-249; C-SA16-217, C-SA16-220–230, C-SA16-305–306, C-SA16-322, C-SA16-328 and C-SA16-330; MP-SA16-81–86.

The computations already supply all 30 subgroups of S₄, their 11 conjugacy classes, 66 Hasse cover relations, ten nontrivial transitive feature sets, and the two inequivalent six-point covers. The remaining value is in presenting explicit maps and composition conventions. The corrected face-diagonal stabilizer lies in the normal Klein subgroup; the reflection-square functor must be distinguished from the nonfaithful functor Q↦Aut(Q).

**First concrete step:** render the saved exact poset and make one map table using the transporter formula for equivariant maps between coset spaces. Keep authorial statements, current completions and unresolved ink alarms visibly distinct. No new exhaustive group calculation is needed.

## 7. Deferred comparison with external boundary and differential projects

**Sources:** SA16-201–210, SA16-255–257 and SA16-288; C-SA16-307 for the locally verified scalar-quotient identity; `context_leads.tsv`. These are earlier-run contextual directions, not authorial open problems, so no invented MP identifier is assigned.

The supplied leaves establish finite level-two/four objects and tangent roots. They do not supply a compatible full congruence tower, a modular cusp, a family with its Gauss–Manin connection, or an indigenous bundle. The relevant LM, S20 and earlier research endpoints are not supplied. Katz1970, OgusVologodsky2007, BouwWewers2006 and Hoshi2015 were checked only to establish the hypotheses that any proposed differential comparison would have to meet.

**First concrete step:** when the cited other endpoint is attached, identify a single family and a single comparison map, record its characteristic and liftability hypotheses, and check both sides of that map. This task has conditional interest; it should not precede the source availability or be represented as a consequence of the finite calculations alone.
