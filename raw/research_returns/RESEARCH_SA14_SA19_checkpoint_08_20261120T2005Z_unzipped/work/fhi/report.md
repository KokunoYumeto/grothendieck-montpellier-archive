INCOMPLETE

# Parts F, H, I: current results

| ID | Status | Result |
|---|---|---|
| F1 | Known | Checked prime-to-p, pronilpotent and strongly F-regular finiteness theorems |
| F2 | Refuted | Dimension-free consequence is false for k[[t]] in characteristic p |
| F3 | Proved | Metabelian group with pronilpotent quotient Z3 and fg open abelianizations need not be fg |
| F-full | Undecided | Full finite generation for all normal complete local surfaces |
| H1 | Proved | Connected pro-generalized Jacobian has projective dimension at most one in Serre category |
| H2 | Proved | Ext>=2(P,Ga)=0 for every source P in Serre category |
| H3 | Refuted | Unaugmented all-degree geometric comparison fails in degree zero |
| H4 | Proved | Etale local cohomology has H3_m(k[[s,t]],Z/p) nonzero |
| H5 | Proved | Perfect étale Ext agrees here by Suzuki exact source/target theorem |
| H4b | Refuted | Ordinary local Jacobian is not projective: explicit nonsplit Z/p extension |
| I1 | Proved | Degree-zero endomorphisms are diagonal in every regular local residual complex |
| I2 | Proved | Complete surface presentation including End2=restricted adeles/F |
| I3 | Proved | Universal presentation for every regular local surface via explicit arrow completion |
| I-full | Undecided | Presentation for all regular local essentially finite type rings and dimensions |

Full proofs and exact gates are in F_proof.md, H_proof.md, and I_proof.md. The three TeX sections contain the proofs, all in mathematical LaTeX. All opened sources are recorded in references.bib.

## Corrections

- F consequence needs dimension-at-least-two qualification; dimension-one counterexample given.
- H additive target already vanishes for every Serre source; connected pro-Jacobian has pd<=1.
- 43:80 augmentation by Z cannot be discarded; comparison of Serre and perfect-site Ext now justified by Suzuki2022 for the precise pro-Jacobian class.
- SA19 H4 Zariski concentration does not transfer to etale supports; the ordinary functor does not descend to perfection.
- I arrows to the closed point require mixed topology, not the local p-adic topology. Degree-zero diagonality is verified.

## Computations

code/finite_checks.py; output/artin_schreier_orbits.csv (20 exact rank checks for p=2,3 retaining target overflow), output/metabelian_factors.csv (n=1,...,8), output/checks.json (A5 perfection and scope). These corroborate, never replace, the symbolic proofs.

## Independent review

Reviewed root sections/A.tex: A4 finite obstruction, exponent and finiteness arguments; surface and fourfold reductions; R3g incidence/dlog generic-kernel argument. No mathematical gap found; suggested stating Leff full faithfulness after shrinking a neighborhood.

## Superseded passage

The first automatic Pandoc typography was replaced before checkpoint01. I.tex is the current authoritative source, now including the noncomplete surface theorem; I_typeset.tex is an older complete-surface-only copy. Root repaired the LuaLaTeX runtime and performs the integrated build.

## SA19 H1–H2 priority audit

The mathematical correspondences with the component-group pairing and biextension formalism are confirmed against exact original SGA7 pages. Priority dating is Undetermined: dates on 43:87 and 43:144 belong to cited publications; 43:118 is a separate administrative list. Full evidence, source URLs, and the precise dating gate are in priority.md and priority.tex.

## Higher-dimensional I reduction

I4 proves the explicit separated coefficient completion for every adjacent arrow in every dimension. I5 proves dense generation of every graded endomorphism module by diagonal coefficients and the differential. Complete proofs are incorporated in I.tex and I_proof.md and separately in I_higher.md. Dense generation is not confused with surjectivity of a completion or the full presentation: uniform continuity, quotient topology, and closed relations remain precise gates.

H3b sharpens the comparison correction: augmentation alone cannot identify perfect-site Hom with ordinary H0(K,G), because Frobenius acts invertibly on perfected Ga but not on k(t).

F1b adds the 2025 published Carvajal-Rojas–Yasuda theorem: complete log terminal surfaces have finite full punctured étale fundamental group in all equal and mixed characteristics, including 2 and 3. The arbitrary normal surface case remains Undetermined.

I6 proves closed-image exactness of residual Hom columns and identifies the quadratic kernel in every gap-two interval in the actual Hom topology. It is explicitly separated from the unresolved topology of the independently completed free algebra.

The official Montpellier catalogue dates cote 43 tentatively from 1961 to around 1968 and explicitly calls the notes undated; its footnote 37 includes a 1967–1968 Bourbaki verso. This further defeats an assumed dossier-wide 1964/1965 upper bound, without proving that the relevant scientific leaves are late. See priority.md and priority.tex.

Independent C2 audit: the proposed full excellent-henselian completion-isomorphism proof passes, including principal finite determinacy, blowup/Stein support, auxiliary finite cohomology, and conductor unit stabilization. Detailed check and opened primary sources are in C2_independent_audit.md.

