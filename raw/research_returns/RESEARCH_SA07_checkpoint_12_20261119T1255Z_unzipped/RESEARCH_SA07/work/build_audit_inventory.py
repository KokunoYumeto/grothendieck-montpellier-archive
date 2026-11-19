"""Assertion-level coverage of every requested F.3 note entry.

Rows are individually adjudicated, not inferred from a keyword classifier.
The source JSON preserves the complete note text and the source-entry CSV its
precise file/line provenance.  Each row retains its historical classification.
"""
from pathlib import Path
import csv
import json
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]
entries = {e['note_id']: e for e in json.loads((ROOT/'work/audit_notes_source.json').read_text())}

# Columns: note id | status | mathematical assertion or reading | proof/locator | exact remaining obligation.
DATA = r"""
I.P01|OPEN|Betti–de Rham realization data classify the proposed global motives.|B.2.1; F.3.4|Specify the global category and essential image, then prove full faithfulness and essential surjectivity; the local comparison does not supply this global statement.
I.P01|OPEN|Betti–Hodge realization data classify the proposed global motives.|C.1.1–C.1.2; F.3.4|General category and essential image remain unspecified; Hodge fullness for algebraic-cycle correspondences requires the indicated cycle-surjectivity statement.
I.P01|OPEN|Bare Hodge structures classify the proposed global motives.|C.1.1–C.1.2; F.3.4|Determine the intended category and the image; general motivic Hodge fullness remains unresolved.
I.P01|OPEN|Betti–Gauss–Manin realization data classify the proposed global motives.|B.2.2; F.3.4|Specify base, connection, integral or rational data, and geometric essential image.
I.P01|OPEN|Betti–Tate realization data classify the proposed global motives.|D.3.2; F.3.6|Known abelian Hom theorems do not provide the unspecified global category and essential image.
I.P01|OPEN|Filtered crystalline realization data classify the proposed global motives.|B.1.5; B.2.3|The proved local admissible categories must not be substituted for an unspecified global motivic essential image.
I.P02|PROVED|Local description 1′ has a period-ring reconstruction using admissible filtered modules and Galois representations.|B.2.1|The manuscript's unspecified global analogue is not identified with this local construction.
I.P02|PROVED|Relative local comparison supplies the stated smooth proper version of 4′, retaining connection and filtration.|B.2.2|No arbitrary geometric essential-image classification is inferred.
I.P02|PROVED|Passing up to isogeny changes lattices to rational representations; finite extension changes good to potentially good reduction data.|B.1.1–B.1.2; B.2.3|The descent datum must remain in the potentially crystalline category.
I.P03|PROVED|Weak admissibility gives the exact rational crystalline or semistable essential-image condition.|B.1.5; B.2.1|Retain N in the semistable case and N=0 in the crystalline case.
I.P03|REFUTED|Every filtered Frobenius module as displayed is admissible without numerical conditions.|B.1.5, rank-one t_H=1,t_N=0 example|No missing weak-admissibility premise may be silently supplied to the witness.
I.P03|REFUTED|The Frobenius semilinearity can always be placed on the ramified coefficient field itself.|B.1.5, p=2 cubic-extension example|Use Frobenius on K_0 and the filtration after scalar extension to K.
I.P04|PROVED|M(A[p]) is canonically H^1_dR(A/k) over a perfect characteristic-p field, including p=2.|F.3.1; Oda Corollary 5.11, p.131|Scope is abelian H^1 over a perfect residue field.
I.P04|PROVED|Oda's map identifies the Dieudonné submodule with the Hodge extension maps.|F.3.1|No canonical splitting is asserted.
I.P04|PROVED|The mixed-characteristic lift and rational Galois realization require the additional reconstruction maps stated in B.|B.1.1–B.2.3|Oda's residue-field comparison is not used as a substitute for those maps.
I.P05|REFUTED|The ℓ-adic Tate module for ℓ≠p faithfully retains a p-divisible group.|B.1.3|The literal prime remains ℓ in the transcription; the faithful mixed-characteristic replacement uses p.
I.P05|READING|The frozen local list writes ℓ although its surrounding vector space is p-adic.|Frozen witness 18/005:L20–26; original cote18 PDF5/archive p.4|Original question leaf visually inspected at180dpi on19November2026; the displayed prime supports the frozen ell-adic reading. The mathematical correction still retains the literal prime and uses p in the faithful replacement.
I.P06|PROVED|The cocycle formula gives φ=u on ker χ.|B.4.1–B.4.2|None.
I.P06|PROVED|ker χ∩ker φ=ker χ∩ker u and χ descends along u exactly when ker u⊆ker χ.|B.4.2|None.
I.P06|REFUTED|ker u=ker χ∩ker φ follows from the displayed formula alone.|B.4.2, explicit C_2 counterexample|The missing containment must be established in any intended application.
I.P07|PROVED|Integral specialization CH^r(X_η)→CH^r(X_s) is a ring homomorphism for X smooth over a DVR.|F.3.8; Fulton Proposition and Corollary 20.3, pp.398–399|Integral coefficients and the closure multiplicities are retained.
I.P07|PROVED|For a complete DVR and ℓ invertible there, geometric specialization commutes with the integral ℓ-adic cycle class.|F.3.8; Fulton Example 20.3.5, p.400|Smooth proper hypotheses give the cohomology specialization isomorphism.
I.P07|READING|The annotated fallback uses raw cycles and inserts the smooth proper hypothesis.|Frozen witness 18/007:L10–17|The historical caveat remains even after a modern proof in the stated DVR setting.
I.P08|READING|The same sheet weakens the assertion to a tentative expectation.|Frozen witness 18/007:L10|No revision chronology beyond the recorded insertion/deletion is inferred.
I.P08|PROVED|The weakened wording is compatible with the raw-cycle square and does not refute integral Chow specialization.|F.3.8; Fulton 20.3|The historical wording is retained; the modern theorem is separately proved.
I.P09|REFUTED|A Tate twist leaves the weight-graded index unchanged.|F.2.1, E=Q(0), n=−1|Use Gr_i^W(E(n))=(Gr_{i+2n}^W E)(n).
I.P09|PROVED|The weight and Hodge filtration shift by 2n and n respectively under E(n).|F.2.1|None.
I.P10|PROVED|Fil and Big are the flag and splitting homogeneous spaces with dimensions u and 2u.|A.1.1|Use the stated pure semisimple category and its type/reflex-field forms.
I.P10|PROVED|Big→Fil is a torsor under a relative varying unipotent group, with U on a chosen fibre.|A.1.1|A globally fixed U-action is not supplied by the homogeneous construction.
I.P10|PROVED|g=l+2u and b=l+u for the cocharacter parabolic and its Levi.|A.1.1|Mixed nonreductive categories require another argument.
I.P11|PROVED|Normalized splitting space Q has dimension u; the expanded H′ space has dimension u+1 with its Tate parameter.|A.1.2|Retain the parameter and distinguish the two actual maps.
I.P11|PROVED|The expanded space maps to the Tate image T_0 with fibre Q.|A.1.2|The identification T_0≃G_m depends on the specified embedding.
I.P12|PROVED|The flag type and bigrading type descend to the appropriate reflex/type field or finite union over Q.|A.1.1|Do not assume each chosen connected type is a Q-form.
I.P12|READING|The margin's coefficient field and equivariance formula have diplomatic alternatives.|Frozen witness 18/011:L14–23|The mathematical form construction does not decide the ink.
I.P13|PROVED|The natural margin morphism is the forgetful map Big→Fil.|A.1.2|None.
I.P13|REFUTED|A canonical equivariant inverse or section Fil→Big exists when u>0.|A.1.2, Levi/parabolic obstruction and GL_2 example|The reverse reading only yields a map of types, not the asserted section.
I.P14|PROVED|A filtration-splitting cocharacter has a Levi centralizer and is central in that Levi.|A.1.1; F.3.3|It need not be central in the full group.
I.P14|REFUTED|The splitting j with εj=id can be identified with the central cohomological weight cocharacter.|F.3.3, GL_2 matrices and εw=t²|Specify the Tate exponent and group containing the cocharacter.
I.P15|REFUTED|The joint splitting/period field always has transcendence degree g+u.|A.2.5–A.2.6|Real non-CM elliptic curves have joint field k(α), so the universal extra u fails.
I.P15|PROVED|The algebraic image dimension is g+v for the exact joint-conjugate parameter 0≤v≤u.|A.2.2|Equality at the arithmetic comparison point is a separate period-genericity assertion.
I.P16|PROVED|The maximally large composite degree forces the proposed smaller degrees by image bounds and field towers.|A.2.4|This is the stated implication; it does not establish its premise.
I.P16|PROVED|The exact corrected relative image dimensions are v,b+v,u for K/α,K/β,K/γ.|A.2.2–A.2.4|Actual-point equalities require the named genericity input.
I.P17|REFUTED|The uppercase-K denominator can be used literally for the requested relative transcendence degrees.|A.1.2|It either is ill-typed or collapses the numerator field over itself; the lowercase-k reading is separately stated.
I.P17|READING|The lowercase k and uppercase K readings remain transcription alternatives.|Frozen witness 18/011:L65–76; original cote18 PDF11/archive p.10, lower crop at300dpi|Two independent visual inspections favor uppercase K in the first two consequence denominators: their straight stems and rightward arms differ from the rounded lowercase k in the boxed base field and third consequence. This qualified glyph preference does not prove field containment. Both mathematical readings and A.1.2 remain recorded.
I.P18|READING|The whole normalized-period draft on 18:12 is cancelled.|Frozen witness 18/012:L2–24|Do not infer a revision chronology or rejection of truth from adjacency to live sheets.
I.P18|OPEN|The cancelled normalized period degree is dim G−1 with only the normalization relation.|A.2.4; A.4.9|The normalization symbol and arithmetic independence are not established by the draft.
I.P19|PROVED|A point with full normalized Zariski locus generates that normalized algebraic group.|A.4.9; A.5.1|This is the locus-containment implication, not the arithmetic premise.
I.P19|OPEN|Semisimplicity and transcendence of π alone prove the cancelled full-group generation claim in its undefined normalization.|F.3.5; A.1.2|Specify the point, normalization, central quotient, and Tate character before the literal general assertion is defined.
I.P19|PROVED|The specified full elliptic period locus generates its motivic torsor.|A.4.9|No equality of that locus with the torsor is inferred.
I.P20|OPEN|Four normalized non-CM elliptic periods have transcendence degree 3 with determinant one the sole relation.|A.4.9; G, Grothendieck 1966 p.102 note 10|This full normalized period-independence assertion is not proved here and is excluded as a target A.4(a).
I.P20|PROVED|Schneider's theorem gives the algebraic-period-ratio CM criterion used for the flag field.|A.3.1|It does not by itself supply the full normalized degree 3 assertion.
I.P21|OPEN|Adjoining transcendental j to the normalized tuple gives the cancelled total degree 4.|A.5.4; D.5.4|The undefined pre-minimal condition and base-field quantifiers must be fixed; the universal unqualified version has the counterexamples cited.
I.P21|REFUTED|The extra condition π transcendental over k suffices for every proposed full period or openness conclusion.|D.5.4|The exact Tate counterexample retains the stipulated transcendence.
I.P21|READING|The margin contains an algebraic-τ special case and a deleted question concerning π over k.|Frozen witness 18/012:L23,L25–26|The normalization and intended scope remain undecided.
I.P22|PROVED|For a single CM elliptic curve over Qbar the full period field has transcendence degree 2.|A.4.3; A.2.7|This theorem is not generalized to arbitrary CM products.
I.P22|OPEN|For a non-CM elliptic curve the full period field has transcendence degree 4.|A.4.9; G|Excluded target A.4(a); neither torsor generation nor flag transcendence proves it.
I.P23|PROVED|Translating the period locus by an algebraic point defines the algebraic subgroup and torsor it generates.|A.4.9|Existence of the algebraic point follows from nonempty finite-type Qbar locus.
I.P23|PROVED|For one elliptic curve that generated torsor is the full motivic torsor.|A.4.9, Kreutz–Shiga–Vignéras theorem in the manuscript's exact version|No full period-genericity consequence is asserted.
I.P24|OPEN|An algebraic Hodge splitting for a non-CM elliptic curve over Qbar is impossible.|A.4.1, A.4.8, A.4.10–A.4.13|Exact remaining obligation is transcendence of the splitting scalar, equivalently the stated χ* value; the functional theorem does not prove that specialization.
I.P24|PROVED|The scalar/formula reduces the manuscript's question to Katz's specified algebraicity question.|A.4.1; A.4.8|No priority or historical dependency claim follows.
I.P25|PROVED|A CM elliptic curve has an algebraic Hodge splitting because its CM eigenspaces are algebraic.|A.4.2|None.
I.P25|PROVED|The CM splitting can be nonzero; zero has the classified special j-invariants.|A.4.4–A.4.7|The phrase algebraic does not mean zero in a chosen de Rham basis.
I.P26|PROVED|The Legendre relation supplies the Tate determinant and a specified normalization can remove it.|A.1.3; A.4.1; G|This calculation does not identify the unknown handwritten normalizing symbol.
I.P26|READING|The ζ/ξ, square-root, and pre-minimal/pre-maximal readings are unresolved.|Frozen witness 18/012:L5–9,L15–22|Need the missing definition or original witness; preserve both alternatives.
I.P27|PROVED|The local residue/Thom comparison gives the cycle factor (2πi)^p in de Rham-to-Betti direction.|F.1.1|Use the inverse factor for α in the manuscript's direction.
I.P28|PROVED|A smooth transversal meeting a codimension-p subvariety at an isolated transverse point has dimension p.|F.3.9, tangent-space dimension calculation|The formula uses ordinary complex dimensions.
I.P28|READING|The frozen transversal is labelled X′ of dimension n−p.|Frozen witness 18/015:L19; original cote18 PDF15/archive p14 at170dpi|Original scan independently inspected by root and period_triangle: codimension p and the written exponent n−p are clear, while n is not defined on the leaf. The ordinary dimension calculation in F.3.9 gives p; retain the written label and its unstated intended convention.
I.P29|PROVED|Proper Gysin of relative codimension p shifts degree by 2p and gives α_Y f_*=(2πi)^−p f_* α_X.|F.1.2|Retain dimensions, sign convention, and Tate target.
I.P29|REFUTED|The displayed global codimension-p Gysin map has shift p in ordinary singular-cohomology grading.|F.1.2; frozen witness 18/017:L21–25|The earlier local 2p is the ordinary degree; retain an unspecified regrading as a reading possibility.
I.P30|PROVED|The local residue calculation extends to one universal scalar λ=2πi, with its p-th power in codimension p.|F.1.1|Local orientation, products, supports, and extension across singular loci are all verified there.
I.P30|PROVED|The local-to-global comparison commutes with support maps and gluing, and yields the complete Gysin diagram.|F.1.1–F.1.2|None in the stated smooth ambient setting.
I.P30|READING|The uncertain marginal request for reasoning and the unfinished global-commutativity sentence are completed in the witness.|Frozen witness 18/015:L20 and 18/017:L2,L25|They remain incomplete documentary evidence; the proof is supplied separately.
I.P31|PROVED|The abstract integral Betti module and its comparison embedding have the stated Tate scaling.|B.3.1; F.1.4–F.1.6|Record both module and actual embedded lattice.
I.P31|REFUTED|The unscaled integral lattice is universally equal to the algebraic de Rham lattice.|B.3.1, P^1 example|The comparison coefficient (2πi)^−1 is retained.
I.P32|PROVED|The two-splitting construction yields the displayed cocycle once the compatibility equation is imposed.|B.4.1|The compatibility equation is explicitly separate from centralization.
I.P32|REFUTED|Centralizing the two chosen subtori by itself implies their claimed equality.|B.4.1, explicit C_2 example|The additional compatibility map must be checked.
I.P33|PROVED|A continuous finite-dimensional p-adic image of a profinite group is a compact p-adic analytic group.|B.4.3|All primes, including 2; finite dimensionality is essential to this argument.
I.P33|REFUTED|Sen's inertia statement implies that the entire Galois image has algebraic Lie algebra in the asserted generality.|B.4.3, unramified Q_5 example|Keep inertia and full Galois image separated by the actual restriction map.
I.P33|REFUTED|The same analyticity conclusion holds for an unrestricted proalgebraic realization image.|B.4.4, unramified Artin tower plus Tate character|The exact natural semilinear extension has both required splittings and image Z_ell times Z_p^times; its inverse-limit topology has no open pro-p subgroup for ell not equal to p. Every finite object is crystalline.
I.M01|PROVED|The usual pure-motive construction specifies cross-variety correspondences, composition, tensor product, summands, and twists.|F.3.4; F.1.3|None for the named modern categories.
I.M01|DOCUMENTARY-GAP|The historical category used on these sheets was constructed from the earlier Lefschetz operator rings.|F.3.4; supplied witness|The pages use the category without the required construction; need the missing construction and its maps.
I.M02|PROVED|The Lefschetz sl_2 action on H^1 of an elliptic curve is zero while the specified standard period SL_2 action is nonzero.|F.3.3|The conclusion concerns these representations and is proved by their operators.
I.M03|PROVED|A tensor-compatible weight grading corresponds to a central cocharacter.|F.3.3; Deligne–Milne Definition 5.1|None.
I.M03|PROVED|εw=t² for the cohomological weight convention, whereas the specified splitting satisfies εj=t.|F.3.3|A change of Tate convention reverses both signs consistently; it does not remove the factor 2.
I.M03|PROVED|The cohomological, Cartan, and filtration-splitting gradings have the displayed comparison maps.|F.3.3|The unspecified historical lift still needs its intended group.
I.M04|PROVED|The operational manuscript A and C match printed Lefschetz A and inverse-Lefschetz B respectively.|F.3.5; Grothendieck 1969 pp.195–197|This matches the operational statements, not every unidentified occurrence of a letter.
I.M04|DOCUMENTARY-GAP|Manuscript B and D have securely identified standalone definitions matching printed D and C.|F.3.5; original cote 14 pp.43–44; complete Coates letters of 1966 and 1967|The 27 August 1965 letter explicitly defines B by positivity on cycles modulo algebraic equivalence. Its cycle-class quotient to cohomological algebraic classes is constructed. The particular B and D in the 1967 Coates letter still lack standalone definitions in the inspected text; no uniform dictionary is inferred from the letters alone.
I.M05|DOCUMENTARY-GAP|Cote 14 carries out the suggested singular-hypersurface reduction.|Supplied context 16:47; complete Coates 1967 letter p.4; F.3.14; original cote14 PDFs111–113 and131|The normalization map from every smooth integral projective variety to an integral hypersurface is constructed in F.3.14, with an exact nodal-cubic cohomology comparison. Original cote14 PDFs111–113 contain cycle-Lefschetz and punctured-cone formulations; PDF131 has a generic-member/base-locus diagram. These inspected pages have not identified the proposed historical standard-conjecture reduction. That documentary execution remains open.
I.M05|READING|The proposed smooth-hypersurface reduction is withdrawn because of the simply-connected obstruction.|Supplied context 16:47|No later construction is inferred from the distinct smooth-projective archimedean question.
I.M06|PROVED|The local extension has kernel G′(C), quotient π, and the two splitting maps used in B.|B.4.1|Its literal kernel and quotient are retained.
I.M06|PROVED|Rational Nori motivic Galois groups have the exact arithmetic base-change sequence with proconstant Galois quotient.|F.3.4; Kahn 2025 Theorems 5.10 and 10.2|No canonical split or identity-component identification is supplied.
I.M06|DOCUMENTARY-GAP|The local displayed sequence itself is a written proof of the arithmetic motivic sequence.|F.3.4; typed local and arithmetic arrows|The witness contains no functor identifying those sequences; the modern arithmetic theorem provides a separate stated comparison.
I.M07|PROVED|Ayoub's and Nori's Betti Hopf algebras are identified by inverse constructed maps for principal ideal coefficient domains.|F.3.4; Choudhury–Gallauer Theorem 9.1|Keep the fixed embedding and coefficient hypotheses.
I.M07|PROVED|The pure rational Nori category is equivalent to the André motivated category.|F.3.4; Arapura Theorem 6.4.1|Algebraic correspondences map to motivated correspondences under the specified functor.
I.M07|OPEN|Every motivated correspondence is represented by an algebraic cycle in the general categories at issue.|C.1.2; F.3.4–F.3.5|The corresponding standard/Hodge cycle-surjectivity obligations remain.
I.M08|PROVED|Hodge realization is full on the specified pure abelian Nori/André subcategory.|F.3.4; Arapura Corollary 7.1.4; C.1.1|Retain the real descent data in C.1.1 when over R.
I.M08|OPEN|The analogous general Nori Hodge realization is full with a characterized essential image.|F.3.4; Arapura Conjectures 7.1.1–7.1.2|General fullness and the unspecified essential image remain unresolved.
I.M09|OPEN|The manuscript's integral fibre-functor forms satisfy a finiteness theorem.|F.3.12; F.3.13; Gille–Moret-Bailly Proposition 5.1; Borel 1963 Theorem 5.1|The arithmetic finiteness theorem, tensor-torsor equivalence, adelic-genus map, and closed finite-presentation automorphism model for an admissibly generated integral stage are proved. The remaining historical gate is identification of the particular M_alpha with that exact category. Over S-integers fpqc locality already implies fppf locality. Unrestricted proalgebraic finiteness has the explicit product-mu_2 counterexample.
I.M09|PROVED|The abelian characteristic-p Dieudonné realization and the mixed-characteristic integral local categories have the specified data.|F.3.1; B.1.5; B.2.3|This proves the named comparison categories only.
I.M09|OPEN|Arbitrary positive-characteristic crystalline points classify the proposed integral motives.|B.3.4; F.3.4|Specify geometric essential image and the F,V,filtration conditions; no such global classification is proved.
I.M10|PROVED|Homological equivalence maps to numerical equivalence by the quotient on cycle classes.|F.3.5|None.
I.M10|PROVED|Rational numerical motives are semisimple.|F.3.5; Jannsen Theorem 1|This theorem does not create a cohomology realization on the quotient.
I.M10|OPEN|Cohomology factors through numerical motives in the full proposed generality.|F.3.5|Exactly the kernel-annihilation condition, equivalently numerical=homological on the relevant correspondence classes, remains.
I.M11|REFUTED|Fixed normalized SL_2 data determine the full GL_2 group and its Tate character uniquely.|F.3.5, GL_2 versus G_m×SL_2|Their explicit central isogeny squares the Tate coordinate, displaying the missing data.
I.M11|PROVED|Full-group generation must retain the central Tate character and its normalization.|F.3.5; A.1.2; A.4.9|The literal undefined normalization remains as in I.P26.
I.B01|PROVED|Tate's finite-field Hom theorem identifies the integral Hom module with Galois-equivariant Tate-module maps.|F.3.6; Tate 1966 Main Theorem|The prime is different from the field characteristic.
I.B01|PROVED|Mochizuki's sub-p-adic curve Hom theorem identifies dominant morphisms with the specified open fundamental-group homomorphisms.|F.3.6; Mochizuki Theorem A|Keep openness, geometric-inner quotient, and stated curve/base hypotheses.
I.B01|PROVED|The relation between these nonlinear and linear maps is geometric abelianization followed by the Albanese/Jacobian map.|F.3.6|Not every Jacobian map is a curve map; multiplication by 2 provides the specified counterexample.
I.B02|REFUTED|Semisimplicity of the representation category forces a trivial centre.|F.3.5, Rep(G_m)|The character decomposition and the conjugation kernel are explicit.
I.B02|PROVED|For centre-free geometric curve groups, the arithmetic extension is the pullback of Aut→Out along the outer Galois action.|F.3.6; Mochizuki Lemma 1.3.1 and Corollary 1.3.2|This uses centre-freeness, not semisimplicity of a linear category.
I.B03|PROVED|A real algebraic Tannakian category is polarizable exactly when its band has a compact real form in the stated theorem.|F.3.7; Deligne–Milne Theorem 4.17(a)|Retain the theorem's algebraic real-category scope.
I.B03|PROVED|Real hyperbolic-curve sections recover connected components of the real locus.|F.3.6; Pál Theorem 1.3 and Example 5.8|They are component classes, not all individual real points.
I.B03|PROVED|The positive Weil form in the real motivic comparison is constructed by the stated involution.|C.5.1; F.3.7|The real involutions alone are not used as an unexplained polarization.
I.B04|PROVED|Number fields have Stix's non-Tate-weight property for abelian Tate modules.|F.3.6; Stix Definition 26 and its following example|The good-prime Frobenius-weight argument gives the required Hom vanishing.
I.B04|PROVED|Cyclotomic normalization in Stix includes both open arithmetic image and the cyclotomic character action.|F.3.6; Stix Definition 29|Both premises are necessary to apply the cited characterization as stated.
I.B04|PROVED|The nontrivial closed pro-ℓ subgroups of geometric π_1 with that normalization are exactly subgroups of cusp inertia.|F.3.6; Stix Theorem 30|Keep the non-Tate and curve hypotheses.
I.B05|REFUTED|The truncated LM6 A.50 proof supplies the missing cyclotomic-character step for LM6 A.22.|F.3.10; full LM6 A.50 pp.33–34 and A.22 pp.16–17|The complete source is obtained and checked with the exact enlargement N to NA. Its noncuspidal alternative produces a weight-one Jacobian character, not the cyclotomic character; the common-kernel subgroup obligation of A.22 remains open.
I.B05|READING|LM6 A.22 and A.50 keep their register statuses rather than acquiring referee-approved status here.|Full LM6 archive and results-state register; F.3.10|A.50 has now been independently checked after the explicit N to NA repair, without changing its hypotheses. A.22 retains its Open status; no independent proof of all later LM6 restrictions is claimed.
I.X01|PROVED|The displayed elliptic family has classical j=1728t and the stated nonzero discriminant off its excluded parameters.|E.3.1|Retain normalized versus classical j.
I.X02|PROVED|The labelled integral Hodge realization of an elliptic curve determines its complex torus and j.|E.3.1|The rational Hodge realization gives the isogeny class instead; the precise integral map is used.
I.X02|PROVED|An integral Hodge isomorphism and the rational version have their respective lattice and isogeny consequences.|E.3.1; D.5.2|Do not replace an embedded integral lattice by its rational span.
I.X03|PROVED|Agreement on all labelled elliptic-family integral Hodge tests forces equality of the field embeddings.|E.3.1|The common labels and the Hodge data are essential to the argument.
"""

