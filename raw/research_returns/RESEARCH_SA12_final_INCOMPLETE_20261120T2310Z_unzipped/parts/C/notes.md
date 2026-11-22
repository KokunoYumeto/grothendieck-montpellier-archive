# Part C working notes

Run: GPT-6 Astra (OpenAI), inherited reasoning effort, `/root/part_c`, 20 November 2026. We assert no priority. These notes are a live research record and distinguish completed statements from the remaining wider classification.

## Exact manuscript hypotheses

`Codex_K29-09/K29-09_transcription.tex`, scan 141, explicitly requires closure under kernels of pairs and images and says that all groups are admissible. These hypotheses are stronger than “all finite flat S-groups with all S-morphisms”. The cusp kernel of multiplication by x on alpha_p is nonflat, so the cusp does not refute the literal scan-141 statement. Theorem C:literal-141 proves that statement using the orbit quotient G/E: its support is an open-and-closed union of components, connectedness selects it and reducedness kills its nilpotent thickening.

## Normality does not suffice

For A=k[x,y] in characteristic p, G=alpha_p × alpha_p and P given by s^p=x^(p+1), t^p=x y^p, the nonzero map (y,-x) kills the pointed class. The only possible generic rank-p reduction is the line (x,y). Its closure has coordinate module direct sum of (x,y)^j z^j for 0<=j<p, generic rank p and fibre dimension p(p+1)/2 at the origin. It is not flat. Every finite flat subgroup with that generic fibre would equal the closure, so P is minimal. This refutes C.1(i) even for a smooth affine surface.

## The cusp also rules out nonflat subgroup reductions

For A=k[t^p,t^(p+1)] the torsor z^p=t^p has no section, while multiplication by t^p kills it. Every proper closed subgroup H of alpha_p has trivial generic fibre. If an fppf H-torsor reduced P, local sections supplied by a trivializing fppf cover would agree generically on double overlaps, hence everywhere by flatness and schematic density of the generic fibre. They would descend to a global section, a contradiction. Thus the first proposed remedy in L7 fails even when nonflat closed subgroups are admitted under the ordinary fppf-local torsor definition.

## Constant groups and all S-morphisms

With k-defined homomorphisms, Proposition 4 holds over every connected reduced noetherian k-scheme, with no properness assumption. The original Nori existence statement, Chapter II §1, Proposition 2 (pp.85–86), has now been opened and confirms the rational-point case directly.

With all S-morphisms and a rational marking, the complete criterion is: always in characteristic zero; in characteristic p, exactly when A=Gamma(S,O)=k. Sufficiency follows because the coefficients of every morphism lie in A. For necessity, I=ker(A→k) has I/F(I) nonzero by Krull intersection. Choose f there and nonzero h in I. If a nonzero scalar r kills the alpha_p class f, that gives the counterexample. Otherwise use G=alpha_(p²) × alpha_p and P with s^(p²)=h^p f, t^p=f. The map (F,-h) kills P. A proper constant subgroup with zero Frobenius cannot carry the first class; any other proper constant subgroup is alpha_(p²) and embeds as a graph dF. A reduction would imply (1-dh)^p f in A^p, impossible because (1-dh)(a)=1.

A failed first attempt used the alpha_p × alpha_p class (f,h^p f). It is not minimal: the allowed varying embedding (1,h):alpha_p→alpha_p × alpha_p gives a reduction. We retain this failed approach as an audit event; it is not used in the checked proof.

The negative result extends to arbitrary geometric marking whenever A is not a field: choose a nonzero nonunit h and a zero b. Evaluation lands in kappa(b), but every field form of alpha_(p²) is trivial since its automorphism group is Ga semidirect Gm. The graph proof therefore still applies. The remaining positive-characteristic gate has A a field L properly extending k. Equalizers of L-maps between k-descended groups need not have a k-form, so we do not silently identify the object categories. The rational-point classification does not settle that unrestricted case.

## Relative etale functor

Under local noetherianity and finite presentation, the pointed finite-etale torsor functor is a quasi-finite etale algebraic space, by Hall–Rydh Theorem 1.2 and SGA 1 XIII Corollary 6.2. Geometrically reduced fibres make it separated and hence a scheme. The proof extends a generic isomorphism by selecting its component in the finite-etale Stein scheme of the Isom-cover (SGA 1 X Proposition 1.2); it does not infer existence solely from specialization surjectivity.