Independent D4 ordinary audit: the Serre–Tate calculation and both finite-flat torsor sequences pass; the proposed ordinary Pic-tau flatness conclusion contradicts the literal Chai Theorem 2.4(iii), whose tangent inference does not apply to nonsmooth torsors. Exact source and proof checks are in D4_independent_audit.md; the subsequent full supersingular audit is recorded separately below.

I7 strengthens the complete-ring column calculation: Hom(E_p,K_A) is actually exact for p nonmaximal, and the maps onto cycles are open above the first arrow. The proof uses Matlis tensor–Hom adjunction and a finite-Ext annihilator correction. It does not settle the full universal-family topology.

## Full higher-dimensional presentation in the linear category

I8, in I_universal_linear.tex, proves the universal presentation in every dimension for separated complete graded algebras with a basis of open left ideals. Every discrete Cousin representation is a quotient of sums of K[J]=Hom(A/J,K), with J a regular-sequence ideal. Exact approximation on finite inputs makes the kernel stable under all residual endomorphisms, and passing to all discrete quotients of a target algebra constructs the continuous universal map. This resolves the higher relations and quotient topology in that category. The exact manuscript convention remains a documentary qualification: the transcription does not explicitly require open left ideals, and an arbitrary non-linear topological-algebra interpretation is not settled by I8. The earlier density-only and column-only gates are superseded in the stated linear category.

Independent D4 supersingular audit: every step of DGJ's complete quartic-hull and Pic-tau-flatness proof passes. The canonical BT subgroup, effectivity and uniqueness, graph classification, norm elimination, algebraization, and finite-flat torsor argument are checked in D4_supersingular_audit.md against the primary Katz and Tate sources.


The original Montpellier scan066 (printed65), visually checked against the transcription, confirms only a separated complete graded topological algebra; it does not specify an open-left-ideal basis. Thus I8 remains a complete theorem in the stated linear category, with the broader category still open in this work.

F4 supplies a rigorous quantitative target for the solvable part: a uniform bound C on normalized H1 for all finite simple coefficient modules gives ceil(C)+1 generators of a prosolvable group. The proof counts complement cocycles and uses compactness; deriving the uniform geometric estimate remains the active step.

F1c updates the mixed-characteristic literature through 2026: Cai–Lee–Ma–Schwede–Tucker prove the full local fundamental group finite of order prime to p under a BCM-regular-pair hypothesis, with an inverse perfectoid-signature bound. The exact additional assumption is retained; it does not resolve arbitrary normal surfaces.


## F5: a geometric obstruction actually excluded

The normalized H1 bound is now proved for all finite F_p coefficient systems with abelian prime-to-p monodromy on a complete normal local surface in equal characteristic p. This excludes the F3 metabelian group as a quotient of the geometric fundamental group in characteristic2. It is genuine progress beyond the abstract criterion, with full proofs and independent root/BCE checks, but it leaves nonabelian and wild coefficient monodromy unresolved. The full local fundamental-group conjecture remains undecided.

F6 further proves uniform finite generation of every quotient with a normal pro-p subgroup and abelian pro-prime-to-p quotient, allowing nonabelian wild kernels. Virtually abelian pro-prime-to-p quotients also give finite generation after a finite cover. Root independently passed the complete F4/F6 arguments. This remains a geometric subclass, not a resolution of arbitrary alternating wild/tame towers.

F7 now proves the uniform rank bound for every finite F_p coefficient system extending over a fixed resolution, including nonabelian and wild monodromy. F7a removes the solvability assumption from the group-theoretic criterion when the kernel is pro-p. F7b consequently proves uniform finite generation for pro-p extensions of quotients factoring through the fixed resolution. All three proofs and the exact proper-specialization/proper-fundamental-group sources passed root audit. The full local group remains undecided.

I8 independent-audit status: root and DGJ passed the full proof, including I4/I5 and the inverse-limit topology argument; BCE separately passed the Cousin generator lemma. This supersedes any earlier request-for-audit wording, within the stated open-left-ideal category.

F8 now proves a uniform rank-linear H1 bound for all finite F_p local systems tame along a fixed SNC resolution. The full monodromy group may contain p-torsion. The proof controls the Frobenius cokernel on the Nth-root stack uniformly in N and cancels the N-fold divisor thickness by generic inertia-character counting. F8b consequently proves uniform finite generation for every quotient with a normal pro-p subgroup and arbitrary pro-prime-to-p quotient. Root passed the complete proof and primary sources; BCE separately passed the root-stack degrees, coarse descent, and character count. The full wild problem, including alternating tame/wild solvable factors, remains open here.

F8 literature/search scope: primary sources checked were Suzuki v4 §§2–3, Sun v2 Theorem3.7 and its local calculation, Borne preprint Theorems4–5/Lemma15/Proposition6, Cadman §§2.3–2.4, and Stacks Abhyankar/purity. The targeted searches concerned uniform tame coefficient bounds, root-stack degree/semistability, and local fundamental-group ramification. They do not establish historical novelty or the absence of a prior theorem; no priority claim is made.

