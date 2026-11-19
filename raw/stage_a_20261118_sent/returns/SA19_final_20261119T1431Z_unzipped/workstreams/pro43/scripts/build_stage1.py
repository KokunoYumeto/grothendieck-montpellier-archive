"""Serialize individually adjudicated notes; no keyword-derived verdicts.

All judgments were composed after the complete entry/passage reading recorded in
reading_log.md. Line numbers are those of the aggregate Pro transcription.
"""
from pathlib import Path
import json, csv
BASE=Path(__file__).resolve().parents[1]
items=[]; rows=[]
def add(n, entries, kind, scans, lines, words, statement, reconstruction, check, reason, verdict='kept'):
    entries = [entries] if isinstance(entries,int) else entries
    ident=f'SA19-{n}'
    items.append(dict(id=ident,sources=[f'MPL_43_094-142#{e}' for e in entries],kind=kind,cote='43',scans=scans,lines=lines,his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason))
    for j,e in enumerate(entries):
        rows.append(dict(entry_id=f'MPL_43_094-142#{e}',item_id=ident,verdict=verdict if j==0 else 'merged',reason=reason if j==0 else f'Merged into {ident}: '+reason))

add(1,1,'unpursued implication',[102,128,132,133],'300–326;1394–1423;1524–1613','Théorie de Rosenlicht locale; autodualité de la Jacobienne',
'The local class group J_{K/k}, cohomology of a complete nonsingular curve, and the self-duality of its Jacobian organize this range. The range supplies cohomological duality ingredients rather than a modulus construction or an arithmetic section map.',
'Scope comparison belongs to the earlier run; the negative finding is restricted to the 46 supplied faces, all read. Earlier cote43 and external theorem149 are not covered by this item.','agrees','The actual pages contain local Rosenlicht theory and the complete-curve Kummer table; the proposed arithmetic construction is absent.')
add(2,2,'idea of the earlier run',[113,132,133],'842–882;1524–1613','On a une suite exacte de C-groupes',
'The earlier run proposes comparing local/curve duality with a later generalized Abel map and Kummer section argument in an external project.',
'No arithmetic section theorem or the named external theorem149 is supplied. Its exact target, hypotheses, and attribution remain unverified; this is a project lead only.','not on the page','The source supports duality ingredients, not the proposed 1983 arithmetic-section proof.', 'corrected')
add(3,[3,4],'idea of the earlier run',[109,112,120,132],'656–718;786–840;1220–1226;1524–1531 (context only)','G=G_m; G_m→nG_m',
'The earlier run tests an external units assertion: Q× is {±1}⊕⊕_{prime q} Z and is not finitely generated, but ∩_{n≥1}(Q×)^n={1}; for Z[1/6]×={±2^a3^b}, the same intersection is {1}.',
'These are independent arithmetic examples, absent from the manuscript. The valuation proof distinguishes finite generation from having no nonzero infinitely divisible element.','not on the page','Both examples are earlier-run calculations rather than Grothendieck claims; they are valid and separately re-proved in computations.md.','corrected')
add(5,[5,22],'reading question',[120],'1215–1226','partie discrète de H¹(K,A) ... divisible',
'The asserted divisibility concerns the discrete part of a geometrized H¹(K,A) for an abelian variety over the local field; it does not concern K× or units of an arithmetic base.',
'A modern sheaf realization must be specified before discrete part can be identified with a particular quotient. This is not a theorem about S-units.','agrees','The line names H¹(K,A), not units. Entry22 repeats the scope correction and external-project caution.')
add(6,6,'unpursued implication',[132,133],'1524–1539;1568–1582','0 → μ_n → G_m → G_m → 0',
'The curve Kummer long exact sequence relates Pic/n, H²(μ_n), and n-torsion in the Brauer group. It is the dimension-one counterpart of cote16 scan21 (8.7), which separates NS⊗Z_l and the Tate module of Br.',
'The cross-folder comparison is ours and the earlier run’s; the two dimensions have different Brauer behavior and must not be identified.','agrees','Both exact-sequence passages were read; cote16 requires its stated divisibility and finite-generation assumptions.')
add(7,7,'reading question',[132],'1533–1539','Pic(C/k)(k); H²(k,G_m)',
'The five-term Picard–Brauer sequence distinguishes line bundles on C from k-points of the relative Picard scheme. A k-rational point removes the usual obstruction, but is not explicitly supplied here.',
'Use the fppf Leray five-term sequence for a smooth proper geometrically connected curve; do not silently identify Pic(C) with Pic_{C/k}(k).','agrees','The actual display contains the obstruction term; suppressing it would strengthen the page.')
add(8,8,'unproved claim',[132,133],'1541–1563;1588–1605','on se ramène au cas géométrique',
'The finite étale coefficient σ in curve duality is reduced to the geometric case and then to Q/Z, with a direct-limit formula for H²(C,Q/Z). Base-change and coefficient-transition maps are not expanded.',
'The finite-level curve calculations are established after fixing the geometric site; descent and passage to Q/Z require continuity. This is distinct from the local Weil-site comparison on scans94–95.','agrees','The entry concerns the explicit geometric/finite-coefficient reduction on the curve pages, not a general perfection assertion. Its limit qualification is retained.')
add(9,[9,23],'unproved claim',[133],'1576–1583;1601–1604','H¹(C,Q/Z)=Hom(T(J),Q/Z)',
'For a smooth proper geometrically connected curve over an algebraically closed field, H¹_et(C,Q/Z) is the group of continuous torsion characters of its profinite abelian fundamental group, canonically related through the Jacobian to its étale Tate modules.',
'The full finite group scheme J[p] must not be substituted for the étale realization; T(J) and the topology of Hom must be declared. The displayed geometric formula is not a formula for arithmetic H¹ over arbitrary k.','agrees','Both entries concern the same Tate-module character formula and its realization. The later p-torsion display requires the separate correction in SA19-10.')
add(10,10,'reading question',[133],'1580–1586','π₁(C)⊗Z/p ≃ J[p]',
'The profinite étale fundamental group modulo p cannot generally equal the full finite flat group scheme J[p]. For a supersingular elliptic curve the étale p-quotient is trivial whereas J[p] has rank p².',
'A realizational symbol or duality sign may be missing. Plausible alternatives use J[p]^{ét} or a Cartier/Serre dual object; the ink is not decided.','agrees','The dangerous identification is present in the transcription and is not repaired by the preceding H¹(C,Z/p) formula.')
add(11,11,'self-flagged step',[133],'1565;1585','idèles; adèles',
'The margin proposes deriving the finite coefficient table from multiplication by n on idèles and Frobenius on adèles.',
'No complexes, normalizations of residues, or compatible chain maps are supplied. The proposal is a construction problem, not a proof of the displayed table.','agrees','Only the named computational route is written; the actual chain-level construction is absent.')
add(12,12,'unproved claim',[112],'786–822','μ_p; Z/p; α_p',
'For a field K of characteristic p, flat Kummer, Artin–Schreier and Frobenius sequences give H¹(K,μ_p)=K×/K×p, H¹(K,Z/p)=K/(F−1)K and H¹(K,α_p)=K/Kp. The prime-to-p rows additionally use local geometric realization.',
'The basic H¹ identities are ordinary fppf/étale identities; geometric group structures and dualities require the residue-field realization. H⁰(μ_p)=H⁰(α_p)=0 means trivial abstract groups over a field, not zero group schemes.','agrees','The rows and the additive versus multiplicative distinction were checked against the source; α_p has the additive quotient.')
add(13,13,'self-flagged step',[112],'824–839','G_m ... ??; Z ... ??',
'The author sketches the G_m/Z portion of local duality and questions how the Z-side higher cohomology and the local multiplicative group fit the derived dual.',
'One must distinguish an abstract group, its geometrized sheaf, and its derived/profinite completion. No complete isomorphism is established by these rows.','agrees','Both question marks survive in the displayed scratch work.')
add(14,14,'reading question',[109],'656–718','Ext¹(G_m,Z/n)=μ_n^∨',
'The page compares extension groups of algebraic/Weil sheaves with finite roots-of-unity duals and characters of k×. Ext in a sheaf category and Ext of the group of k-points are distinct.',
'A finite-field realization and its derived shift can explain the comparison; an arbitrary-field equality with all abstract characters is not supported. The μ_p and direct/inverse-limit readings need the specified site.','agrees','The categories change within the calculations and the final character expression is a margin note, not an unconditional equality.')
add(15,15,'unproved claim',[117],'1028–1040','π₀(A) et π₀(B) duaux dans Q/Z',
'The component groups of the Néron models of mutually dual abelian varieties are expected to be in perfect duality through Grothendieck’s pairing over a complete discretely valued field with perfect residue field.',
'The modern hypothesis perfect residue field and identification of the pairing are made explicit; the page itself is schematic and does not prove perfectness.','agrees','The pairing and reciprocal H¹/Ext formulas are written without a proof.')
add(16,16,'unproved claim',[119],'1143–1154','0 → B(K)⊗Q/Z → H¹(K,B(tors)) → H¹(K,B) → 0',
'The Kummer direct limit gives 0→B(K)⊗Q/Z→H¹(K,B_tors)→H¹(K,B)_tors→0; replacing the final torsion subgroup by the whole H¹ requires a torsion theorem.',
'For an abelian variety over a field, torsors become trivial over a finite extension and H¹ is torsion. The first term is a tensor product; there is no canonical map B(K)→B(K)⊗Q/Z without a chosen element of Q/Z.','agrees','The retained tensor term is essential and cannot be deleted merely because some cohomology component is divisible.')
add(17,17,'self-flagged step',[116],'981–1008','plus grand quotient compact; complété profini',
'The double-dual spectral sequence suggests a completion of the realized object rather than literal identity before completion.',
'In the modern Serre-dual ind-rational setting, the correct bidual depends on the unipotent, semiabelian and discrete pieces; the incomplete symbol Δ|0 does not specify one universal completion functor.','agrees','The completion is explicitly in the margin and the relevant degree is uncertain.')
add(18,18,'self-flagged step',[120],'1185–1199;1228–1229','H¹(K,B_n) → Ext¹_kgr(A,Z/n) ?',
'The finite-coefficient comparison starts with derived realization T(A). The later question asks whether it may be replaced by the ordinary realized Néron object in an Ext¹ formula.',
'This replacement needs a truncation/acyclicity statement; no proof of that simplification appears.','agrees','The last arrow is explicitly questioned and differs from the earlier derived expression.')
add(19,19,'withdrawn in the same text',[113],'842–882','page entièrement barrée',
'In the cancelled draft, the closed normal subgroup generated by decomposition groups cuts out the maximal extension in which the selected places split completely; the analogous inertia subgroup cuts out the corresponding unramified extension.',
'These are standard Galois-theoretic reconstructions of the intended maps, whose choice of prolongations must be kept up to conjugacy. Cancellation prevents presenting the draft as an endorsed theorem of the folder.','agrees','The whole page is cancelled, although its normal-closure mechanism remains mathematically interpretable.','withdrawn')
add(20,20,'idea of the earlier run',[112,133],'786–822;1568–1586','(n,p)=1',
'The earlier run proposes using the prime-to-p and characteristic-p coefficient rows to test external FLAGGED_149 B9 and Z142g cover-tower assertions, keeping pullback, trace and F,V maps explicit.',
'The named tower, compatible point differences and external targets are absent; no status upgrade is justified. The coefficient rows are source evidence, while the comparison is the earlier run’s lead.','agrees','The note accurately limits its claim to a finite-coefficient comparison target. The unavailable arithmetic tower is explicitly unverified.')
add(21,21,'idea of the earlier run',[117,133],'1028–1040;1577;1601–1604','π₀(A) et π₀(B) duaux; Hom(T(J),Q/Z)',
'The earlier run proposes supplying a specified Galois-subgroup action on the Jacobian realization and a map from a normalizer or centralizer to the displayed character target.',
'The component and character pairings are on the pages; the action, invariants and normalizer-to-module map are not. WG H1, FLAGGED_149 F8a and LM6 A.50 remain unverified external targets.','agrees','The note explicitly presents a map-level comparison task and does not claim the normalizer theorem is on these pages.')

