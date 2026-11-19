"""Serialize manually read source judgments. No keyword-based verdict inference."""
from pathlib import Path
import json,csv
ROOT=Path(__file__).resolve().parents[1]
P='MPL_16+47+54+44'
items=[]; entries=[]
def item(n,sources,kind,cote,scans,lines,words,statement,reconstruction,check,reason,verdicts=None):
    ident=f'SA19-{n}'
    items.append(dict(id=ident,sources=[f'{P}#{x}' for x in sources],kind=kind,cote=cote,scans=scans,lines=[f'{P}_transcription.tex:{x}' for x in lines],his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for k,x in enumerate(sources):
        v=(verdicts or {}).get(x,'kept' if k==0 else 'merged')
        entries.append(dict(entry_id=f'{P}#{x}',item_id=ident,verdict=v,reason=reason))

item(201,[44],'other',47,[3,4],['2087–2108','2142–2153','2167–2215'],
 'Alors φ_L transforme produit de Pontryagin * en produit ordinaire; cqfd.',
 'For an abelian scheme A/S, an S-scheme X and a line bundle L on A×_S X, rigidified along 0×X and fibrewise algebraically trivial, the integral transform Φ_L sends derived Pontryagin convolution of perfect complexes to their derived tensor product. The page reduces to the Poincaré kernel on the dual abelian scheme and calculates the natural isomorphism using base change, projection, Künneth and the theorem of the square.',
 'The resolution of parf|prof as Perf, and standard finiteness hypotheses needed for operations, are modern interpretation. The following page supplies an actual proof; the initial proposition is not merely an unsupported assertion.',
 'understates','The entry correctly identifies the universal reduction and base-change issue, but calls the proposition unproved although scan 4 supplies the calculation ending cqfd. The unbounded marginal extension is a separate claim.',{44:'corrected'})
item(202,[45],'idea of the earlier run',47,[3],['2113–2140'],
 'quelconques faisceaux L,L′,L″; π:P×Q→R',
 'A specified kernel isomorphism (π×id_X)^*L ≅ pr_13^*L′ ⊗^L pr_23^*L″ induces a binary compatibility between an integral transform of convolution and a tensor product, provided all pushforwards have proper support and derived pullbacks/tensor products lie in the chosen categories. The margin first treats a flat group scheme with inputs having proper support.',
 'The earlier run adds precise support/Tor requirements and notes that monoidal associativity and unit coherence need additional compatible data. It does not assert that the manuscript already proves those data.',
 'agrees','The three-kernel suggestion and the flatness/proper-support qualifications occur in the margin; the categorical coherence discussion is explicitly the earlier run’s extension.')
item(203,[46,47,48],'unproved claim',47,[4,5,6],['2217–2224','2228–2235','2258–2276','2296–2309','2326–2330'],
 'Ls_A^* suivi de τ_A[-n]; τ_A≃Λ^n t_A≃Λ^n t_B; K est l’anti-diagonale',
 'For dual abelian schemes A,B of relative dimension g and normalized Poincaré kernel, the corrected composite is Φ_{P^t}Φ_P(F) ≅ (−1_A)^*F ⊗ π_A^*det(Lie A)[−g]. The determinant lines for A and B are canonically identified. Thus on K_0 the composite is (−1)^g[π_A^*det(Lie A)](−1_A)^*. The anti-diagonal is the zero fibre of addition and is the graph of inversion.',
 'The K_0 formula is the earlier run’s direct consequence. A line on the base has rank one but need not have K_0 class one. The old identity target survives in the proof, and the earlier K-theory theorem has not received the determinant correction visibly inserted into the derived theorem.',
 'agrees','These entries address one corrected inversion statement. The source supplies the kernel argument but leaves Lemma 1 dependent on an unfinished compatibility check. The initial identity is explicitly corrected at the theorem; the later retained identity target is a textual inconsistency, not a second valid theorem.')
item(204,[49],'unproved claim',47,[7],['2334–2353'],
 'L alg. équivalent à zéro, et non isomorphe à O_B; Nous allons ici admettre le lemme 2',
 'For an abelian variety B over an algebraically closed field and a nontrivial algebraically trivial line bundle L, H^i(B,L)=0 for every i. It implies that the Poincaré direct image is supported on the zero section but does not alone determine its scheme-theoretic support, shift or determinant line.',
 'B replaces the formula’s unexplained X solely in this modern statement. The admission and attribution to Mumford are explicit; the separate proof needed at the zero section is not supplied by support vanishing.',
 'agrees','The page expressly admits the vanishing lemma, and the entry correctly limits what follows from it.')
item(205,[50,51],'self-flagged step',47,[7,8],['2350–2377','2381–2393'],
 'on prend alors l’hom identique; à faire une vérification de compatibilité.....',
 'The manuscript constructs Rp_*P → e_*τ[−g] from the top base-change map and R^gq_*O_B ≅ det Lie(B^∨), then asks whether it is an isomorphism on derived point fibres. For a regular zero section with tangent bundle T and τ=det T, H^i(Le^*e_*τ[−g]) ≅ Λ^{g−i}T^∨⊗det T ≅ Λ^iT for 0≤i≤g. Equal fibre dimensions do not establish that this particular morphism is invertible.',
 'The Koszul calculation and perfect-cone criterion are the earlier run’s proof plan; the equality of the actual comparison map on the unit fibre remains unproved on the pages.',
 'agrees','Both entries concern the same expressly unfinished unit-fibre compatibility. They are merged without treating an object-level dimension calculation as a check of the map.')
item(206,[52],'idea of the earlier run',47,[6],['2280–2294','2312–2330'],
 'K=Ker ψ; O_K est parfait sur C',
 'For a homomorphism ψ:C→B^∨ and its associated normalized line bundle N, derived base change gives Rpr_{C*}N ≅ Lψ^*(e_*τ[−g]). If ψ is flat and surjective, K=ker ψ is the regular inverse image of the zero section and the expression becomes O_K⊗_Sτ[−g]; O_K is perfect on C. Without flatness a derived fibre, with higher Tor, is required.',
 'The missing e_* in the first corollary display is flagged, not inserted into the transcription. Flatness is a written hypothesis of the specialization.',
 'agrees','The entry correctly keeps the zero-section pushforward in the reconstruction and distinguishes the general derived pullback from the flat specialization.')
item(207,[53],'idea of the earlier run',47,[8],['2395–2406'],
 'L_t … τ[-n]e_{−t}; Φ_L(F)*e_t',
 'With T_t(b)=b+t and P_t=P|_{A×{t}}, Φ(F⊗P_t)≅T_t^*Φ(F), whereas convolution by δ_u gives T_{−u}^*. Thus the compatible skyscraper in the last formula is δ_{−t}. The preceding Φ(P_t)=τδ_{−t}[−g] is consistent with that convention. Virtual rank of Φ(F) equals χ(F), and χ(Φ(F))=(−1)^g rank(F).',
 'This is a convention-fixed sign calculation of the earlier run. It supplies a scan-check alternative, not an emendation of e_t.',
 'agrees','The entry observes an actual difference between the two written signs and correctly distinguishes translations from convolution by a skyscraper.')
item(208,[54],'idea of the earlier run',47,[9],['2425–2447'],
 'Heuristiquement, on devrait avoir; χ exp(−D′/χ)',
 'If L is ample on an abelian variety over an algebraically closed field, r=χ(L)>0 and E=Φ_P(L), then E is a rank-r bundle; for φ_L:A→A^∨ one has φ_L^*E≅H^0(A,L)⊗L^{−1}. For D′=−c_1(E), rational Chow pullback gives ch(E)=r exp(−D′/r).',
 'The ample field hypotheses are the earlier run’s restricted case. The manuscript asks about all line bundles with nonzero Euler characteristic over a general base and writes a formal fractional line bundle in quotation marks. No such line bundle is constructed.',
 'agrees','The note states its restricted geometric setting explicitly and does not convert the formal fractional-power notation into an actual bundle.')
item(209,[55,56],'idea of the earlier run',47,[9],['2440–2465'],
 '(1−D′/χ)^χ; χ(χ−1)/(2χ)',
 'For r≠0 the displayed generating expression has c_k=(−1)^k(r−1)…(r−k+1)D′^k/(k!r^{k−1}). The expanded quadratic and cubic manuscript coefficients have one extra factor r. On A=E_1×E_2 over C, L=O_{E_1}([0])⊠O_{E_2}(2[0]), the actual transform has c_2-number 1, while the literal expanded coefficient yields 2. Thus the written expanded identity fails even cohomologically under all the ample field hypotheses.',
 'The coefficient correction and elliptic-product example are the earlier run’s mathematics, rerun here. The ink is not changed; a missing exponent or an authorial arithmetic slip remains for scan review.',
 'agrees','The two entries check the same coefficient discrepancy; one is the formal calculation and the other realizes it geometrically, so they are merged.')
item(210,[57],'idea of the earlier run',47,[9],['2463–2468'],
 'provient d’un cycle à coeff. entiers',
 'In the ample field setting of SA19-208, the manuscript’s final coefficient ((r−1)…(r−k+1)/(k!r^{k−2}))D′^k equals (−1)^k r c_k(E), and therefore has an integral algebraic cycle lift in rational Chow or cohomology. This weaker statement survives the incorrect identification of that coefficient with c_k(E).',
 'The relation to actual Chern classes is an earlier-run deduction; it does not imply an integral Fourier transform on all Chow classes, equality sensitive to torsion, or the unrestricted base case.',
 'agrees','The final integrality coefficient is genuinely one power of r different from the corrected Chern class, as the entry says.')
item(211,[58],'self-flagged step',47,[9],['2432–2468'],
 'ces formules sont-elles bien vraies mod torsion?',
 'The page asks whether the formal Fourier-transform character/Chern formulas hold modulo torsion. Rational Chow equality for an individual transformed bundle is distinct from constructing an integral transform on the entire Chow group and distinct from a torsion-sensitive equality in K-theory or a chosen filtration.',
 'The comparison with integral Fourier transforms is the earlier run’s extension. The page does not specify which filtration Gr or which integral lifting property is intended.',
 'agrees','The question is explicit, so it is indexed as a self-flagged problem rather than merely an unpursued implication.',{58:'corrected'})
item(212,[59],'idea of the earlier run',47,[10],['2473–2484','2505–2524'],
 'par R.R.; T= Todd(t_A)',
 'In a rational intersection theory admitting GRR for the smooth proper morphisms used, ch(x*y)=(ch x*ch y)Td(Lie A), while ch Φ_P(x)=Ψ_P(ch x)Td(Lie A). The projection formula then cancels the two equal base Todd factors and gives Ψ_P(a*b)=Ψ_P(a)Ψ_P(b). A Todd class is invertible in the finite-dimensional graded setting because its constant term is one.',
 'The earlier run specifies a valid RR framework and does not identify the manuscript’s undefined Gr for arbitrary S.',
 'agrees','The two displayed Todd contributions occur in the retained calculation; the canceled earlier calculation is not used as a theorem.')
item(213,[60],'idea of the earlier run',47,[11],['2529–2542'],
 '(-1)^n T ch ω_A',
 'Keeping both bases’ tangent bundles gives Ψ_A(ab)=(−1)^g(Ψ_A(a)*_BΨ_A(b))Td(Lie A)Td(Lie B)ch(det Lie(A)^∨). The extra factor is Td(H^1_dR(A/S)) by the Hodge exact sequence. Under Moonen’s stated smooth-base hypotheses that Todd class is one in CH(S)_Q.',
 'This is the earlier run’s convention-controlled reconstruction. The manuscript display omits a convolution star and appears to retain only one Todd factor; neither is silently repaired.',
 'agrees','The note correctly isolates two separate issues: a missing output star and incomplete relative Todd bookkeeping. The cited Moonen work is first circulated in 2024 and assigned to a January 2026 volume; both dates are retained in the reference audit.')
item(214,[61],'unproved claim',47,[11],['2531–2548'],
 'le facteur (-1)^n',
 'For the normalized Poincaré Fourier transform on rational Chow groups of an abelian variety of dimension g over a field, the two products are interchanged with Ψ(a*b)=Ψ(a)Ψ(b) and Ψ(ab)=(−1)^gΨ(a)*Ψ(b). The square is (−1)^g(−1)^*.',
 'The output star in the second formula is a modern statement supported by the literature; the literal source display has juxtaposition.',
 'agrees','The note supports the parity factor in a precise field setting, while leaving the actual printed omission to scan review.')
item(215,[62],'reading question',47,[11],['2543–2548'],
 'Kleiman dans “10 Exposés ...” … n’a pas tenu compte du facteur (-1)^n',
 'The manuscript attributes a missing parity factor to Kleiman. Verification requires identifying his Fourier convention and the exact asserted formula, not merely finding a related convolution-to-cup identity.',
 'The notes’ identification of Kleiman 1968 §§2A12–2A13 is a lead. The converse-product allegation is not established by the comparison alone.',
 'agrees','The source contains the allegation, but neither a locator nor the relevant converse formula. The note appropriately leaves the historical allegation unresolved.')
item(216,[63],'idea of the earlier run',47,[11],['2550–2570'],
 'Φ_L(check F⊗ω_A[n])≃Φ_L(F)^∨',
 'For perfect F and ordinary derived dual F^∨, smooth proper duality gives Φ_P(F)^∨≅Φ_{P^∨}(F^∨⊗π_A^*ω_A[g])≅(−1_B)^*Φ_P(F^∨⊗π_A^*ω_A[g]). The written same-kernel formula is compatible if check F means (−1_A)^*F^∨; that convention is absent on these pages.',
 'The proposed meaning of the check is an explicit conditional reconstruction, not a transcription decision. The final automorphism equivariance is a further compatibility, with actions u.F left undefined.',
 'agrees','The note keeps inverse kernel and dual/inversion conventions separate, as the text requires.')
item(217,[64,85],'other',None,[],[],
 '',
 'These are two editorial bibliography sections, containing literature leads for Fourier–Mukai theory, abelian duality, intermediate Jacobians, and the other mixed-package topics. They contain no independent claim of Grothendieck.',
 'References are independently opened and checked in the research audit; source-list membership is not a theorem verification.',
 'not on the page','Both headings are editorial reference lists, with no corresponding manuscript statement. They are retained together as a bibliographic item, rather than assigned an invented manuscript location.')
item(218,[65],'unproved claim',54,[3],['2611–2645'],
 'Je dis que cette extension n’est autre que S_B; t_E=H^1(B)',
 'Let A be an abelian variety and B=A^∨. Its universal vector extension has kernel with tangent space H^1(A,O_A)^∨=Lie(B)^∨; its tangent exact sequence canonically identifies with 0→H^0(B,Ω_B^1)→H^1_dR(B)→H^1(B,O_B)→0. Invariant one-forms on E(A), by contrast, identify with H^1_dR(A).',
 'The vector-group convention is translated so that tangent spaces agree. The source writes V(t_B^∨), whereas some references define V(M)=Spec Sym M, contravariantly. The isomorphism requires the universal property, not dimensions alone.',
 'agrees','The note precisely preserves the A/B variance of the written tangent sequence.')
item(219,[66],'unpursued implication',54,[3,5],['2646–2652','2685–2694'],
 'H^1(A) et H^1(B) sont duaux l’un de l’autre',
 'Poincaré duality between dual abelian varieties yields a perfect degree-one de Rham pairing compatible with the two Hodge exact sequences. Exterior powers produce degree-r pairings, and on Hodge pieces H^p(A,Ω_A^q) is paired with H^q(B,Ω_B^p). No canonical splitting of the Hodge sequences is asserted.',
 'The exterior-power argument is explicitly an earlier-run extension. Ω_A on B in the source is a reading alarm; Ω_B is used only in the modern formulation.',
 'agrees','The degree-one comparison and proposed exterior-algebra reduction are written on the pages; the note does not assume a splitting.')
item(220,[67],'unproved claim',54,[5,7],['2696–2701','2716–2725'],
 'F^A et F^B sont orthogonaux l’un de l’autre',
 'Over a perfect field of characteristic p, under the Cartier/Weil duality A[p]^D≅B[p], the annihilator of ker(F_A:A→A^(p)) is ker F_B, with Frobenius twists retained. The factorization [p]=V_AF_A yields 0→ker F_A→A[p]→(ker F_B)^D→0. The two kernel ranks are p^g and rank A[p]=p^(2g).',
 'p^A is interpreted as the finite group scheme A[p], not its geometric points. Twists and the direction of duality are explicit modern notation.',
 'agrees','The page states orthogonality and sketches it using transposed F/V sequences; equal ranks alone would not establish the pairing claim.')
item(221,[68],'unpursued implication',54,[7],['2727–2730'],
 'extension de p-alg. de Lie abéliennes; puissance p-ième nulle',
 'A finite-dimensional restricted Lie algebra in characteristic p corresponds to a finite infinitesimal group scheme of Frobenius height at most one. Therefore the restricted structure on the Hodge extension, including zero p-operation on its additive kernel, is part of the proposed radicial-group extension. An ordinary Lie algebra does not determine an arbitrary p-torsion group scheme.',
 'The height-one restriction is the earlier run’s necessary precise scope. A[p] generally has higher Frobenius height, so applying this equivalence directly to all of A[p] would be wrong.',
 'agrees','The inserted zero p-power and the radicial extension are visible. The note correctly limits the Lie/group correspondence.')
item(222,[69],'conjecture',54,[7],['2721–2730'],
 'Cette extension peut-elle se déduire de la connaissance de p^A ??',
 'For an abelian variety over a perfect field of characteristic p, its finite group scheme A[p], equivalently its Dieudonné module with F and V, determines H^1_dR(A) with its Hodge subspace. The question on the sheet also asks to recover its particular restricted Lie extension; that requires matching the semilinear p-operation and variance conventions.',
 'The filtered Dieudonné realization is the established precise formulation. The abstract finite group A[p](k̄) is insufficient. Identification of the sheet’s restricted operation is not inferred merely from a vector-space isomorphism.',
 'agrees','The note locates the exact question and correctly states the extra operator comparison that remains necessary to match it literally.')
item(223,[70],'reading question',54,[4,6],['2658–2677','2707–2710'],
 'M_f soit libre sur A_f; pour tout changement de base',
 'The reused typescript contains (i) a canceled generic-freeness refinement over an irreducible possibly nonreduced base with generic flatness, (ii) a canceled nilpotent/adic flatness criterion whose extension after deleting nilpotence is false as literally written, and (iii) Proposition A: after shrinking the base, a finitely presented closed stratum universally represents flatness of a finitely presented sheaf, with simultaneous freeness on a chosen finite affine cover.',
 'The earlier run’s noetherian-domain generic-freeness theorem checks only a reduced special case. The nonreduced generic-base and universal flattening content must be recorded separately; the deleted assumption and missing predecessor 4.1 bis cannot be supplied from the note.',
 'understates','The note correctly distinguishes generic flatness from a universal stratum, but it omits the nonreduced and nilpotent criteria on scan4. The nonnilpotent amendment has counterexample A=k[t], I=(t), A1=k[t,t^-1], M=A/(t): all written tests hold but M moduloI² is not flat. Nilpotent refinement and universal relation-ideal construction are audited separately.',{70:'corrected'})
item(224,[71],'idea of the earlier run',44,[3],['2809–2840'],
 'sur les modules gradués … TF … est exact et fidèle',
 'For a noetherian nonnegatively graded ring with an adic degree filtration, the completion is flat. For finitely generated graded modules, the usual graded completion equals the degreewise product and is faithful on that graded category. The undefined TF extension and the final inserted remark cannot be read as faithfulness on all ungraded modules: k[x]/(x−1) becomes zero after tensoring with k[[x]].',
 'The counterexample tests the omission of grading, not the source’s qualified statement. The cancellation chronology of the final inserted line remains undecided.',
 'agrees','The entry expressly avoids refuting the actual graded claim with an ungraded example; it correctly flags TF and cancellation order.')
item(225,[72],'reading question',44,[2,8,9],['2787–2800','2970–2979','2991–2995'],
 'équivalence d’Albanese; une relation d’équivalence que je ne sais pas bien identifier',
 'The pages construct quotients of parameter Albanese varieties through divisor correspondences and hope for abelian varieties P^i/J^i attached to algebraically trivial codimension-i cycles. A close later formulation is the incidence quotient A^i(X)/K_inc^i(X), where every correspondence from X to a smooth projective Y of codimension dim(X)−i+1 sends K_inc to zero in Pic^0(Y). This differs from universality among every regular homomorphism.',
 'Identification with Saito’s Picard-homomorphism construction is this run’s historically supported comparison, not a recovered missing definition. The earlier run’s algebraic representative is a second candidate, and the Abel–Jacobi image is a third.',
 'understates','The note is right not to identify the objects from dimension alone, but its focus on universal regular representatives misses the closer incidence/Picard construction and Grothendieck attribution in Saito 1979, Proposition 3.4 and Theorem 3.6.',{72:'corrected'})
item(226,[73],'unproved claim',44,[2,8],['2793–2803','2974'],
 'majorée par un nb ne dépendant que de X [en fait, par ½ b^(2i−1)(X)!]',
 'The programme’s boundedness strategy seeks dim P_ξ≤b_(2i−1)(X)/2 uniformly over cycle families. For the incidence/Picard-homomorphism interpretation, Saito’s Proposition 3.4 proves the all-codimension Betti bound, explicitly attributing the argument to Grothendieck. Kahn’s repaired codimension-two theorem concerns the stronger universal-regular-homomorphism problem and cannot be substituted as the only fate of this claim.',
 'The universal-regular and Picard subclasses are distinguished. The programme’s undefined N(ξ) still prevents an unconditional assertion that its exact integral quotient has been recovered.',
 'understates','The earlier note gives a correct codimension-two comparison but omits the all-codimension incidence theorem closest to the written construction.',{73:'corrected'})
item(227,[74],'conjecture',44,[8],['2974–2976'],
 'c’est même un sous-module dudit',
 'The letter first asserts a Tate-module subquotient of H^(2i−1)(X,Z_ℓ(i)) and conjectures an actual submodule. For modern surjective regular homomorphisms to B and a miniversal cycle inducing [r]_B, an injective realization into cohomology modulo torsion is established for i=1,2,dim X and ℓ different from the characteristic and prime to r. Rational realizations of incidence quotients require a different comparison.',
 'The excluded primes, chosen cycle, torsion quotient and restricted codimensions are genuine qualifications. Over the letter’s algebraically closed field, however, a bare Z_ℓ-module subquotient surjecting onto finite free T_ℓJ already splits abstractly, yielding a noncanonical embedding. A substantive stronger conjecture must require a natural, correspondence-induced or equivariant embedding; those additional words are not supplied by the letter.',
 'understates','The note carefully preserves the modern theorem’s qualifications but does not observe that the bare abstract module implication follows from projectivity of T_ℓJ. The geometric meaning of the stronger wording therefore remains a reading/context question.',{74:'corrected'})
item(228,[75],'unpursued implication',44,[8],['2974–2979'],
 'Je suis moralement sûr que ce sont “les bonnes”',
 'For a smooth projective complex variety, the Abel–Jacobi image of algebraically trivial codimension-i cycles is an abelian variety; it need not be the universal algebraic representative in intermediate codimension. Ottem–Suzuki exhibit a complex fourfold in codimension three with a nontrivial isogeny between a universal regular target and the Abel–Jacobi image.',
 'This is a test of one possible identification, not a refutation of the manuscript’s incidence-like construction or of existence of its own quotient. The phrase “the good ones” carries no universal property by itself.',
 'agrees','The entry correctly distinguishes existence from identification and does not claim the example refutes Grothendieck’s unspecified relation.')
item(229,[76],'unproved claim',44,[4],['2850–2874'],
 '〈ζ,ζ′〉=(-1)^m Z.Z′; énoncé plus général … fibrations … variante locale',
 'For X smooth projective of dimension n, a generic hyperplane section Y of a pencil with geometrically integral fibres, and cycles Z,Z′ of codimensions i,j with i+j=n whose restrictions to Y are algebraically trivial, the source proposes an equality between a Néron–Tate pairing of their intermediate-Jacobian classes and (−1)^m deg(Z·Z′). The height normalization, primitive sign, vertical corrections and m outside the middle case are not specified.',
 'A modern geometric-height statement must fix the base curve degree, models and vertical orthogonality. The earlier run’s abelian-variety/number-field height result is only an analogy and does not supply these missing hypotheses.',
 'agrees','The note explicitly limits its later comparison and preserves the source’s unresolved sign and extension invariance.')
item(230,[77],'idea of the earlier run',44,[2,8,9],['2802–2803','2979–2981','2989–2995'],
 'A prouver que cette dernière est positive !; décomposition primitive',
 'For dim X=2m−1 and a pointed smooth connected parameter variety T with z∈CH^m(T×X), z(a)=0, the manuscript forms D=r_*(p^*z·q^*z), a symmetric divisor correspondence. After quotienting its Albanese kernel it asks that the descended class be a polarization. Symmetry and nondegeneracy alone do not imply ampleness: the negative of a polarization is still a symmetric isogeny. Primitive decomposition is expressly flagged.',
 'The negative-polarization example tests an invalid inference, not this particular D. This run additionally tests the preceding descent: for X=T=E over C, End(E)=Z, m=1 and z=2c_1(P), D induces ±4 on E. Quotient by its full kernel E[4] is [4]; pullback of an integral correspondence on the quotient multiplies its endomorphism by 16, so descent would require ±1/4. A connected-kernel quotient or rational coefficients avoids this obstruction. These are explicit alternative formulations, not ink decisions. The positivity problem independently requires primitive signs and algebraicity.',
 'understates','The earlier note correctly isolates the positivity gap, but assumes the asserted descent without checking the full-kernel and integral-coefficient issue. The displayed elliptic example refutes literal integral descent through the full kernel while leaving the intended convention open.',{77:'corrected'})
item(231,[78],'reading question',44,[6],['2942–2944'],
 'L’équivalence numérique = τ-équivalence',
 'If τ-equivalence means algebraic equivalence after a nonzero integral multiple, numerical=τ holds for divisors on a smooth projective variety. In arbitrary codimension it fails: on a very general smooth quintic threefold over C, Clemens produces non-torsion homologically trivial classes modulo algebraic equivalence; such classes are numerically trivial.',
 'The meaning of τ is not defined locally, so the all-codimension refutation is conditional on that meaning. It is not a proof of an ink error or permission to add “divisors” to the transcription.',
 'agrees','The note correctly separates the verified divisor theorem from a counterexample to the unrestricted interpretation, with its definitional condition explicit.')
item(232,[79],'idea of the earlier run',54,[8],['2740–2750'],
 'un ensemble localement fini d’hyperplans affines; mur mitoyen de deux chambres',
 'For a locally finite affine-hyperplane arrangement in a finite-dimensional real affine space, a compact segment meets only finitely many hyperplanes. A chamber is the intersection of its wall half-spaces. Each hyperplane supports adjacent chambers; the relative interior of a particular wall is a chamber of the induced arrangement and has a unique adjacent chamber on the other side, constant along that relative interior.',
 'The elementary compactness/local-ball argument is the earlier run’s verification under explicit real affine hypotheses. It does not assert that only two chambers globally meet an entire hyperplane. The typescript’s original provenance is not identified.',
 'agrees','The note’s local two-sided argument agrees with Corollaries 2–3, whose proof runs off the supplied sheet.')

expected={*range(44,80),85}
assert {int(x['entry_id'].split('#')[-1]) for x in entries}==expected
assert len(entries)==37
(ROOT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
with (ROOT/'entries.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(sorted(entries,key=lambda x:int(x['entry_id'].split('#')[-1])))
print(f'Serialized {len(items)} manually adjudicated items covering {len(entries)} assigned entries.')
print('Verdicts:',{v:sum(e['verdict']==v for e in entries) for v in sorted({e['verdict'] for e in entries})})
print('All item locators refer to the original mixed-package transcription, with true cote retained.')