F9 gives a uniform generator bound for the full tame local quotient by standard root-stack/curve/gluing methods. The primary SGA1 XIII Cor2.12 was checked: its full tame-group generator assertion is distinct from its prime-to-p presentation assertion. Combining this with F8 and F7a, F9b proves uniform finite generation for every local quotient having a normal pro-p subgroup and tame quotient, even when that tame quotient has p-part. Root passed all gluing, coarse-space, and source steps. The actual wild kernel may fail to be pro-p, so the alternating-factor gate remains.

F10–F11 are proved and independently checked. The exact regular F-finite global refined Swan theorem of Krishna–Majumder, arXiv2601.12177v2 (8 Nov2026), combines with the negative exceptional intersection matrix to bound every rank-one p-primary conductor uniformly. Witt restriction then shows that one fixed p-power makes every such character unramified on the resolution. Together with the prime-to-p intersection calculation and known finite generation of the abelian group, this proves that the entire abelian inertia kernel is finite. One fixed finite abelian cover therefore makes every original abelian coefficient system extend to a fixed resolution. F7 for coefficient p and tame affine-cocycle descent for every other coefficient prime give one uniform all-prime H1/rank bound. Complement-count induction proves uniform finite generation of every metabelian quotient (F11). Root passed the complete proof and primary source; BCE independently passed F10 and F10b. This explicitly depends on the November2026 preprint and carries no priority claim. Derived length three is the next solvable gate; general F remains unresolved.

F12 closes the characteristic-p coefficient estimate for simple systems with metabelian monodromy: after F10b’s single fixed cover, wild inertia maps into the commutator of the faithful metabelian image, whose p-primary part is killed by simplicity, hence the system is tame. F8 applies even when restriction is not simple; inflation–restriction accounts for any p-divisibility of the cover degree. F12b proves uniform finite generation for all local quotients with pro-p closed second derived subgroup, using F11 and F7a. Root passed both proofs. Equal characteristic p and the full remaining coefficient-ell-not-p gate at derived length three are explicit.


F13 proves a fixed highest logarithmic conductor bound, after F10b’s single fixed cover, for every finite coefficient-ell-not-p system with metabelian monodromy. F13a gives a full modular monomial proof with a specified abelian normal subgroup; F13b proves that the refined-Swan cutoff is unchanged by any finite etale cover of the resolution. Kato–Saito identifies the rank-one conductor and Abbes–Saito shows unramified induction preserves the cutoff. Root passed the full proof and exact primary sources; BCE independently passed F13b geometry. The explicit remaining gate F13.5 is a rank-linear H1 bound for this fixed complete-local pair. Hu–Teyssier Th7.34 provides such a bound for proper smooth finite-type varieties, and its geometric-trait nearby-cycle theorem does not itself extend this to the complete-local pair. This result postdates formal review03 and is recorded for the next review.


F13c removes unbounded unramified order from the rank-one gate: on every finite etale resolution cover, each p-primary character is an unramified twist of a character of order at most p^e, with one e independent of the cover degree. The proof derives divisibility of unramified p-primary characters from Artin–Schreier H2(D,Fp)=0. F13d gives a complete sufficient reduction to a degree-linear tame-generator bound for cyclic ramified covers of degree at most p^e. Root independently passed the reduction. The latter geometric bound F13.6 remains an explicit unproved hypothesis; neither F13.5 nor derived length three is promoted.


F13e bounds the total zero length of the refined-Swan sections on the original exceptional curves by C times the degree of the finite etale resolution cover. More precisely, a component of degree d_a over C_i and positive Swan coefficient s_a has zero length at most d_a(−B_ii)(t_i−s_a). The proof uses saturation, the same residue sequence as F10, the projection formula, and (−B)t=k. Root independently passed every step. It does not bound the successive cleanup blowups or their cohomology; those remain genuine additional requirements for F13.5/F13.6.


F13f records the strict subunit cutoff subclass: if every t_i is less than one on the fixed post-F10b resolution, integer rank-one Swan conductors force the induced systems tame, closing the coefficient bound and derived-length-three case in that subclass. Root passed the proof. No claim that the numerical hypothesis is automatic is made, and this corollary is not a separate formal-review movement.


I7b, proved by BCE and independently passed by root, removes completeness from the open dense image assertion for residual Hom columns, including whole products of source columns. The arbitrary-target extension statement remains conditional on continuity in the preceding degree. The broad topological universal presentation is still Undecided; this result does not silently replace that missing premise.


F13g/h sharpen the conductor reduction. A positive Swan coefficient prime to p has nonzero logarithmic residue, forcing nonnegative intersection with its exceptional component. Negative definiteness therefore forces any nonzero Swan divisor to have a p-divisible positive coefficient and maximum at least p. Consequently the uniform unramified exponent may satisfy p^(e+1)>T0, and F13f is strengthened from t_i<1 to t_i<p. Root reopened Yatagawa v1 pp8–9 and Krishna–Majumder Cor9.6/9.7 plus Lemma9.11 and passed the full proof. General F13.5/F13.6 remain open.