Separatedness is false under C.2 as written. Take a connected etale double cover Q0→C of a smooth proper curve and A=k[t]_(t), characteristic different from two. Let E=Spec A[z]/(z²−t²), and quotient Q0×E by the free diagonal involution. The resulting X/A is proper flat with universal H0=O and a section, while the induced pointed double torsor is generically trivial and specially nontrivial. This contradicts separatedness of any representing object.

## General finite-flat functor

The pointed torsor groupoid is an algebraic stack under the same finite-presentation hypotheses. If G is commutative its pointed inertia is trivial, giving an algebraic space equal to Hom(G^D,Pic_X/S) by Raynaud Proposition 6.2.1(1), with the section providing the rigidification. For a supersingular elliptic curve, G=alpha_p yields Ga; G=mu_p yields E[p]. The first identity is checked on nonreduced tests using naturality of relative Frobenius and primitive polynomials.

The noncommutative class functor can fail even the Zariski sheaf condition. In characteristic three, take an elliptic curve C with a nontrivial two-torsion line bundle L, its split square-zero thickening X=(O_C⊕L), and G=alpha_3 semidirect mu_2. Pull back the mu_2 cover associated to L and extend its group to G. The entire pointed automorphism sheaf of the resulting torsor is Ga: the sign-eigenfunctions on the cover are b epsilon with epsilon²=0. Twisting by a nontrivial Ga torsor on a proper positive-genus curve T yields globally distinct pointed torsors that become equal locally. Full inertia and descent arguments appear in C:non-sheaf.

## Corrections with exact attachment locators