DATA += r"""
II.C01|PROVED|The untwisted codimension-p cycle comparison under σ:C→k has scalar σ(2πi)^−p.|F.1.1; F.1.4|None.
II.C01|PROVED|The same factor is global and valid for singular algebraic cycles in a smooth ambient variety.|F.1.1|None.
II.C02|PROVED|Changing σ to σc multiplies a codimension-p cycle class by (−1)^p.|F.1.4|None.
II.C02|REFUTED|That change always supplies one minus sign, independent of p.|F.1.4, point class in P^2|The single minus is valid for the adjacent p=1 example and other odd p.
II.C03|PROVED|The support-to-ordinary cohomology arrow is the natural localization map and commutes with comparison.|F.1.1|None.
II.C03|READING|The faint arrow or equality sign on 18:21 is securely deciphered by the mathematics.|Frozen witness 18/021|It is not deciphered; retain the diplomatic alternatives.
II.C04|PROVED|A proper morphism of relative codimension p has Gysin degree shift 2p and comparison factor (2πi)^−p.|F.1.2|All r, including odd r and negative p, are included with the stated dimensions.
II.C04|PROVED|The Gysin comparison is compatible with composition and its exponents add.|F.1.2|None.
II.C05|PROVED|Correspondence action is p_2*(p_1* x cup cl(z)) of degree 2r−2dim X.|F.1.3|Retain target Tate twist r−dim X.
II.C05|PROVED|The cycle and projection scalars cancel for degree-zero correspondences and after the indicated general twist.|F.1.3|None.
II.C05|READING|The handwritten exponent and last Ω-subscript are unambiguous.|Frozen witness 18/025; F.1.3|They remain recorded readings; the typed correction is proved separately.
II.C06|PROVED|Changing i to −i reverses the oriented P^1 generator and the comparison scalar together.|F.1.1; F.1.4|The unoriented embedded lattice is unchanged.
II.C06|PROVED|ξ(Z(−1)) is the rank-one Tate lattice with its specified comparison coefficient.|A.1.3; F.1.1|No unscaled identification is inserted.
II.C07|PROVED|As complete archimedean topologies vary, comparison generators of the P^1 line are exactly the vectors with transcendental coefficient.|F.1.5|The base is an abstract field isomorphic to C.
II.C07|REFUTED|Every nonzero vector of the one-dimensional de Rham line is such a comparison generator.|F.1.5, coefficient 1|Algebraic nonzero coefficients do not occur.
II.C07|PROVED|For a fixed cyclic lattice the primitive elements are its two generators.|F.1.5|Primitive requires that lattice to be specified.
II.C07|READING|The word primitifs or possibles is fixed by this calculation.|Frozen witness 18/029|Both readings remain; their mathematical interpretations are separately resolved.
II.C08|PROVED|The embedded diagonal integral Betti lattice is stable under real Galois action in the finite and de Rham factors.|F.1.6|Use the rational real Frobenius on Betti and semilinear descent on de Rham.
II.RH03|PROVED|Two compatible complex identifications for one complete archimedean topology differ by identity or conjugation.|C.4.1|This is the fixed-topology statement, not all abstract field automorphisms.
II.RH03|PROVED|The transported Hodge decomposition changes by the indicated semilinear map and interchange of Hodge indices.|C.4.1; C.1.1|None.
II.RH04|PROVED|The two real involutions commute and f_∞ is their rational linear quotient under comparison.|C.1.1; C.2.1; B.3.2|Keep coefficient conjugation and rational real Frobenius typed separately.
II.RH04|PROVED|The twisted real form is V^+⊗R plus iV^−⊗R inside V_C.|C.2.1|None.
II.RH04|PROVED|Integral Betti–étale comparison identifies the relevant finite realizations and real action.|D.1.1; F.1.6; SGA 4 XVI Theorem 4.1|Use finite torsion coefficients and inverse limit as stated.
II.RH05|PROVED|The real Hodge realization of the specified abelian absolute-Hodge category is full and faithful.|C.1.1|The functor retains the involution and morphism compatibility.
II.RH05|OPEN|The analogous algebraic-cycle homological realization is full for all motives without a cycle-surjectivity premise.|C.1.2|The precise Hodge-cycle surjectivity on tensor constructions is the remaining obligation.
II.RH05|PROVED|The group is generated by its connected component and the real Frobenius in the specified category.|C.1.3|No statement for an arbitrary undefined motivic category is inferred.
II.RH06|PROVED|The vector-space projection V^+ plus V^−→V^+ plus iV^− has the computed minus-times-minus tensor defect.|C.2.1|The corrected tensor constraint and Isom torsor are retained.
II.RH06|PROVED|The corresponding fibre-functor torsor is the inflation of the real C_2 cocycle to Q(i).|C.2.1|A point requires triviality of that actual torsor class.
II.RH07|PROVED|For the nontrivial real Artin character the torsor is x²=−1 and has no Q-point.|C.2.2|This is an explicit obstruction on the Artin subcategory.
II.RH07|PROVED|For a pure Tate category the torsor is trivial, with the computed tensor-compatible choice.|C.2.2|The naive projection need not be the compatible choice.
II.RH07|PROVED|Non-CM and CM elliptic tests have the stated distinct torsor outcomes via their actual tensor subcategories.|C.2.2|The CM obstruction is detected by the indicated Artin summand.
II.RH08|REFUTED|Cohomology of X(R) always equals the conjugation invariants in H*(X(C),Q).|F.3.7, P^1_R and Spec C/R|The restriction maps in both counterexamples are computed.
II.RH08|PROVED|For P^1_R the conjugation quotient is a closed disk with rational cohomology equal to the invariant part.|F.3.7, sphere-to-hemisphere quotient map|This calculates the quotient example actually asserted by the note.
II.RH08|READING|The superscript star or zero and the intended fixed-locus versus quotient convention are undecided.|Frozen witness 18/035:L13–21 and 18/040:L21–28|Both counterexamples retain the diplomatic alternatives rather than assigning a new meaning to the manuscript.
II.RH09|PROVED|The actual period comparison α has real coefficients exactly when f_∞=1.|C.3.2|This is a statement about the actual comparison point.
II.RH09|PROVED|The existence of a real point of the comparison torsor means triviality of its real torsor class and need not make α real.|C.3.2|The torsor point and the specified comparison point are different maps.
II.RH10|REFUTED|Only sums of even Tate powers have f_∞=1.|C.3.1, odd Artin–Tate example|The tensor sign computation supplies the counterexample.
II.RH10|PROVED|In the specified real abelian absolute-Hodge category, f_∞=1 exactly for the stated Artin–Tate sums.|C.3.1|Retain that category and its real descent involution.
II.RH11|PROVED|An abstract quotient G_m does not by itself specify the image of f_∞.|C.3.1; F.3.5|On μ_2×G_m the characters (a,t)↦t and (a,t)↦at have different real signs.
II.RH12|PROVED|Central f_∞ has the Artin–Tate characterization in the stated categories.|C.3.3|The homological version has the separately stated fullness hypothesis.
II.RH12|READING|The expression Q tordu has one uniquely established tensor-category meaning in the witness.|Frozen witness 18/037:L16–21|Its readings are retained and matched to the explicit Artin–Tate construction.
II.RH13|REFUTED|The raw centralizer or two-element normalizer of the Weil element in G(R) is always compact.|F.3.7, pure Tate G_m|The weight torus itself is the explicit noncompact subgroup.
II.RH13|PROVED|After the weight quotient in the polarizable setting, C²=1 and its centralizer is maximal compact on each finite tensor-generator quotient.|F.3.7|The positive-form proof supplies the needed hypotheses and actual subgroup.
II.RH13|READING|The maximal-compact paragraph and its change from G to G/im(w) are withdrawn on the sheet.|Frozen witness 18/038:L20–44|The modern proof does not reverse the recorded cancellation.
II.RH14|PROVED|Betti and de Rham real structures are related by κ_D=α f_∞ κ_B α^−1.|C.2.1; C.4.1; B.3.2|None.
II.RH14|PROVED|The de Rham Hodge splitting β is R-rational and R(γ)=R(α).|C.4.2; F.3.7|This does not establish Qbar-rationality of β.
II.RH15|PROVED|The Hodge (p,q) summand belongs to total degree p+q with the typed comparison target.|A.1.1; C.4.1|None.
II.RH15|READING|The doubtful total-degree superscript is decided by direct scan inspection.|Frozen witness 18/041|No such inspection occurred; retain the alternative and the typed mathematical formula.
II.RH16|PROVED|The intersection of all real closures determined by complex embeddings is the totally real algebraic subfield in the stated sense.|C.4.1|Use the exact scalar-field intersection and embeddings specified there.
II.RH17|PROVED|Problem 3 has the stated p-adic period-ring, good-reduction, semistable, and relative comparisons.|B.3.3; B.2.1–B.2.3|The appropriate extra structures and coefficient rings are retained.
II.RH17|PROVED|Problem 4 has the characteristic-p crystalline, rigid, and prismatic structures within their exact hypotheses.|B.3.4|No undeclared geometric essential-image classification is inferred.
II.RH18|PROVED|A[p] determines the canonical characteristic-p de Rham Hodge extension for an abelian variety over a perfect field.|F.3.1|This is Oda's canonical module comparison, not a canonical vector-space splitting.
II.RH19|PROVED|The stated Weil form is positive definite after the prescribed involution and sign normalization.|C.5.1|Its scalar Tate value is normalized exactly as in that proof.
II.RH20|PROVED|Real hyperbolic-curve section classes recover real connected components.|F.3.6; Pál Theorem 1.3|Individual points are not recovered by the component set.
II.RH20|PROVED|The conjugation action on geometric abelianization is independent of the section class.|F.3.6, inner-conjugation calculation|The full abelianized extension or section cocycle can contain more data; only the action is computed.
II.P01|PROVED|The Betti–de Rham comparison, including real structures and splittings, is constructed with the stated dependence on topology.|A.1–A.2; B.3.1–B.3.2; C.4|The original question status remains part of the witness.
II.P01|PROVED|The Betti–ℓ-adic comparison and embedded integral lattices have the exact coefficient maps in D.|D.1.1; F.1.6|The original question status remains part of the witness.
II.P01|PROVED|The de Rham–p-adic comparison has the specified admissible period-ring constructions.|B.2.1–B.2.3; B.3.3|These constructions are supplied here, not read into the historical sheet.
II.P01|PROVED|Characteristic-p cohomology has the listed crystalline, rigid, and prismatic realizations with their exact hypotheses.|B.3.4; F.3.1|The question marks in the witness are retained.
II.P02|PROVED|For two non-CM geometrically nonisogenous elliptic curves, the product motivic group has dimension 7 and the product parabolic dimension 5.|D.2.1; D.3.2|CM or isogenous cases need their different groups; the numerical assertion is not unconditional in E,E′.
II.P02|PROVED|The written filtration map has a geometric source and target of the displayed dimensions.|D.2.1; A.1.1|These dimensions alone do not compute the undefined coefficient field K.
II.P03|DOCUMENTARY-GAP|The field K on 18:45 is defined well enough to test the numerical value 6.|D.2.1|Its generators and base field are absent; retain the exact source gate.
II.P03|REFUTED|Lead H5 validly refutes the full period conjecture from the displayed number 6.|D.2.1|The omitted field definition prevents that inference.
II.P04|PROVED|The simultaneous relative quotient has dimension at most (n−1)dim G with the stated exact quotient map.|D.1.2|Actual transcendence-degree equality requires the corresponding genericity input.
II.P05|PROVED|The finite coefficient rings Q⊗Zhat, A_f, and the full product of Q_ℓ have the exact embeddings specified in D.|D.1.1|Do not use an unqualified product sign for all three.
II.P05|REFUTED|The full product of Q_ℓ can replace the restricted finite adeles in the compact-open arguments.|D.1.1, additive-group and tuple (1/ℓ) tests|The compact-open and integrality conditions require the restricted product.
II.P06|REFUTED|The general strengthened Tate statement gives finite-index adelic image for the entire motivic group.|D.4.2, the actual Tate motive Q(-2)|With its stated integral group model G_m, the image is (Zhat^times)^2, of infinite index by the square-class quotient at arbitrarily many odd primes. The map from the Q(-1) tensor group is explicitly t to t^2. D.3.2 retains the named elliptic open-image cases.
II.P06|PROVED|The stated non-CM elliptic and independent-product cases have the requisite open images.|D.3.2|All named hypotheses of the opened theorems are retained.
II.P07|PROVED|Every coset of an open compact subgroup contains a point generic over a countable coefficient field.|D.3.1|The proof uses the exact adelic setting and Baire/measure argument stated there.
II.P07|PROVED|The same argument gives simultaneous genericity against the specified countable family.|D.3.1|None.
II.P08|PROVED|For G_m the generic-coset argument can avoid each countably many polynomial zero conditions inside the indicated unit neighbourhood.|D.3.1|This is the torus instance, not density of Q×.
II.P09|REFUTED|Diagonal Q× is dense in A_f×.|D.4.1, explicit neighbourhood obstruction|The restricted multiplicative topology and global rational unit constraints are retained.
II.P09|PROVED|The connected affine groups satisfying the approximation property have the criterion stated in D.|D.4.1|The reductive/unipotent quotient and simply connected covers are handled by the cited exact criterion.
II.P10|PROVED|Plain integral comparison data do not universally recover an archimedean place, even with all specified tests.|E.2.1; D.6.1|The concrete pair of places and compatible comparison maps are constructed.
II.P10|READING|The est/pas reading in the place-dependence sentence is resolved by the counterexample.|Frozen witness 18/051; original cote18 PDF51/archive p.50, lower crop at300dpi|Two independent inspections of the original full page and lower crop do not securely distinguish est from pas. The clear est above supplies a comparison but does not settle the disputed stroke. Both readings and their mathematical analyses are retained; the counterexample does not decide paleography.
II.P11|PROVED|The margin equivalence is true for the precise two-input formulations stated in D.|D.4.2|The exact subgroup and closure conditions must be included.
II.P11|REFUTED|The broader reading of that equivalence without those inputs is universally true.|D.4.2, explicit counterexamples|The proof identifies the failed implication for each reading.
II.P12|PROVED|Restriction Aut(k/k_0)→Gal(k_0bar/k_0) is surjective with kernel Aut(k/k_0bar) in the stated algebraically closed setting.|D.5.1|No topology is suppressed.
II.P12|PROVED|For positive transcendence degree the pointwise topology on the abstract automorphism group need not be compact.|D.5.1|The translation family gives the explicit obstruction.
II.P13|PROVED|A fixed integral comparison matrix maps diagonally through Z→Z_ℓ and its ambiguity is determined by that integral structure.|D.5.1; D.1.1|This computes the map after a comparison exists.
II.P13|REFUTED|Such an integral comparison exists for every pair of relevant places or elliptic realizations.|D.5.2|The CM ideal-class example gives the exact obstruction.
II.P14|PROVED|The fibre stabilizer is Γ∩{id,c_v}; its cardinality is one or two according to the base-fixing condition.|D.5.1|The erased universal cardinality two is replaced by this exact formula.
II.P14|READING|The fibre-cardinality-two passage is cancelled.|Frozen witness 18/057|Cancellation is retained.
II.P15|PROVED|The two multiplication conventions are related by inversion and have the specified cocycle equations.|A.5.3; D.5.1|Do not interchange left and right cocycles without this conversion.
II.P16|PROVED|The actual tensor-Isom scheme descends as the stated fpqc torsor.|A.5.1; D.5.1|Use effective algebraic descent, not arbitrary set-theoretic Aut(k/k_0) data.
II.P16|REFUTED|An arbitrary abstract automorphism descent datum on the unspecified object is effective algebraic descent.|F.3.11, discontinuous action on a two-point finite etale scheme|The exact semilinear action uses a discontinuous quotient of the multiquadratic Galois group and cannot descend. The actual tensor-Isom fpqc torsor of II.P16.01 remains proved; it is not identified with the counterexample.
II.P17|PROVED|Genericity over k_0 and closedness after scalar extension to k are related by the exact period-locus base-change maps.|A.5.1|Keep the base fields in each closure.
II.P18|PROVED|For φ(σ)=(σg)^−1g the orbit map x↦x^−1g has inverse y↦gy^−1, giving the exact image-locus formula.|A.5.1|None.
II.P18|PROVED|The resulting locus formula gives the precisely stated density criterion.|A.5.1|It is a criterion, not proof that every arithmetic point meets its genericity premise.
II.P19|PROVED|A field of definition can absorb a transcendental comparison parameter even for a genuine motive.|A.5.4; D.5.4|The explicitly constructed elliptic/Tate examples determine the resulting cocycle image.
II.P19|REFUTED|The unfinished π qualification is sufficient for the universal intended conclusion.|D.5.4|The displayed strengthened counterexample preserves π transcendental over the chosen field.
II.P20|PROVED|The cocycle defines a homomorphism only after passage to the stated semidirect product.|A.5.3|The group law and action are explicit.
II.P20|REFUTED|The same cocycle is automatically a homomorphism into G with its ordinary multiplication.|A.5.3, translation example|The cocycle action cannot be omitted.
II.P21|REFUTED|The Euclidean/adelic closure of the image is universally open as expected in the sheet.|D.5.3, Tate counterexample|The exact remaining elliptic image question is separately recorded there.
II.P22|PROVED|Changing the place changes the cocycle by the explicitly computed cochain/conjugacy transport.|D.5.1|The chosen identifications are included in the formula.
II.P23|DOCUMENTARY-GAP|The condensed Hua synopsis contains a complete proof of all its descent, action, and density assertions.|A.5.1–A.5.3; D.5.1|Only its fully stated components are proved; obtain any missing quantified statement before assigning a theorem status.
II.P24|PROVED|The Bost–Charles tensor-Isom torsor construction gives the stated algebraic maps and orbit closure.|A.5.1|The actual period locus and its generated torsor are retained separately.
II.P25|PROVED|The exact printed period-independence witness is Grothendieck 1966, p.102 note 10.|G and its source record|This is a checked literature witness, not a date for the archive sheet.
II.P26|PROVED|The actual cocycle image and the subgroup it generates can have different Zariski closures.|A.5.2, quadratic-field G_m example|The image is the explicit two-point set; its generated subgroup is dense.
"""