add(24,24,'self-flagged step',[94,95],'2–55','Il faudrait prouver; Il faudrait aussi',
'For the proposed finite-surjective Weil-type site, establish cohomology/Ext comparison with quasi-algebraic groups and descent from a perfect field to its algebraic closure.',
'The site’s objects, sheaf conventions and continuity are not fully specified. Modern rational/ind-rational sites realize a related programme under explicit restrictions.','agrees','The two pages distinguish proposed comparison from assertions already made.')
add(25,25,'unproved claim',[94],'27–30','k algébriquement clos ... H^i(k,F)=0',
'For an algebraically closed residue field, the author asserts acyclicity of the final object and compatibility of internal Ext with base extension in the proposed site.',
'Algebraic closedness alone does not make global sections exact in every topology; the stated finite-surjective covers and coefficient category must make this precise.','agrees','The vanishing and base-change assertions are stated but not proved.')
add(26,[26,88],'withdrawn in the same text',[96,97],'91–99','Non, car V ... ne commute pas aux limites inductives',
'The proposed Néron realization is initially said to commute with filtered direct limits, and that assertion is explicitly withdrawn because the valuation/Witt-vector construction does not commute with them.',
'This is a retraction in the same manuscript. A finite-level or completed limit construction may still work, but is a new statement.','agrees','Both the initial crossed-out claim and its immediate counter-observation were read; the duplicate register entry88 adds no independent assertion.','withdrawn')
add(27,27,'self-flagged step',[97],'101–126','N transforme les injectifs ... à vérifier',
'From left-exact N and Γ_S=Γ_k∘N, the proposed Leray spectral sequence needs N to send injectives to Γ_k-acyclic objects; preservation of injectives is a stronger sufficient condition.',
'The adjunction proof is cancelled. The spectral sequence is conditional on the acyclicity condition, not supplied merely by left exactness.','agrees','The text marks the exact hypothesis à vérifier and strikes its attempted proof.')
add(28,28,'self-flagged step',[98],'130–148','Il faudra ... vérifier',
'The first relative-Hom spectral sequence requires acyclicity of the functor that takes Hom from the selected coefficient object after Néron realization.',
'The uncertain F/G subscript must be resolved before a precise derived functor identity is fixed. We retain the conditional Grothendieck-spectral-sequence criterion.','agrees','The first gate is independently marked and is not discharged by the preceding Leray discussion.')
add(29,29,'self-flagged step',[98],'150–171','Il faut ... vérifier',
'A second comparison interchanges Néron realization and internal Hom/Ext; it requires its own acyclicity or derived adjunction theorem. H^i=Ext^i(Z,−) is the formal special case.',
'The formal Ext description of cohomology is separated from the unproved comparison of two functors.','agrees','The second vérifier concerns a different composite and cannot be merged with the first without losing a hypothesis.')
add(30,30,'self-flagged step',[104],'395–436','parfait ?; (i); (ii); (iii)',
'The realization programme asks for acyclicity, cohomological dimension ≤2 (≤1 after excluding Z-components), and residue-field base-change compatibility.',
'The coefficient class and perfectness of K versus residue k are not settled in the page. In characteristic p, perfecting K kills flat μ_p/α_p cohomology, so it cannot be done invisibly.','agrees','All three requirements and the perfection question remain explicit.')
add(31,31,'unproved claim',[100,130],'173–235;1472–1512','sans composantes G_a; sans composantes abéliennes',
'The local duality sketch excludes additive constituents; the curve duality statement uses a different affine/no-abelian-constituent restriction and a degree-two shift.',
'These restrictions should not be conflated. Their exact extension from finite to general affine coefficients depends on category and support conditions.','agrees','The two pages write different exclusions and shifts, with uncertain exponents in the local display.')
add(32,32,'self-flagged step',[106],'490–545','Comment obtient on le carré du bas ?',
'The desired square compares Cartier, Serre and Pontryagin duality after Greenberg–Néron realization and finite-field points, with a degree shift in Ext.',
'Finite-field Lang theory and derived Galois descent can explain the shift; a commutative square for the author’s unspecified N is still a comparison task.','agrees','The lower square is a question, not an established compatibility.')
add(33,33,'reading question',[107],'547–589','H^i(A) × H^{2−i}(B); H^i(Z/n) × H^{1−i}(μ_n)',
'The page writes pairings with complementary degrees two and one. Ordinary local-field cohomology and geometrized residue-field duality have different total shifts.',
'A degree cannot be corrected solely to make the rows agree: first identify whether cohomology over finite residue k has already been taken.','agrees','The competing indices occur in different fragments; the excerpt supplies no complete comparison resolving them.')
add(34,34,'reading question',[114],'884–943','H^{1−i}; H^i; i+1',
'The scratch duality and spectral-sequence formulas contain incompatible or uncertain total degrees, including 1−i and a questioned i+1.',
'The proposed repair is a derived-degree audit with source/target and shifts declared. No transcription is altered.','agrees','The cancellations and multiple exponents were preserved; they do not determine a unique theorem.')
add(35,35,'reading question',[117],'1045–1067','produit direct; suite exacte',
'An upper display suggests a product decomposition of a cohomology/dual object, whereas the lower display establishes at most an extension by a finite component-group term.',
'A canonical splitting would require additional data or proof. The rank 2a+t of a semiabelian prime-to-p Tate module is separate from the splitting question.','agrees','The extension and product are not interchangeable and the page supplies no splitting argument.')
add(36,36,'self-flagged step',[123],'1281–1329','Ext^i_m(M,A) ?= D(M)',
'The author seeks a local-duality statement exchanging cohomology supported at a closed subset with completion along that subset, including Ext on a local ring.',
'Precise versions require noetherian hypotheses, a dualizing complex or a regular/Gorenstein normalization, and explicit support conventions. D(M) is not defined sufficiently here to identify one exact theorem.','agrees','The correspondence is posed with question marks and incomplete arrows.')
add(37,37,'self-flagged step',[125],'1340–1373','lim Ext^i(F/J^nF,G)',
'Ext with support is written as a filtered colimit over thickenings, and duality suggests inverse limits/completion on the other side.',
'The colimit formula needs a coherent first argument or another finiteness condition; moving a Hom functor through filtered colimits for an arbitrary module is false. Derived completion can also contribute higher inverse limits.','agrees','The finite-thickening formula is present; the final completion comparison is unfinished.')
add(38,38,'idea of the earlier run',[123,125],'1287–1311;1342–1371','[no DVR calculation on these pages]',
'The earlier run tests local duality over A=k[[t]]: Ext¹_A(A/t^n,A)=A/t^n, transition multiplication by t; the direct limit is K/A and End_A(K/A)=A.',
'This explicit model is an independent calculation, not text supplied by Grothendieck. It illustrates how a direct limit on torsion produces completion under duality.','not on the page','The finite resolutions and inverse-limit compatibility are re-proved in the worker computations.','corrected')
add(39,39,'self-flagged step',[128],'1392–1424','nous admettrons ... dimension cohomologique finie',
'For a complete nonsingular curve C/k the page introduces fppf commutative-group sheaves, a left-exact direct image, injectives, and assumes a finite cohomological bound.',
'A finite bound must specify torsion/constructibility and the relative site; fppf cohomology of every sheaf and every base change is not bounded solely by dim C=1.','agrees','The finite bound is expressly admitted, not established; the definition-equivalence question also remains.')
add(40,40,'self-flagged step',[130],'1474–1500','γ : Rf_*Sσ → σ',
'The trace map γ is intended to convert evaluation on C into a duality morphism E(G,Sσ)→E(Rf_*G,σ).',
'Composition is formal once derived evaluation, projection formula and trace are defined. Existence and perfectness of the trace in the chosen fppf/geometric category are substantive.','agrees','The diagram constructs the desired map conditionally and does not prove it is an isomorphism.')
add(41,41,'self-flagged step',[130,132],'1502–1512;1541–1563','préciser; type fini modulo θ',
'The asserted curve duality range includes finite coefficients and certain affine groups, with a degree-two dualizing coefficient Sσ=(DΔσ)(2). The meaning of finite type modulo θ is unfinished.',
'Modern finite-flat curve duality supplies a precise subcase. The θ-qualified extension is not identifiable without a definition absent from the package.','agrees','The page requests precision and leaves clause c) unfinished.')
add(42,42,'reading question',[100,132],'181–188;1541–1544','Sσ=(DΔσ_K)(1); Sσ=(DΔσ)(2)',
'The local and curve constructions use degree-one and degree-two shifts. These are compatible with distinct relative dimensions, provided a single convention is declared.',
'Whether parentheses denote cohomological shifts here must be checked against the surrounding E notation; they must not be read automatically as Tate twists.','agrees','The difference in the displayed integers is explicit and meaningful; unresolved local superscripts remain alarms.')
add(43,43,'reading question',[133],'1590–1597','Rf_*G_m(−1); Rf_*G_m(+1)',
'Adjacent formulas use opposite shifts for the same prospective Ext representation of curve cohomology.',
'Only one may fit a fixed cohomological convention. Comparing H⁰(C,Q/Z) and H¹(C,Q/Z) detects the degree error but does not decide the ink.','agrees','The sign conflict is genuinely in the transcription and is placed in readings.tsv.')
add(44,44,'self-flagged step',[135],'1621–1634','hensélisé',
'The point-supported Ext comparison is expected to depend only on a henselized local neighborhood, with codimension-one shift two for prime-to-p torsion.',
'A strict henselization is needed when removing residue-field Galois cohomology. Wild flat coefficients require a different dualizing object.','agrees','The page names the henselian reduction but does not prove the needed comparison.')
add(45,45,'withdrawn in the same text',[135],'1665–1674','n quelconque [barré]; premier à p',
'The promised easy μ_n calculation is narrowed by the author from arbitrary n to n prime to the residue characteristic.',
'The discarded arbitrary-n statement cannot be cited as proved. Flat Kummer exactness remains valid for all n, but étale purity and the easy calculation do not follow for p-torsion.','agrees','The cancellation and replacement are both explicit.','withdrawn')
add(46,46,'self-flagged step',[135,136],'1636–1669;1676–1749','F_U; H^m_U(F)=H^{m+1}_{x|X}(F_U)',
'The extension-by-zero short exact sequence and localization triangle are paired with a proposed local duality triangle. The margin gives a one-degree shift between open cohomology and boundary support in its acyclic ambient case.',
'Exactness of j_! is standard for open immersions of étale topoi. A stalk/strict-local vanishing hypothesis is required for the displayed shifted isomorphism.','agrees','The page’s shifted identity is retained; it prevents using the later unshifted box as a general theorem.')
add(47,47,'reading question',[138],'1775–1796','3−i; 2−i; isomorphisme ?',
'The five-term local-duality diagram has corrected complementary indices and ends with a questioned vertical isomorphism.',
'This is a compatibility proof still to be supplied. A diagram with matching dimensions alone does not prove the morphisms commute or are isomorphisms.','agrees','The late isomorphism remains explicitly questioned.')
add(48,[48,49],'self-flagged step',[140,136],'1840–1847;1733–1739','H^*_{Y/k}(i_!G) ?= H^*_{U/k}(G) ???',
'The boxed unshifted comparison of boundary-supported cohomology of extension by zero with cohomology on the open is doubtful. In the ordinary étale interpretation X=P¹ over an algebraically closed field, U=A¹, Y={∞}, G=Z/ℓ with ℓ invertible, the degree-zero left side is zero and the right side is Z/ℓ.',
'This counterexample refutes that ordinary unshifted interpretation; it does not identify an exotic relative cohomology notation whose definition is missing. The shifted localization triangle is the safe replacement.','agrees','The earlier run’s counterexample checks the actual question rather than correcting its ink. Entry49 is merged as the independent test of the same box.')