1. `inputs/RESEARCH_SA12_study/study/STUDY.md:172` labels both 29/139 and 29/141 false using the cusp. This conflates two statements. The kernel-closed admissible category of 141 satisfies Proposition 4; the cusp violates kernel closure. Compare `inputs/RESEARCH_SA12_transcriptions/transcriptions/Codex_K29-09/K29-09_transcription.tex:21-25`.
2. `inputs/RESEARCH_SA12_study/study/readings/c29b_c31.md:45-51` carries the cusp failure into the kernel-closed non-etale setting and leaves that setting open. C:literal-141 closes it. The diagnosis of circular uniqueness at lines 33–40 remains correct as criticism of the written proof, not as a counterexample to its conclusion.
3. `inputs/RESEARCH_SA12_study/study/readings/c29b_c31.md:59-64` says kernels are unnecessary in the strict pro-object construction. For the faithfully flat transition maps over a general base, we use flat kernels to identify the quotient with the image. Scheme-theoretic surjectivity alone is not a substitute for this step.
4. `inputs/RESEARCH_SA12_study/study/HUNCHES.md:54` proposes minimality among all closed subgroups, flat or not. C:cusp-all-subgroups refutes this candidate for fppf-locally trivial torsors under those groups.
5. `inputs/RESEARCH_SA12_study/study/HUNCHES.md:79-82` and `inputs/RESEARCH_SA12_study/study/readings/c29b_c31.md:386-389` restrict the successful k-morphism setting to proper S. Properness is unnecessary, as proved here and stated in Nori Chapter II §1 Proposition 2.
6. `inputs/RESEARCH_SA12_study/study/STUDY.md:191-192` lists the non-etale varying-map and relative cases as open. The present work separates the literal closed category, the smooth-surface counterexample, the rational-point classification, etale nonseparatedness and finite-flat failure of the sheaf condition. The unrestricted field-extension variant was still open at the first checkpoint; C:all-constant-classification subsequently closed it by the exact criterion recorded below.
7. `inputs/RESEARCH_SA12_study/study/readings/c29a.md:609-612` correctly identifies admissible equalizers as sufficient. We supply the full orbit-support proof rather than taking the asserted reduction torsor on authority.
8. `inputs/RESEARCH_SA12_transcriptions/transcriptions/Codex_K29-08/K29-08_transcription.tex:363-366` has the reversed contracted-product notation already flagged in the study: a reduction is a G'-torsor, and the induced G-torsor is P' ×^{G'} G. We use that typed formulation.

## Checkpoint status at 00:46 UTC

The checked fragment contains 12 numbered statements. The separate unresolved fragment records the wider C.1(iii) field-of-global-functions issue and the non-finitely-presented relative scope. The exact algebra program has 17 checks and ran in 0.061371275 seconds. Root independently audited C:literal-141, C:normal-counterexample and C:constant-all-maps; events are recorded in CHECK_EVENTS_C.tsv. Original Nori and Raynaud sources have been opened at exact locators. `search_log.md` records searches, sources, failed approaches and computation scope.

## Movement at 01:20 UTC: field descent counterexamples completed

C:field-descent is now a checked proposition, with explicit examples over Q⊂Q(sqrt2) and F5⊂F25. A cyclic quartic extension supplies an order-nine etale k-group whose every order-three L-subgroup has a quadratic character that cannot descend to k. The degree-three isogeny y²=x³+b → y²=x³−27b supplies a nontrivial torsor under such a subgroup. After inducing the group, the torsor is minimal relative to k-descended objects and is killed by a nonzero projection. Product with a proper cuspidal cubic makes the base nonnormal while preserving Gamma(S,O)=L and nontriviality. Thus the unresolved field case is a real descent issue, not a missing simplification to 'A is a field'.

The second program, check_field_descent.py, checks all 9 group vectors, all 4 lines, the order-four automorphism of Q[r]/(r⁴−4r²+2), all 25 GF25 elements, the nonsquare b and the cleared 3-isogeny equation. Run time 0.043755036 seconds. The checked fragment now has 13 numbered statements. Velu's original formulas were opened in the Ghitza translation at §3, equations (8)–(11), Remark 3.

Root requested a fresh attack on A.2 after this insertion. We now turn to the proposed persistent Pic/l obstruction for an excellent Dedekind domain with cd_l fraction field one.

## Movement at 01:57 UTC: the field gate is closed by an exact criterion

The marked-point convention is now checked at its source: scan 29/126, K29-08 transcription lines 80–84, says algebraically closed extension of a residue field. Thus the manuscript means geometric marking. The earlier discussion of an unspecified field-valued convention was overcautious; the rational-lift variant remains a useful separately stated refinement.

The new lemma C:detect-proper-subgroup proves that every proper L-subgroup of a finite k-defined group is distinguishable by two L-maps to a finite k-defined target. If it misses an etale component, the target is the automorphism group of two copies of the component group, with conjugation by the permutation swapping copies precisely over the subgroup. If it hits every component, a nonconstant invariant in the regular representation gives a cocycle vanishing on the geometric reduction; a high Frobenius kernel contains the cocycle, so its semidirect product with the original group is a finite target defined over k. This works over arbitrary k and arbitrary L/k, including inseparable extensions.

C:all-constant-classification therefore gives a complete intrinsic answer for every S in C.1(iii). In characteristic p, nonfield global functions force failure. If global functions are a field L, the answer is exactly whether every proper finite quotient image of the full finite-L pointed fundamental group in a k-descended group lies in a proper subgroup having a k-form. In characteristic zero the same criterion applies with L the algebraic-constants field inside global functions, whether or not the global ring is a field. The proof establishes necessity using target detection and sufficiency using faithful-flat full monodromy. This is a group-theoretic descent criterion in the specified data, not a claim that the field L by itself decides the answer.

The geometric convention also forces a correction to the Nori comparison. A rational underlying point alone is insufficient: over F5 the quadratic field torsor, also pulled back to the projective cuspidal cubic, contributes to the geometric-lift functor but not to Nori's rational-lift functor. C:nori now states this negative result and the positive canonical comparison after requiring the torsor lift to be k-rational. This qualifies the identification at `inputs/RESEARCH_SA12_study/study/STUDY.md:168` and `inputs/RESEARCH_SA12_study/study/readings/c29b_c31.md:386-389`. The new program checks all 25 finite-field elements and all 12 proper subgroups of cyclic groups of orders 2–8; elapsed 0.004885775 seconds.

For root's A.2 work, `A2_notes.tex` contains two checked lemmas: arbitrary k-subalgebra cohomological dimension bounded by cd(k)+transcendence degree, with every continuity step opened at its exact Stacks locator; and a direct finite-character proof that a tower with finite prime splitting and bounded ramification has Dedekind integral closure. The first rules out the proposed class-group construction inside a field algebraic over an algebraically closed one-variable function field. The arithmetic Iwasawa route is separate and is being checked by root.

## Complementary B.2 work at 02:18 UTC

The complete C classification and the geometric-point Nori correction have both been independently audited by root. We now assist B.2 over an imperfect ground field. `B2_norm_notes.tex` proves a support lemma: for a proper generically finite map of normal integral schemes, pullback on the entire fppf Picard sheaf has kernel killed by the generic degree. The proof uses the normal finite Stein factor, its finite-flat locus containing every codimension-one point, norm, and extension of line-bundle isomorphisms across codimension two after arbitrary k-base change. Thus it controls infinitesimal kernels as well as geometric points. For a fixed regular alteration, B.1g fixes the Picard group of every normal main graph, and the fixed-Jacobian embedding bounds these kernels uniformly.

The remaining issue is the image, not this kernel. After choosing a maximal abelian dimension among allowed geometrically normal models, a finite quotient can still lie in a positive-dimensional abelian quotient of the geometric stable Picard group. Its order is not bounded by dimension or tangent dimension alone. A quotient model constructed over a purely inseparable constant extension need not be geometrically normal over k, and cannot simply be inserted into the permitted model category. We directly re-read Schröer 2024, §§3–4 and the proof of Theorem 6.1/Proposition 6.2. His abelian-part stabilization uses a filtered compactification category and does not by itself control these finite Picard quotients. We do not present failure of the descent argument as a counterexample to the weak stabilization statement.

## Complementary audits and B.2 search at 02:20–02:44 UTC

We independently audited D.10's arbitrary-base criterion and its nonconstructible direct-image counterexample, the Raynaud quasiprojective-boundary reduction for D.1–D.2, and the connected non-quasi-compact nodal-chain obstruction to the natural unrestricted Proposition5 construction. The last example retains uniformly bounded rank2 objects; its failure comes from unbounded group-coordinate dependence on infinitely many clopen components after etale base change. Clopen-base completion repairs that descent defect, though it need not preserve the additional global bounded-rank condition. Exact audit scopes, including which primary sources were independently reopened, are recorded in CHECK_EVENTS_C.tsv.

For A.2 we checked root's arithmetic-algebraic-domain bound, Dedekind Milnor-residue criterion, semilocal CRT proof, and reduction through a possibly nonfinite one-dimensional normalization. The generic-zero cokernel comparison works by expressing the sheaf as a filtered colimit of constructibles and replacing each stage by its image at a later stage where the generic stalk has died; that image has finite closed support. Finite residue extensions preserve finite p-cohomological dimension after the real-field exception is excluded. We did not duplicate root's source searches for the Bloch–Kato or arithmetic-duality inputs.

The B.2 graph gate remains open. We investigated the class-group realization lemma in Kollar–Lieblich–Olsson–Sawin's author-hosted book draft. Lemma10.3.5 and the Albanese construction in section10.3.9 explicitly assume a perfect base field, so they do not supply the needed imperfect-field geometric-normality statement. A search snippet juxtaposed a separate geometrically normal corollary with this lemma; reading the primary text prevented that inference. A rank-one reflexive Cartierizing modification may behave better than arbitrary blowups, but the normalized Rees algebra uses integral closures of powers, not their reflexive hulls. No theorem equating those constructions is claimed. Postcomposing an Albanese rational map with an isogeny cannot remove a bad divisorial valuation from its normalized graph.

## 03:40 UTC — threefold cofinal Picard counterexample and A.2 audit

The full proposed B.2q fragment is in B2_threefold_cofinal_counterexample.tex. B has independently audited the actual file; its requested finite-intermediate-curve and dual-isogeny explanations are now explicit. The source of the Albanese comparison is C_ACMV2026, Theorem3.2/Remark3.3, authorpp12-13. The construction refutes a single constant domination-cofinal Picard diagram, not eventual constancy on one upper cone. All finite symbolic examples are covered by B elliptic_branch_certificate_B.py (11 checks) and C check_threefold_local_geometry.py (11 checks). The latter exact chart certificate ran in0.040636211s and is saved as output/threefold_local_geometry.json.

Root actual file parts/A/overrings_A2_post04.tex passes independent audit; no correction needed. In particular no assertion that an arbitrary Dedekind overring is a localization was used. Parent was notified before the checkpoint build.

## 04:04 UTC — weak upper-cone breakthrough under audit

The regular-birational-model argument is now written by B in B2_regular_model_stabilization.tex and passes our actual-file audit subject to the separately prepared no-torus lemma B.2r. We supplied the generic-fibre restriction and closed-kernel descent proofs. New bad divisorial valuations need not already be divisors on the fixed regular model; each is selected from a failed abelian graph, its allowed centre dimension is maximized, and its proper generic fibre gives a persistent restriction kernel.

Our separate B2_alteration_abelian_realization.tex proposes the general alteration extension. It constructs smooth-over-finite-constants equivariant data by descending a regular Galois alteration over kperf, retaining the semilinear action on finite separable constants. The invariant abelian subgroup realization then uses the Albanese torsor, kills finite translation action, descends along l/l^Gamma, and uses the explicit field homomorphism a -> a^q for the remaining pure extension. B and parent have been asked to audit; this file is provisional, not part of the checked C results.

## 04:10 UTC — all-dimensional weak stabilization proof audited

B wrote the complete extension in parts/B/B2_arbitrary_field_stabilization.tex. Our independent actual-file audit passes without a mathematical correction. The invariant abelian realization has independent audits by B and root; B also audited the full relative-Picard finite-constant sheaf lemma. The final argument retains the source abelian subgroup A_* separately from its isogenous ambient image A0, and the norm degree d multiplies the terminal exponent N before the fixed-Jacobian rank bound. This proves the weak upper-cone formulation over arbitrary fields of positive characteristic. The strong cofinal formulation is still refuted by the two elliptic branches. No claim of novelty or priority is made.

## 04:26 UTC — A.2 refuted by an excellent arithmetic curve

The full proof is now A2_quadratic_tower_counterexample.tex; at parent request an identical copy with A-prefixed labels is parts/A/quadratic_tower_A2_post05.tex. The three local locators are 4: \label{C:A2-wreath-calculation}; 50: \label{C:A2-quadratic-step}; 206: \label{C:A2-persistent-arithmetic-counterexample}.

The quadratic step combines old-prime eventual inertness with injective extension of ideal classes modulo2 and rank doubling. Its key input is a principal prime in a prescribed ray class, followed by an explicit regular-module Kummer extension and quotient; no unproved embedding theorem is used. The dyadic prescription is one unramified nonsquare class per old dyadic prime and square at its other M-primes, so L/F is inert at2 while N/L is split at2. Root and B independently audited all local and transfer steps and the actual full manuscript.

The limit ring is an excellent Dedekind domain R with cd2 Frac(R)=1. Every nonempty open U has infinite-dimensional Pic(U)/2, and every nonempty affine open has cd2(U)=2. The finite-extension Brauer argument uses a uniform lower bound on local two-adic degrees after arbitrary finite base change, not an assumption that inertness itself survives base change. All coefficient passage is explicit.

The seed was simplified from an unused Q(sqrt(-119)) biquadratic candidate to Q(sqrt(-35)), whose entire class-group calculation follows from Minkowski plus the norm x²+xy+9y². An attempted SymPy quartic maximal-order computation for the unused seed failed; no assertion relies on it. The final exact certificate has111784 passed assertions in0.068522112997s and includes an independent reduced-form check of the final seed.

Seven check events were appended. The old construction gate in A2_arithmetic_tower_notes.tex is explicitly marked resolved. Parent owns the final A status and inclusion updates. No original Part C gate remains.

## 04:37 UTC — a single exceptional curve: separable residue implies tame

D_positive_genus_residue.tex proves a weighted different inequality for every finite generically separable cover etale away from a singularity resolved by one smooth positive-genus curve C. It includes all extra exceptional curves after resolving the finite normalization. Contracting rational (-1) curves preserves the map to the original resolution; on the resulting minimal resolution K is nef on every exceptional component. Summed adjunction and projection formulas give the inequality. Every residue-separable cover is tame; in genus1 the residue extension is automatically separable and tameness holds without Q-Gorenstein. Root and D independently audited the actual file; D requested only integral-source and resolution-isomorphism precision, now applied. No new finite example occurs in this general theorem.

Primary Stacks statements independently reopened:0BGP54.14.5,0C2M54.16.8,0C5R54.17.1,0C1D53.12.2,0CD053.13.5,0CD253.13.7. The negative-definite intersection theorem is the previously source-checked D input Kollar2013D10.1, not newly re-read in full here. The remaining higher-genus case has genuinely inseparable residue extension (fierce ramification). Bounded different alone is not asserted to imply finite wild image or finite generation.

## 2026-11-20 04:46 — normalized fierce different: a local obstruction

The proposed bound `(delta-e+1)/e >= 1` is false. The family in `D_fierce_different_obstruction.tex` has Galois group F_q^2 semidirect F_q^*, ramification index q(q-1), purely inseparable residue degree q, and different exponent q^2+q-3. The normalized excess is 2/q, tending to zero in every fixed characteristic. Root and D checked the p case, and root checked its general-q extension. The exact program verifies six finite instances with 1,029,677 assertions. This is a local divisorial extension only, so it does not refute the global surface finite-generation question. The single-curve weighted inequality remains valid but cannot rule out fierce extensions solely through a lower bound on normalized different or by taking self-intersection sufficiently negative.

Opened primary background: Carvajal-Rojas and Yasuda (2025), *On the behavior of stringy motives under Galois quasi-étale covers*, Documenta Mathematica30,709–751, DOI10.4171/DM/1012; Proposition6.5 proof pp742–744 discusses the different/depth formula and degree-p ramification. Opened de Smit, *Ramification groups of local fields with imperfect residue class fields*, author PDF, §§2–4; its double filtration does not supply the disproved lower bound. No assertion in our explicit family depends on these sources.

## Rational exceptional trees in characteristic p

`D_rational_tree_Qfactorial.tex` gives a complete direct proof that a normal surface local ring resolved by a rational SNC tree has class group annihilated by `abs(det(M))*p^a` for one fixed a. The finite thickening exponent does not depend on the chosen numerically trivial line bundle. Both Picard injectivity and unit surjectivity are needed to make the formal trivializations compatible. The conclusion is Q-factoriality; it does not assert that the singularity is rational or that R1fO vanishes. The proof is with root for independent actual-file audit. No finite numerical example appears. Published Tanaka3.25/3.26 has only one irreducible exceptional curve, so we do not silently apply it to a whole tree.

## Completed graded surface cone tameness (post-review research)

The complete proof is in `D_graded_cone_tameness.tex`. It has now passed independent actual-file audits by B and D. The key step is an affine inverse-limit lift group whose kernel is the constant deck group on every test algebra, proved using a finite free Cohen parameter module and the punctured Hartogs/idempotent calculation. Gabber local smallness and divisibility of k* give surjectivity on k-points; faithful flatness of arbitrary commutative Hopf extensions then upgrades this to a finite etale lift of the torus. The commuting deck and torus actions give a positive graded finite algebra; the radial residue extension is separable by equality of the two fixed fields. Thus completed graded normal surface cones have tame radial inertia in every punctured finite cover. The genuine completed boundary DVR is explicitly distinguished from vertex completion.

The blow-up of A1_t times C at (0,c), after deleting the strict transform of A1 times {c}, is Tot(O_C(-c)); near c its chart is t=z u. Therefore the two single exceptional curves R0,R1 in the higher-genus Schroer three-point example satisfy the theorem. Parent and D are reviewing/integrating that global consequence. No priority claim is made, and no finite numerical example is used in the local theorem.


## Post-CP07: weighted graded partial resolutions (05:26--05:30 UTC)

We saved the new two-statement fragment `D_weighted_graded_partial_resolution.tex` for root/B/D actual-file audit. The extraction is the normalized blow-up of the vertex-primary ideal R_N R for a standard Veronese. Local normalized equations T^N=u z^a admit finite regular covers u=r^N, z=s^N, T=r s^a of degree N even when p divides N. Divisor norms give Q-factoriality, including on completed local rings. Stacks 54.11.3 and 54.11.6 descend the completed normalized blow-up exactly, and 54.11.1 supplies the common completed boundary DVR. The only exceptional valuation is radial, hence tame by the already checked lift-group theorem. This adds formally weighted graded omitted points to the mixed global surface theorem. No numerical finite example is introduced.

We also completed and recorded the actual-file audits of D's all-genus Schroer application, B's negative-curve formal linearization, and D's mixed formal-cone global extension. All pass under their stated hypotheses.

The general modification shortcut remains unjustified: making one curve more negative by point blow-ups adds boundary components at which covers can ramify. Applying the one-curve punctured-contraction theorem then requires additional local information. A good contracting action on the entire formal exceptional neighborhood would descend by formal functions to the original completed local ring; one cannot assume arbitrary germs become formally graded by modification.


## Post-CP07: curve fibrations and finite inertia (05:35--05:41 UTC)

The new `D_vertical_fibration.tex` gives four statements. The strongest says that every normal proper surface over an algebraically closed field admitting a nonconstant morphism to a proper curve has finitely generated fundamental group after deleting any finite closed subset. Proper separable homotopy on a dense base open leaves a quotient of the base group. In each finite quotient, the base inertia index divides every retained fibre-component multiplicity. Hence the full profinite inertia image is finite; an open subgroup avoiding the finitely many images is a quotient of a proper curve group. Arbitrary multiple fibres are allowed.

For the automatic fibration consequence, Stein factorization makes F=k(B) relatively algebraically closed in K=k(S). Since F has p-rank one, K tensor_F F^(1/p) is a field: otherwise a non-pth-power t of F would acquire a pth root algebraic in K and therefore in F. Thus the generic fibre is geometrically reduced. Proper flat openness and Stein connectedness give exactly SGA1 X1.4, including singular geometrically reduced generic curves. We do not claim generic smoothness. Smooth retained points, or gcd-one retained multiplicities, give the full proper-base exact sequence; prime-to-p multiplicities retain a simple numerical tame-base generator bound.

Root supplied the finite-inertia strengthening and the automatic Stein-factor consequence; both have been proved in the fragment and sent for root/D actual-file audit.

## 2026-11-20 05:55 UTC: arbitrary-boundary curve fibration

We wrote `D_log_fibration.tex`, with labels `D:log-fibration-criterion` and `D:surface-map-all-boundaries`. The latter proves finite generation of the prescribed fixed-boundary tame quotient for every proper closed boundary on any normal proper surface admitting a nonconstant morphism to a proper curve. The new input beyond the four checked vertical-fibration statements is Hoshi Theorem2.3 plus a finite purely inseparable normalization of the generic curve and its horizontal marked points. Bad-fibre multiplicities bound only the p-part of base inertia, which suffices: finite wild images can be avoided in a finite-index subgroup. We impose no multiplicity-one condition and allow whole deleted fibres. The arbitrary-pencil route remains blocked by uncontrolled new horizontal exceptional valuations. No finite example or program certificate is involved. Root and D actual-file passes for the earlier four vertical-fibration statements were recorded exactly, with root primary-source audit still separate.

## Post-CP07: generic-fibre generation in all dimensions

The full log-fibration fragment passed independent actual-file audits by root, D, and B; root and D also reopened all precise Hoshi/Stacks inputs. It is integrated by D. We then wrote `D_generic_fibre_criterion.tex`: arithmetic exactness over the base function field and normality give the closed normal image of the actual geometric generic fibre, without properness of the open family. A uniform base open follows from the retained relative smooth locus. Full inertia is bounded if every fibre is met; wild inertia is bounded for the prescribed tame quotient even if whole fibres are deleted. This proves all-dimensional vertical-boundary results and arbitrary-boundary results when the normalization of the geometric generic fibre is projective. The latter uses finite pure geometric normalization and the already checked radicial/tame descent. No finite example is used; root requested holding its integration until after CP08.

B independently reopened Schroer1999 printed pp3--4, Sections2.2/2.3/2.5: the two distinct-fibre mutations glue as a normal proper scheme over P1, and the nontorsion difference of marked points forces every descended line bundle to have degree zero on the general curve fibre. Thus a normal proper surface mapping to a curve need not be projective; the fibration theorem has genuine nonprojective scope. We did not introduce another finite example or count this as a new theorem beyond the source-backed observation.

## 06:08 UTC: post-CP08 projective-target fragment

`D_projective_target.tex` proves the fixed-boundary assertion for a normal proper scheme admitting a generically finite morphism toward a projective scheme. Stein factorization gives a birational map toward a normal projective target, and its codimension-one DVRs are unchanged. We opened Stacks0BFP and reread03H0 in full. Source key `C_StacksProjectiveTarget` is pending addition after the bibliography freeze. This fragment is not yet integrated. Overlap with earlier positive cases is not asserted to be empty; a strict new example would be needed to count separate review movement.

## Post-CP08: projective bases and residual inseparability (06:10--06:15 UTC)

The new three-statement `D_projective_base_fibration.tex` extends the generic-fibre method to projective bases of arbitrary dimension. Its new field lemma bounds the inseparable residue degree by one fixed finite pure extension making the chosen upstairs residue field separable. Together with multiplicity transfer this bounds the full wild inertia order e_p*f_insep; bounding e alone would be insufficient. A smooth-surjective retained locus and normalization base change give actual etaleness over a single base open, including codimension-two points. Killing the finitely many bounded wild images produces a quotient of the fixed-boundary group on a finite normal projective base cover. Consequences include arbitrary vertical boundary over any projective image and arbitrary boundary whenever the geometric generic normalization is projective; in particular generic fibre dimension at most one suffices. The draft awaits actual-file audits.

The shorter `D_projective_target.tex` passed D actual-file/source audit; its pending source key is now saved. The all-dimensional curve-base generic-fibre fragment passed B and D actual-file/source audits. All integration remains with D/root.

The three projective-base statements passed D actual-file and independently reopened-source audit with no correction. We independently passed D's two proper-log/log-regular statements using the complete relevant AHLS primary TeX and HoshiA.10. The web PDF endpoint failed, but the preserved primary source and exact theorem proofs were read; the audit record distinguishes those facts.

## 06:23 UTC: finite formal cone covers and boundary cases independently audited

We read both B fragments in full. The finite formal cone-cover proof and its full wild-inertia bound pass, with no assumption that the resulting function-field extension is separable or purely inseparable. Grothendieck existence is applied to a finite formal algebra on the proper resolution, not to a nonproper formal neighborhood in isolation. We independently reopened Stacks 09ZT, 088C, 0BUA and 0BG4. The threshold d>2g-2 is a strict enlargement of the prior formal-isomorphism range.

The torsion equality case also passes: Frobenius and Kummer covers trivialize the line, then Artin--Schreier covers kill the Frobenius-stable cohomology component. The explicit genus-two source has N=omega^{-1} and F^2 H^1(O)=0, giving a cone cover of degree four and full wild-image bounds four/eight on source/target. We requested the finite differential/bound arithmetic certificate; the geometric proof itself passes. Exact reopened sources: 0A3J, 03PK, 0BS2, 0BS6.

The requested additional finite certificate is complete: B/code/check_finite_cone_genus2.py, output/finite_cone_genus2.json; 16 assertions passed in 0.044191410 s. We inspected the entire program and output. The finite example is fully checked.

## Formal retraction audit

We passed both statements in D/D_formal_retraction_root.tex. The exact extra datum is a retraction of the whole formal neighborhood. Frobenius base change along that map makes the normal bundle sufficiently negative, and the remaining relative coordinate obstructions vanish. The completed boundary DVR fields have a common parameter and a purely inseparable coefficient-field extension, so cone tameness descends as zero wild inertia. No generic-field conclusion is inferred merely from radicial infinitesimal fibres. We reopened Stacks04FF in full and used the GE/ramification sources independently reopened earlier in the same sequence.

## Iterated fibration closure

D_iterated_fibrations.tex isolates the exact hereditary base property: every boundary on every finite normal cover has finitely generated fixed-boundary group. The existing projective-base proof only invokes projectivity at that final finite-normalization step, so the replacement is formal. A full induction gives the property for any tower over a projective base whose reduced geometric generic normalizations are projective, in particular every tower of relative dimension at most one. The induction explicitly quantifies over all finite normal covers, so the pure constants needed for geometric normalization are included. We do not count the mere reformulation as separate movement. All maps are globally defined morphisms; rational pencils still leave the exceptional wild gate.