DATA += r"""
II.MB01|PROVED|A codimension-r correspondence from X acts in degree i+2r−2dim X and twist r−dim X.|F.1.3|None.
II.MB01|PROVED|Correspondence composition and comparison compatibility follow from the triple-product push–pull formula.|F.1.3|None.
II.MB02|PROVED|Tensor automorphisms satisfy g_N ω(a)=ω(a)g_M on each morphism.|F.3.4|None.
II.MB02|PROVED|The neutral rigid abelian fibre-functor construction reconstructs C as Rep(G).|F.3.4; Deligne–Milne Theorem 2.11|The category and fibre-functor hypotheses are part of the statement.
II.MB03|PROVED|The specified E,F,H matrices satisfy the three sl_2 commutator identities on every primitive string.|F.3.2, basis-vector proof and exact certificate|None.
II.MB03|PROVED|The partial-inverse lowering operator and sl_2 lowering operator have the displayed rational conversion coefficients.|F.3.2|The operator normalization is specified, not silently replaced.
II.MB03|REFUTED|Those formulas yield equality of the integral operator rings without further divisibility conditions.|F.3.2, m=2 modulo 2 counterexample|The rational denominators are essential on the chosen lattice.
II.MB03b|PROVED|B_m=BΛ^mTE^mB projects to the bottom of the unique length-m string.|F.3.2|None.
II.MB03b|PROVED|E^b B_m Λ^a are the matrix units identifying Q[E,Λ] with the product of full matrix algebras.|F.3.2|Multiplicity spaces carry the identity action.
II.MB03b|PROVED|Casimir and H interpolation recover the same matrix units from E,F,H over Q.|F.3.2|The equality is of actual subalgebras of End(W).
II.MB04|PROVED|The displayed P^1 Lefschetz representation cannot factor through diag(1,z), since it moves the unit vector.|F.3.3|This is the precise failed factorization, not a categorical unrelatedness assertion.
II.MB04|PROVED|The Tate torus conjugates E and F by z and z^−1, and E:h^0→h^2(1) is equivariant.|F.3.3|None.
II.MB05|PROVED|λ_X(t)=t^−d w_X(t), and both conjugate a degree-j endomorphism by t^j.|F.3.3|None.
II.MB05|PROVED|The tensor weight gives εw=t², while the specified filtration splitting gives εj=t.|F.3.3|The Levi and full-group domains are stated explicitly.
II.MB06|PROVED|The Lefschetz operators vanish on elliptic H^1, so the nontrivial standard period action is not their action.|F.3.3|The exact matrices and target degrees prove the comparison.
II.MB07|PROVED|The operational first and third manuscript letters have the two printed standard-conjecture matches.|F.3.5; I.M04|Only the matched operational definitions are asserted.
II.MB07|DOCUMENTARY-GAP|The remaining two letter identifications have secure definitions in this packet.|F.3.5; I.M04; original cote 14 pp.43–44 and complete Coates letters|The newly opened 1965 Serre letter defines its B by primitive positivity, with an explicit cycle-class quotient to the cohomological convention. The specific B and D of the 1967 Coates letter still lack standalone definitions in the inspected sources.
II.MB08|DOCUMENTARY-GAP|The cote14 pages implement the proposed singular-hypersurface programme.|I.M05.01; F.3.14; original cote14 PDFs111–113 and131; complete Coates 1967 letter p.4|F.3.14 supplies the exact finite normalization map and the nodal ordinary-cohomology comparison. The newly inspected original Lefschetz and generic-member pages have not identified execution of the particular historical standard-conjecture proposal; this documentary gate remains.
II.MB09|PROVED|The rational arithmetic Nori motivic sequence is exact with proconstant Galois quotient.|F.3.4; Kahn 2025 Theorems 5.10,10.2|The 2025 proof fixes the older normality gap.
II.MB09|OPEN|That sequence has a canonical splitting or kernel equal to the identity component in the unspecified generality.|F.3.4|Neither property is supplied by exactness; the intended additional statement must be specified and proved.
II.MB10|PROVED|The Ayoub–Nori Hopf maps are inverse over the stated principal ideal coefficient domain.|F.3.4; Choudhury–Gallauer Theorem 9.1|None within the source's hypotheses.
II.MB10|PROVED|The pure rational Nori–André comparison is an equivalence compatible with Betti realization.|F.3.4; Arapura Theorem 6.4.1|No equality of all motivated and algebraic cycles is inferred.
II.MB11|PROVED|Hodge realization is full on the specified abelian-generated pure category.|F.3.4; Arapura Corollary 7.1.4; C.1.1|None within that scope.
II.MB11|OPEN|General Nori Hodge fullness and the proposed general essential image are established.|F.3.4; Arapura Conjectures 7.1.1–7.1.2|The conjectural fullness and essential-image obligations remain.
II.MB12|PROVED|The homological-to-numerical quotient is the surjective identity-on-cycles map.|F.3.5|None.
II.MB12|PROVED|The numerical category is semisimple; cohomology descends exactly when the quotient kernel acts trivially.|F.3.5; Jannsen Theorem 1|The factorization criterion is proved as an equivalence of the actual maps.
II.MB12|OPEN|The kernel-annihilation criterion holds on every relevant product without further input.|F.3.5|This is the numerical=homological standard-conjecture obligation.
II.MB13|PROVED|Curve-to-Jacobian abelianization relates Mochizuki's nonlinear Hom map to Tate/Faltings linear Hom maps.|F.3.6|The primes and field hypotheses of each theorem are retained.
II.MB13|REFUTED|Every Jacobian linear map in those Hom spaces arises from a curve morphism.|F.3.6, multiplication by 2 and Riemann–Hurwitz|This explicit obstruction is the only non-surjectivity conclusion used.
II.MB14|REFUTED|Semisimplicity implies centre-freeness.|F.3.5, G_m character decomposition|None.
II.MB14|PROVED|The centre-free geometric fundamental group gives the pullback reconstruction through Aut→Out.|F.3.6|The homomorphism, its kernel, and its surjectivity are explicit.
II.MB15|PROVED|Stix's cusp-inertia criterion requires non-Tate weights, open normalizer image, and cyclotomic conjugation.|F.3.6; Stix Definitions 26,29 and Theorem 30|None for the fully stated criterion.
II.MB15|REFUTED|The truncated LM6 statements already supply every premise of that criterion.|F.3.10; full LM6 A.50 pp.33–34; Stix Definition 29 and Theorem 30|The full statement and proof are now checked with N to NA. The residual Jacobian character has Frobenius weight one; Stix's cyclotomic-action premise is not supplied in that branch. LM6 A.22 remains open.
II.MB16|PROVED|An integral group comparison transports a chosen integral representation and its lattice.|F.3.4; Choudhury–Gallauer Theorem 9.1|None.
II.MB16|REFUTED|The rational representation or Hopf comparison by itself chooses the required integral lattice and all its forms.|F.3.4; D.5.2|A lattice and its equivalence relation are extra specified data.
II.SF10|OPEN|The Hodge-fullness conjecture in the general algebraic-cycle setting is settled by the real formulation.|C.1.2; II.RH05|The exact cycle-surjectivity premise remains.
II.SF10|PROVED|The abelian absolute-Hodge real formulation is fully faithful with its stated essential image.|C.1.1|None within that category.
II.SF11|PROVED|The naive projection has the minus-times-minus tensor defect, repaired by the specified tensor structure.|C.2.1; II.RH06|None.
II.SF12|PROVED|The Artin and Tate tests determine the nontrivial and trivial fibre-functor torsor examples respectively.|C.2.2; II.RH07|Do not use the naive projection as a tensor isomorphism.
II.SF13|READING|The stronger HC/even-Tate paragraph is deleted in the frozen witness.|Frozen witness 18/037|Retain cancellation even where its surviving mathematical claims have counterexamples.
II.SF13|REFUTED|The cancelled even-Tate conclusion holds universally.|C.3.1|The Artin–Tate counterexample applies to the indicated conclusion.
II.SF14|REFUTED|The live even-Tate iff claim holds in the stated real motivic category.|C.3.1|Use the proved Artin–Tate replacement.
II.SF14|PROVED|The correct f_∞=1 criterion is the specified Artin–Tate decomposition.|C.3.1|Retain the category hypotheses.
II.SF15|READING|The maximal-compact normalizer discussion and its weight quotient are withdrawn.|Frozen witness 18/038; II.RH13|No uncancellation is inferred from a modern proof.
II.SF15|PROVED|The weight-zero centralizer is maximal compact under the polarizable finite-generator hypotheses.|F.3.7|The raw group has the explicit Tate counterexample.
II.SF16|PROVED|Fixed-topology complex transport uses only identity and conjugation and preserves the stated integral lattice.|C.4.1; F.1.6|Do not extend this two-element ambiguity to all abstract embeddings.
II.SF17|PROVED|Problem 3 admits the stated local comparison constructions.|B.3.3|All coefficient, reduction, filtration, and descent hypotheses remain.
II.SF18|PROVED|Problem 4 admits the specified characteristic-p cohomology and Frobenius structures.|B.3.4|No universal motivic classification is asserted.
II.SF19|DOCUMENTARY-GAP|The formula involving K on 18:45 has a fully specified field and degree.|D.2.1|Recover K's generators and base field.
II.SF21|REFUTED|The strengthened Tate open-image assertion holds for every motive.|D.4.2, Q(-2) and the central isogeny t to t^2|The actual image in the stated integral G_m model is (Zhat^times)^2, whose square-class quotients at arbitrarily many odd primes prove infinite index. The named elliptic statements in D.3.2 remain proved.
II.SF21|PROVED|Those named elliptic cases satisfy the needed open-image hypotheses.|D.3.2|None within the exact theorem scopes.
II.SF22|PROVED|An open compact coset contains a point with the stated maximal algebraic independence over a countable field.|D.3.1|None.
II.SF24|PROVED|The precise approximation property has the connected-affine-group criterion and counterexamples in D.|D.4.1|No universal approximation is asserted.
II.SF25|READING|The dependence sentence admits the recorded est/pas alternatives.|Frozen witness 18/051; original cote18 PDF51/archive p.50; II.P10.02|Original page and lower300dpi crop were independently inspected by root and period_triangle on19November2026. The disputed word remains unsafe; keep both alternatives. The mathematical plain-data counterexample is E.2.1.
II.SF25|REFUTED|The strongest plain integral-data reading universally recovers the archimedean place.|E.2.1; D.6.1|The actual compatible counterexample is constructed.
II.SF26|PROVED|The exact two-input equivalence asserted in the margin is valid in the formulations of D.|D.4.2|Broader readings have the displayed counterexamples.
II.SF27|REFUTED|The desired integral comparison exists without an integral-lattice obstruction.|D.5.2|The CM ideal-class example is the counterexample.
II.SF27|PROVED|Once a comparison exists its ambiguity and finite realizations are given by the stated integral maps.|D.5.1; D.1.1|Existence is not inferred from that ambiguity computation.
II.SF28|READING|The universal two-point fibre statement is cancelled.|Frozen witness 18/057|Retain cancellation.
II.SF28|PROVED|The exact stabilizer formula determines when the fibre has one or two elements.|D.5.1|The conjugation must fix the base in the two-element case.
II.SF29|PROVED|The cocycle and left/right conversion are the exact formulas of A.5.3 and D.5.1.|A.5.3; D.5.1|None.
II.SF30|PROVED|The actual tensor-Isom object is an algebraic torsor with the stated descent maps.|A.5.1; D.5.1|This does not certify arbitrary abstract automorphism data as effective descent.
II.SF31|PROVED|The genericity condition translates to the precise orbit-locus statement.|A.5.1|The arithmetic genericity premise remains the named period assertion.
II.SF31|OPEN|That period-genericity premise holds for every motive in the proposed scope.|A.2.4; A.5.1|Only the established cases and the requested implication are proved.
II.SF32|PROVED|The π qualification is necessary in the exhibited Tate situation but insufficient for the proposed universal conclusion.|D.5.4|The two exact examples retain the field definitions.
II.SF32|READING|The margin's unfinished condition has a uniquely determined complete formulation.|Frozen witness 18/060|It does not; preserve the unfinished expression.
II.SF33|PROVED|The action/cocycle pair is a homomorphism into the specified semidirect product.|A.5.3|The ordinary-product homomorphism claim has the explicit counterexample.
II.SF34|REFUTED|The predicted Euclidean/adelic openness holds universally.|D.5.3|The remaining specific elliptic assertion is recorded separately.
II.SF35|PROVED|The two place-dependent cocycles are related by the computed cochain transport.|D.5.1|The comparison choices are part of the formula.
II.SF36|PROVED|Place change gives the stated conjugacy/translation relation on the relevant images and closures.|D.5.1|The unresolved reading of any truncated synopsis is not promoted to an additional theorem.
II.SF36|READING|The live boxed change-of-trivialization formula retains the final inverse omitted in the cancelled line.|Frozen witness 18/062|Both the cancellation and the corrected expression remain recorded.
I.ST01|PROVED|The proposed local descriptions receive the exact rational, integral, and relative realization constructions of B.|B.1–B.3; F.3.1|The six unspecified global essential images remain open as in I.P01.
I.ST01|OPEN|Those local theorems establish all six global motivic classification claims.|I.P01; F.3.4|Specify and characterize each global essential image.
I.ST02|PROVED|Integral Chow specialization and its geometric ℓ-adic cycle-class square hold in the smooth proper complete-DVR setting.|F.3.8; I.P07; Fulton 20.3|The SGA 6 mirror omits printed p.580; Fulton and Stacks supply the checked modern theorem.
I.ST03|PROVED|The typed triangle, group dimensions, and exact conjugate-joint image dimensions are as in A.|A.1.1–A.2.4|The unsupported universal g+u assertion is refuted in A.2.5.
I.ST03|NAMED-CONJECTURE-IMPLICATION|The named joint period conjecture gives the corrected actual-point transcendence-degree table.|A.2.4|This is a proved implication, not a proof of its arithmetic premise.
I.ST04|READING|The normalized-period draft remains wholly cancelled with its uncertain normalization.|I.P18; I.P26|No chronology or resolved normalization is inferred.
I.ST04|OPEN|The cancelled full normalized period-independence assertion is established.|I.P18–I.P21|The specified arithmetic assertion is not proved; excluded full non-CM target remains excluded.
I.ST05|OPEN|The cancelled elliptic normalized independence, including its transcendental-j total-degree version, is established by Schneider's theorem.|I.P20–I.P21; A.3.1; G|The stronger independence is not proved; the field and normalization remain unspecified in the margins.
I.ST05|READING|The uncertain known remark and deleted π-over-k question constitute a completed proof.|Frozen witness 18/012:L13–26|They keep their own uncertain and deleted status.
I.ST06|PROVED|The CM elliptic full period field has degree 2, and the elliptic period locus generates the full motivic torsor.|A.4.3; A.4.9|These answer two precisely scoped parts of the live questions.
I.ST06|OPEN|The non-CM full degree 4 is established.|I.P22; A.4.9|That full period target is excluded and is not proved by torsor generation.
I.ST06|OPEN|The non-CM algebraic Hodge splitting is impossible.|I.P24; A.4.13|The scalar/χ* arithmetic specialization obligation remains.
I.ST07|PROVED|There is one universal cycle-comparison multiplier λ=2πi, yielding λ^p in codimension p.|F.1.1|Products, orientations, and supports provide the global proof.
I.ST08|PROVED|The unfinished local-to-global commutativity argument is supplied by the support-localization and Gysin proofs.|F.1.1–F.1.2|The proof is present here; the manuscript's sentence remains unfinished.
I.ST08|READING|The marginal faire le raisonnement and final Provient de la comm. de have secure complete readings.|Frozen witness 18/017:L2,L25|Retain both uncertainty and incompleteness.
"""