add(50,[50,51],'idea of the earlier run',[94,96,100,106,114,130,133,136,138,140],'2–43;57–95;173–235;490–545;884–943;1472–1512;1564–1613;1676–1750;1775–1796;1809–1850','[no Fourier kernel or unit-fibre assertion here]',
'No second Fourier-transform witness occurs in this Pro43 range. Cote47 scans3–8 construct a kernel transform and leave unit-fibre/inversion compatibility for later; it remains a separate object and task.',
'The absence claim is based on reading all 46 faces. The companion target was read directly (aggregate companion lines2086–2418); analogy between duality diagrams does not prove the Fourier compatibility.','agrees','Entries50–51 concern the same scope warning and preservation of the distinct cote47 test.')
add(52,52,'title, date or page count',[118],'1070–1136','Septembre 1963',
'The date appears in a cancelled administrative/EGA outline and cannot date all neighboring duality pages. The companion cycle letter bears 12 August 1964.',
'Chronological reconstruction must follow document units, reused paper and explicit dated passages; physical adjacency is insufficient.','agrees','The administrative page and the dated cote44 letter were both read.')
add(53,53,'idea of the earlier run',[128,132,133],'1392–1424;1524–1613','C courbe complète non singulière',
'The curve Jacobian calculations supply no higher-dimensional cycle-kernel characterization for the P^i programme of cote44.',
'The cote44 target (scans2,8–9) concerns incidence/Picard cycle quotients, and modern universal regular representatives are not automatically the same object.','agrees','The positive curve endpoint is kept while the unsupported extension to the cycle programme is excluded.')
add(54,54,'idea of the earlier run',[133],'1568–1586','{}_nJ; autodualité de la Jacobienne',
'The finite torsion table for a fixed curve does not supply a uniform bound on dimensions of intermediate cycle Jacobians. Cote44 asks for such a bound separately.',
'Saito’s Picard-homomorphism Betti bound is a precise later comparison for the companion programme; it is not written in these curve sheets.','agrees','Both the curve table and the companion boundedness programme were read; their quantifiers differ.')
add(55,55,'unpursued implication',[128,132,133],'1392–1424;1524–1613','Pic; J; autodualité',
'The usual curve Jacobian is a genuine endpoint of the higher-dimensional Picard/Albanese cycle programme: degree-zero divisors are represented by Pic⁰(C), and duality supplies its abelian counterpart.',
'This endpoint does not identify every higher-codimension incidence quotient or universal regular representative.','agrees','The source supports the dimension-one example, and the companion c44 programme states its higher-dimensional ambition separately.')
add(56,56,'unpursued implication',[133],'1584–1586','autodualité de la Jacobienne',
'Jacobian autoduality underlies the finite coefficient pairings here. The general positive correspondence and complementary cycle duality sought in cote44 need additional input.',
'A canonical principal polarization of a curve Jacobian is not proof of a positive cycle correspondence in arbitrary dimension.','agrees','The text invokes the curve result only.')
add(57,57,'idea of the earlier run',[107,117,142],'547–589;1026–1069;1866–1871','[no height pairing on these leaves]',
'The local/finite duality displays and Tate–Cassels cover do not construct the Néron–Tate/intersection pairing proposed in cote44 scan4 Theorem5; its later correspondence discussion occurs on scans8–9.',
'The companion letter’s height question is a distinct research line; its existence or positivity must be checked in its own literature.','agrees','No height construction occurs in the 46 read faces, and the companion height passage was read.')
add(58,58,'idea of the earlier run',[118,133],'1070–1136;1564–1613','Sections hyperplanes, multisections',
'The cancelled EGA outline and the curve table do not prove a Lefschetz hyperplane theorem for cycle-parameter Jacobians.',
'The external hyperplane comparison remains a lead; a contents-list mention is not a mathematical argument.','agrees','The only nearby outline wording belongs to a cancelled programme.')
add(59,59,'reading question',[100,106,130,132],'173–235;490–545;1472–1512;1541–1563','σ; τ; θ',
'Coefficient symbols and an undefined θ-qualification in these duality pages must not be identified with the τ-equivalence relation on cycles in cote44.',
'Similarity of letters supplies no mathematical identification. The source has separate categories, objects and purposes.','agrees','The companion cycle-equivalence passage and these coefficient formulas were read independently.')
add(60,[60,68,70],'unpursued implication',[133],'1584–1586','autodualité de la Jacobienne; V,F|p [reading uncertain]',
'For an isogeny λ:A→B, Cartier duality identifies ker(λ∨) with D(ker λ). Applied to n and to a polarization, it gives the finite-level pairings behind the Jacobian table, with Oda’s stated bidual sign convention.',
'The full functorial statement is supplied by Oda Cor1.3 (1969, pp69–70), not proved in this manuscript. Skew symmetry follows for a symmetric λ; ampleness and positivity are extra conditions.','agrees','The page’s finite duality is consistent with the checked isogeny theorem; the earlier run correctly separates pairings from positivity.')
add(61,61,'unpursued implication',[133],'1584–1586','autodualité de la Jacobienne; V,F|p [reading uncertain]',
'For a map f:G→H of finite commutative group schemes, D(coker f)=ker D(f); under a perfect Cartier pairing, the annihilator of im f is ker D(f). Frobenius and Verschiebung are adjoint between the appropriate Frobenius twists.',
'A statement about annihilators of kernels instead uses images of the dual maps. Suppressing the Frobenius twist can turn a correct identity into an ill-typed one.','agrees','The schematic source phrase is retained; exact kernels/images and twists are the reconstruction to be checked in Oda’s conventions.')
add(62,62,'unpursued implication',[133],'1584–1586','autodualité de la Jacobienne; V,F|p [reading uncertain]',
'Over a perfect field of characteristic p, the contravariant Dieudonné module of the Cartier dual finite p-group is canonically the dual module with F and V interchanged by Frobenius-semilinear transposition.',
'This is Oda Thm3.19, not an additional statement written in Pro43. Its relevance is the realization of the finite dualities already on the page.','agrees','The literature interpretation is exact after specifying Oda’s Def3.5 and Prop3.13 conventions.')
add(63,63,'unpursued implication',[133],'1580–1586','H¹(O)^F; J_p',
'For an abelian variety A over a perfect field of characteristic p, Oda Cor5.11 identifies M(A[p]) with H¹_dR(A), and VM=ker F with H⁰(A,Ω¹). This answers the filtered finite-group reconstruction question in companion cote54 scan7.',
'The de Rham theorem is later literature; Pro43 itself has only the finite coefficient/Frobenius table. No identity of arbitrary restricted-Lie p-operations follows merely from the vector-space filtration.','agrees','Both the Pro43 table and c54 question were read; the claimed bridge is explicitly later work.')
add(64,64,'unpursued implication',[133],'1580–1586','J; H¹(O)',
'Oda Cor5.2 proves degeneration of the Hodge-to-de-Rham spectral sequence for a smooth proper curve; its proof uses the Abel–Jacobi pullback isomorphism on H¹(O). For a smooth proper pointed X over perfect characteristic-p k, Cor5.12 gives a Picard-to-de-Rham injection with specified image, not automatically an isomorphism.',
'These are later comparison theorems and their hypotheses must remain distinct. Existence of a rational base point is part of Oda’s formulation.','agrees','The earlier run’s endpoint comparison is valid after distinguishing the curve isomorphism from the general injection.')
add(65,65,'idea of the earlier run',[133],'1584–1586','V,F|p [reading uncertain]',
'A useful audit is to transport the page’s Frobenius/Verschiebung pairing through Oda’s module functor, keeping σ-linear F and σ⁻¹-linear V and the twist M(G^(p))=(W,σ)⊗M(G).',
'This is a proposed checking task; it is not an additional Grothendieck conjecture. The semilinear adjunction is established in Oda Def3.5 and Prop3.13.','agrees','The task is well posed only with the exact dual convention, now checked in the primary source.')
add(66,66,'unproved claim',[133],'1586','le plus gd sous-groupe … isomorphe à un α_p^n … dual au … plus gd quotient [wording uncertain]',
'Cartier duality exchanges the maximal subgroup of α_p type with the maximal quotient of α_p type of the dual finite p-group; after Jacobian self-duality this yields a duality between their tangent spaces.',
'The maximal α_p^r object and its quotient are finite group schemes, not the entire p-torsion. Identification with a-numbers uses the Dieudonné realization.','agrees','The page states exactly this finite subquotient comparison, without deriving it.')
add(67,67,'reading question',[112,133],'803–822;1572–1575','μ_p; Z/p; α_p',
'The three characteristic-p rows record different group schemes: multiplicative, étale, and local additive. They yield different kernels/cokernels of n, F−1 and F.',
'Neither passing to geometric points nor identifying all kernels of Frobenius preserves the finite-flat information.','agrees','The rows are separate in both local and curve tables; combining them would erase the issue driving c54.')
add(69,69,'unpursued implication',[133],'1584–1586','autodualité de la Jacobienne',
'For a line bundle L on an abelian scheme, Oda’s Prop1.15 proves that the pairing derived from the dual-isogeny construction ρ(L)=ν∘Λ(L)(p) equals Mumford’s e(L).',
'This checked compatibility belongs to finite/p-divisible duality. It does not discharge the unrelated unit-fibre θ compatibility left open in cote47 Fourier notes.','agrees','The literature result and the companion open Fourier task have different maps and domains.')

add(71,71,'conjecture',[101],'268–294','It would seem reasonable to suppose that the maps Df and Δ are of the same S-homotopy type.',
'The reused Atiyah typescript conjecturally identifies the Spanier–Whitehead dual of James’s intrinsic-join map with the diagonal-induced Thom map, after declaring γ=−α−τ and δ=−β−τ.',
'This is Atiyah’s copied/reused text, not attributable as a conjecture of Grothendieck. Its exact stable range and identification with later results must be checked in the published Thom Complexes paper.','agrees','The text is a continuous reused typescript with its own bibliography and distinct authorial voice.','corrected')
add(72,72,'reading question',[101,103],'252–298;343–394','2r ≥ dn−2; r=d(n−k+1)−2',
'Substituting the displayed r gives the stable-range inequality n≥2(k−1)+2/d. In the real case d=1 this is n≥2k. The sphere exponent in Lemma6.3 must match real dimension dn.',
'The algebraic simplification is independently checked; the uncertain printed exponent 3n−1 versus dn−1 is left for the image.','agrees','The stable range follows exactly from the written inequality, while the sphere dimension is a mathematical reading alarm.')
add(73,73,'title, date or page count',[101,103,105],'237–394;438–489','Thom Complexes; References',
'The reused leaves form the end of Atiyah’s Thom Complexes, published in Proceedings of the London Mathematical Society (3)11 (1961), pp291–310; source order103→101 follows typed pages21→22.',
'Document identification is distinct from authorship of the manuscript annotations and from dating neighboring sheets.','agrees','Internal page order and bibliography give a strong identification; the published source is checked separately.')
add(74,74,'withdrawn in the same text',[108],'591–655','[brouillon barré]',
'The cancelled draft studies variation in numbers of geometric connected/irreducible components under properness, openness and separability hypotheses.',
'Some fragments suggest continuity while others only semicontinuity. The exact functor and hypotheses are not stable enough to extract a single global theorem from the cancelled page.','agrees','Cancellation, competing component notions and incomplete conditions prevent promoting this to a finished result.','withdrawn')
add(75,75,'self-flagged step',[110],'719–785','Proposition6.7; Lemme6.8; J’ignore',
'The draft proposes upper semicontinuity of total geometric multiplicity and a DVR length criterion for flatness, under properness/universal openness and a condition S₁ on the special fibre.',
'Total multiplicity, the generic-point summation and module support hypotheses require exact specification. The proof’s equality case is separated from the false literal inequality criterion in SA19-76.','agrees','The proposition and local lemma are genuine mathematical content on reused paper, with explicit margin doubts.')
add(76,76,'reading question',[110],'747–769','Si l’inégalité est vérifiée, alors F est plat',
'The literal assertion is false: take R=k[[t]], X=Y=Spec R, f=id and F=R⊕R/(t). The special length is2 and generic length1, so the inequality holds; F has nonzero t-torsion and is not flat. Both fibres are zero-dimensional S₁, f is proper and universally open, and the support is all X.',
'The following proof instead uses equality to force N/tN=0 for the t-torsion submodule N. This suggests égalité as a reading alternative, not an authorized correction of ink.','agrees','Every stated hypothesis relevant to the displayed example was checked; the mathematical failure is substantive.')
add(77,77,'unproved claim',[115],'944–979','R^p f_*(g_*O(n)) = R^p(fg)_*O(n)',
'For proper f between noetherian schemes, the proof uses a projective Chow modification g and Serre vanishing for sufficiently large n to collapse Leray and prove coherence of higher direct images.',
'The exact finite-type/noetherian setup is partly on preceding reused pages. In its standard formulation this is the proper direct-image coherence theorem of EGAIII3.2.1.','agrees','The displayed equality is the Leray-collapse step, not a freestanding assertion for arbitrary n.')
add(78,78,'self-flagged step',[116],'1019–1024','[question barrée] Cohen–Macaulay; équidimensionnel',
'A cancelled marginal question asks whether equidimensionality/Cohen–Macaulay hypotheses can be weakened in a result referred to only as1.1(ii) or2.6.',
'The cited statements are absent. No exact weakening can be identified or classified as solved from the surviving fragment.','agrees','The references and hypotheses cannot be reconstructed uniquely; the cancelled status is retained.')
add(79,79,'title, date or page count',[118],'1070–1136','Septembre 1963; [plan barré]',
'The cancelled outline lists EGA topics and contains an administrative date. It records an agenda, not proofs of the listed theorems and not a date for the whole duality dossier.',
'Only explicit documentary facts are retained; root’s broader chronology may add independently dated units.','agrees','All outline entries were read, including the cancelled status and separate date.')
add(80,80,'unproved claim',[121],'1234–1272','caractéristique d’Euler; polynôme',
'For bounded complexes of finite-length modules, alternating total length is additive and equals alternating cohomology length. For a coherent sheaf on a projective scheme over an artinian base, the Euler characteristic of its twists is a polynomial for all integers and agrees with the length of global sections for sufficiently large twists; its leading coefficient is positive when the sheaf is nonzero.',
'Positivity does not mean every coefficient is positive. The zero sheaf gives the zero polynomial; strict inequalities require the nonzero hypothesis.','agrees','The proof of Euler additivity is present; the Hilbert-polynomial context is partially carried over from reused paper.')
add(81,81,'reading question',[129],'1425–1471','dim; prof; propriété(P)',
'For a localization of a polynomial algebra over a noetherian local ring, the dimension/depth formulas add the regular-fibre dimension. The cancelled draft then asks transfer of a property(P) whose definition is not supplied.',
'The variable-count ambiguity and the missing property prevent reading a unique preservation theorem. The regular-fibre dimension/depth formulas are stated separately with hypotheses.','agrees','The formula fragments can be interpreted, but the final property(P) cannot.')
add(82,82,'unproved claim',[137],'1751–1774','fidèlement plat; B/h(A)',
'For a flat ring map A→B, faithfulness is equivalent to nonvanishing after tensoring every nonzero A-module, to surjectivity Spec B→Spec A, and to proper extension of every maximal ideal; faithful flatness gives contraction IB∩A=I and injective tensor-unit maps.',
'The displayed B h(A) must be compared to the quotient B/h(A) used in the following proof; this is a likely slash omission. Flatness is indispensable in the equivalence package.','agrees','The proof and the surrounding equivalent conditions were read rather than inferred from the heading.')
add(83,83,'unproved claim',[124,126],'1330–1339;1374–1391','faisceau mou; partition de l’unité',
'On a paracompact Hausdorff space, softness of a suitable sheaf of rings supports partitions of unity subordinate to locally finite covers; the local softness condition requires extension from closed sets and is not satisfied by every constant sheaf.',
'The proof is partial and uses a maximal-family extension. The exact support and paracompactness assumptions must remain explicit.','agrees','Both the partition argument and the local definition/counterexample context were read.')
add(84,[84,85],'unproved claim',[139,141],'1797–1808;1851–1864','F → F⊗I',
'The reused sheaf-theory text embeds any sheaf of abelian groups F into F⊗I, where I is the sheaf of arbitrary integer-valued functions, and uses I-module structure to obtain a fine sheaf. At each stalk evaluation at the base point splits Z→I_x, so the tensor-unit map is injective.',
'The stalkwise retraction is the earlier run’s alternative proof; it does not furnish one global evaluation map. Open/closed extension statements require their own standard sheaf-theoretic hypotheses.','agrees','The embedding is written; the stronger global splitting is not. The two entries are merged as statement and proof audit.')
add(86,86,'other',[],'notes metadata section only','[no single manuscript passage]',
'The context-key inventory records names of external working registers and research runs used by the earlier notes.',
'Those documents are not attached; their claims and identifiers are preserved only as unverified project provenance. They do not become claims of Grothendieck.','not on the page','This entry is metadata for the earlier run, not an additional theorem.','corrected')
add(87,87,'other',[94,95,96,97,98,100,102,104,106,107,109,110,112,114,116,117,119,120,123,125,128,130,132,133,135,136,138,140],'2–1850, individual loci in claims/problems','à vérifier; ?; Il faudrait',
'The SF01–SF41 register indexes self-flagged steps already occurring in the mathematical entries and also preserves individual margin flags not separately titled.',
'It is a finding aid, not41 independent theorems. Every referenced fragment was read and is represented by the problem/claim map or an explicit not-identifiable record.','agrees','The full41-row register was read, including its corrected degree and hypothesis warnings; its duplicates are merged through the claims map.')
add(89,89,'title, date or page count',[s for s in range(94,143) if s not in (99,111,127)],'1–1871','Corps de classes et dualité des Courbes Algébriques; Dualité de Tate–Cassels',
'The package contains46 scanned faces: scans94–142 excluding99,111,127. There are27 mathematical faces,11 reused typescript faces,4 cancelled drafts and4 covers. Archive page numerals are one less than scan labels; additional reused typescript page numbers belong to their own series.',
'The scan list contains exactly the46 present faces. Reused page order is103→101 and141→139. These counts do not date mathematical units.',
'agrees','All46 scan markers and all1871 aggregate lines were read; the source-title/result index was checked against those faces.')

def finish():
    # Final rereading confirmed these entries already label their own ideas,
    # documentary metadata or reused author correctly. Do not invent an error
    # merely because they are not new claims of Grothendieck.
    retained={2:'Kept as the earlier run’s explicitly limited comparison task; it already states that the1983 arithmetic-section proof is unavailable.',
              3:'Kept as the earlier run’s own arithmetic model, correctly distinguished from the manuscript and independently re-proved here.',
              38:'Kept as the earlier run’s own DVR model; its attribution and transition maps agree and were independently re-proved.',
              71:'Kept: the note already identifies the reused typed author through Atiyah/R03 and correctly retains the conjectural comparison.',
              86:'Kept as context-key metadata, exactly as presented by the source entry; it is not counted as a mathematical claim.'}
    for r in rows:
        n=int(r['entry_id'].split('#')[1])
        if n in retained:r.update(verdict='kept',reason=retained[n])
    (BASE/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    with (BASE/'entries.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(sorted(rows,key=lambda r:int(r['entry_id'].split('#')[1])))
    print(f'{len(items)} individually adjudicated items; {len(rows)} source verdicts written')

if __name__=='__main__': finish()