rows = []
counts = Counter()
for raw in DATA.splitlines():
    raw = raw.strip()
    if not raw:
        continue
    cells = raw.split('|')
    assert len(cells) == 5, (len(cells), raw)
    key, status, claim, proof, obligation = cells
    assert key in entries, key
    counts[key] += 1
    e = entries[key]
    rows.append({
        'assertion_id': f'{key}.{counts[key]:02d}',
        'note_id': key,
        'witness': e['witness'],
        'original_note_kind': e['note_kind'],
        'claim': claim,
        'status': status,
        'proof_or_locator': proof,
        'remaining_obligation_or_scope': obligation,
        'source_file': e['source_file'],
        'source_line': e['source_line'],
    })

assert set(counts) == set(entries), ('Missing', sorted(set(entries)-set(counts)), 'Extra', sorted(set(counts)-set(entries)))
assert len({r['assertion_id'] for r in rows}) == len(rows)

out = ROOT/'work/audit_claims.csv'
with out.open('w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

status_counts = Counter(r['status'] for r in rows)
md = [
    '# F.3 exhaustive assertion inventory',
    '',
    f'{len(entries)} requested source entries are represented by {len(rows)} individually adjudicated rows. The extraction includes 52 notes [I], 94 notes [II] (including MB03b), and eight cote-18 standing-question rows.',
    '',
    'The complete source text is preserved in `audit_notes_source.json`, with metadata in `audit_notes_entries.csv`. The CSV `audit_claims.csv` is the machine-readable assertion inventory. Every source entry has at least one row, and the build script checks complete coverage and unique assertion identifiers.',
    '',
    'Statuses record the mathematical result and do not reverse the historical cancellation or uncertainty in the original-note-kind column. OPEN records the exact remaining obligation; DOCUMENTARY-GAP and READING are not claims that an unseen proof or handwritten sign has been checked. NAMED-CONJECTURE-IMPLICATION records only the proved implication.',
    '',
    'Supplemental proofs F.3.1–F.3.14 are in `agent_audit.md`, the research addenda, and `../output/RESEARCH_SA07/sections/F_audit.tex`; other identifiers refer to the current manuscript. No scans were supplied initially. Targeted original cote14, cote16 and cote18 pages were subsequently acquired and visually inspected; cote15 was also acquired for the remaining definition search, with exact page access recorded in the source ledgers; no full archival reading is implied. The CSV adds original-assertion check-event links and canonical dependencies through `build_triangle_check_events.py`; the corresponding event rows are in `triangle_comparison_audit_CHECK_EVENTS.tsv` and the dated addenda `audit_next_CHECK_EVENTS.tsv` and `audit_postcheckpoint_CHECK_EVENTS.tsv`.',
    '',
    '## Status totals',
    '',
    '| Status | Rows |',
    '|---|---:|',
]
md += [f'| {k} | {n} |' for k,n in sorted(status_counts.items())]
for key,e in entries.items():
    md += ['', f'## {key} — {e["title"]}', '', f'Witness: {e["witness"]}. Source: `{e["source_file"]}`, line {e["source_line"]}.', '', '| Assertion | Status | Claim | Proof or exact locator | Remaining obligation or scope |', '|---|---|---|---|---|']
    for r in rows:
        if r['note_id'] == key:
            esc = lambda x: str(x).replace('|','&#124;').replace('\n',' ')
            md.append('| '+' | '.join(esc(r[c]) for c in ['assertion_id','status','claim','proof_or_locator','remaining_obligation_or_scope'])+' |')
(ROOT/'work/audit_claims.md').write_text('\n'.join(md)+'\n')

coverage = {
    'source_entry_count': len(entries),
    'assertion_count': len(rows),
    'source_package_counts': dict(Counter(e['package'] for e in entries.values())),
    'status_counts': dict(status_counts),
    'uncovered_entries': sorted(set(entries)-set(counts)),
    'duplicate_assertion_ids': [],
}
(ROOT/'work/audit_claims_coverage.json').write_text(json.dumps(coverage, indent=2)+'\n')
print(json.dumps(coverage, indent=2))
