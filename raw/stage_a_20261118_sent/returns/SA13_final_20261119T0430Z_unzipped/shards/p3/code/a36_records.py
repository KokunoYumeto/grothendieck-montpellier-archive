"""Additional claims from the completely read Codex A36-01 and A36-02.

These source folders have no NOTES_INDEX verdict rows. Semantic records below
were written individually after reading the passages and their corrections.
"""
def ai(n,folder,kind,locs,words,statement,reconstruction='',check='agrees',reason=''):
    items.append(dict(id=f'SA13-{n}',sources=[f'codex/{folder}'],kind=kind,cote=[36],
      scans=[f'36:{s:03}' for s,a,b in locs],
      lines=[dict(file=f'codex/{folder}_transcription.tex',cote=36,scan=s,start=a,end=b) for s,a,b in locs],
      his_words=words,statement=statement,reconstruction=reconstruction,check=check,check_reason=reason or 'Directly read in the supplied Codex transcription; no indexed Pro verdict is created.'))

ai(343,'A36-01','unproved claim',[(10,5,16)],'Disons que x est primitive; la suite spectrale de Leray ... u(x)',
 'For a proper smooth morphism f:Y→S with connected regular S, ell invertible, and the stated constant twisted ell-adic coefficients, a class restricting to zero on one geometric fibre is primitive and has a canonical Leray class in H1(S,R^{m−1}f_*F).',
 'The canonical map is F1H^m→E_infinity^{1,m−1}→E2^{1,m−1}; no degeneration assertion is needed for this particular injection.')
ai(344,'A36-01','unproved claim',[(10,17,29),(11,33,37)],'u(Z(x′))=Z(u(x′))',
 'A cohomological correspondence of degreeN between smooth proper S-schemes of constant relative dimensions, with m=m′+N−2d′ and compatible Tate twists, preserves primitive classes and commutes with their Leray classes.')
ai(345,'A36-01','unproved claim',[(11,39,57),(12,61,73)],'si l’homomorphisme (*) est nul ... alors ... u(x) ... nul',
 'A difference of sections of a smooth proper geometrically connected relative curve gives a primitive divisor class. A relative correspondence whose H1 map vanishes at one geometric fibre annihilates the resulting Leray class.',
 'Existence of cycle classes and intersections requires the restrictions explicitly stated in the text; one-fibre vanishing uses lissity and connectedness.')
ai(346,'A36-01','self-flagged step',[(11,47,57)],'de codimension ... ≤ n fibre par fibre; les intersections ... ont un sens',
 'The author restricts the base and cycle geometry to make relative cycle classes and pullbacks well-defined; the transcribed fibrewise ≤n requires an ink check against the expected proper-intersection inequality.',
 'No alteration of the transcription is made. A Chow-theoretic formulation for smooth projective varieties over a field is a modern precise safe case.')
ai(347,'A36-01','conjecture',[(12,75,85)],'conjectures standart; lorsque X se remonte en car. zéro avec sa polarisation',
 'Assume an algebraic correspondence gives a partial right inverse to i*:H^{2n−1}(X)→H^{2n−1}(Y) on its image. For a hyperplane inclusion, algebraicity of the Lefschetz inverse implies this. The additional parenthesis claiming that lifting with a polarization to characteristic0 suffices is not a known consequence of hard Lefschetz.',
 'The last sentence would require algebraicity, not merely an isomorphism of cohomology groups. No counterexample to the standard conjecture is asserted.')
ai(348,'A36-01','conjecture',[(13,89,93)],'le plus grand morceau ... de niveau 1 ... est nul',
 'Conditionb says that every correspondence from a smooth proper connected curve has its H1 image contained in im(i*). Its interpretation as vanishing of a maximal level1 submotive is explicitly conditional on the motivic framework.')
ai(349,'A36-01','unproved claim',[(13,95,101)],'z=i*(z′)+z″; Démonstration immédiate',
 'Under conditionsa,b, an algebraically trivial rational codimension-n cycle onY decomposes into the pullback of an algebraically trivial rational cycle onX and a difference of fibres of a curve correspondence acting trivially onH1.',
 'The equality should be interpreted in a cycle theory where all pullbacks/compositions exist, for example rational Chow groups of smooth projective varieties; denominators are essential.')
ai(350,'A36-01','self-flagged step',[(13,103,106),(14,110,116)],'modulo une classe de torsion; restriction ... probablement inutile',
 'For a smooth proper family and a generically algebraically trivial cycle, conditionsa,b on the geometric generic fibre imply that its rational Leray class comes fromX after shrinking the regular connected base. The author conjectures that shrinking may be unnecessary.',
 'Trace/descent and spreading are part of the argument. The displayed sourceX_s→X_s and the space on which cycle equality holds are reading alarms.')
ai(351,'A36-01','unproved claim',[(14,118,122),(15,126,148)],'l’image inverse ... de Im i* est réduite à zéro',
 'The Griffiths map from primitive middle cohomology toH1 of a Lefschetz pencil is injective modulo the fixed part.',
 'The printed theorem requires the Lefschetz and pencil hypotheses specified in SGA7XVIII5.8.4; the manuscript’s “trivial calculations” are not reproduced there.')
ai(352,'A36-01','unproved claim',[(15,150,152)],'z est cohomologiquement équivalent à zéro (mod torsion)',
 'For X of even dimension2n and a Lefschetz pencil satisfyinga,b, any codimension-n cycle whose restriction to the geometric generic section is algebraically trivial has zero rational ell-adic cohomology class.')
ai(353,'A36-01','unproved claim',[(15,152,152),(16,157,157)],'contient comme sous-espace ... P_alg^{2n}(X)',
 'The rational Griffiths group of the generic section has dimension at least that of primitive algebraic middle cohomology ofX.',
 'The natural argument produces the latter space as a quotient of a subgroup of the Griffiths group. An abstract vector-space embedding can be chosen, but no canonical embedding is produced.')
ai(354,'A36-01','conjecture',[(16,159,162),(17,166,166),(18,173,178)],'il existe un entier d0; non, pas tout à fait !',
 'For fixed smooth projective even-dimensionalX, sufficiently general high-degree Lefschetz pencils should satisfy conditionb. The attempt in§7 is expressly qualified in the margin and must be kept separate from the conjecture itself.')
ai(355,'A36-01','unproved claim',[(16,162,162)],'module simple ... tout sous-groupe ... ouvert',
 'Under the pencil/Lefschetz hypotheses, odd-degree vanishing cohomology is absolutely irreducible, including after restriction to an open subgroup. The reason is that nontrivial transvections survive positive powers.')
ai(356,'A36-01','unproved claim',[(16,162,162)],'Cela prouve ... en caractéristique nulle',
 'In characteristic0 the growth of H^{2n−1}(Y,O_Y) for high-degree sections supplies Hodge types outside the two curve-level types, proving conditionb using the preceding irreducibility.',
 'E^{n−1} and “pour ces valeurs” conflict with the argument and remain scan-reading alarms.')
ai(357,'A36-01','self-flagged step',[(17,166,166)],'je ne sais pas ... que le niveau ... ne peut que diminuer par spécialisation',
 'The author uses specialization of curve/abelian-level realizations via good reduction but explicitly lacks a general specialization theorem for motivic level, even assuming standard conjectures.')
ai(358,'A36-01','conjecture',[(17,166,166)],'implique ... peut-être équivalent à ... divisibilité',
 'A curve-level realization of weight2n−1 over a finite field has Frobenius eigenvalues divisible byq^{n−1}. The converse is only queried. A unit eigenvalue rules out curve level whenn≥2.',
 'Integrality and a Tate twist prove necessity. The converse is a generalized Tate/coniveau question, not a formal consequence of the congruence formula.')
ai(359,'A36-01','withdrawn in the same text',[(18,173,182)],'un sous-espace V′_0 ... stable par u; pas prouvé sous cette forme forte',
 'Theorem7.1 originally asks for every residue to occur as a trace on the whole Frobenius-fixed representation of generic vanishing coherent cohomology. An insertion weakens it to a trace on an invariant subspace; the p-group and dimension consequences are deleted.',
 'The two statements are different. The strong statement is not refuted by the weak version, but its proof is expressly withdrawn.')
ai(360,'A36-01','self-flagged step',[(18,184,186)],'pas prouvé; ... équivalent à 7.1 sous sa forme forte',
 'Corollary7.2 predicts every residue modp among rational-point counts on sections parametrized by any dense open, after a finite base-field extension. Its margin explicitly says the proof needs the strong trace theorem.',
 'The statement continues on A36-02 scan19; the missing proof cannot be supplied by applying Chebotarev to a trace on a proper invariant subspace.')
ai(361,'A36-02','unproved claim',[(19,5,15),(20,19,27)],'la somme alternée des traces ... égal au nombre ... mod p',
 'Deligne’s coherent Frobenius trace congruence expresses the rational-point count of a proper scheme overFq modulo p as the alternating trace ofFq onH^i(O). In the family it yields the fixed contribution plus the trace on vanishing coherent cohomology.')
ai(362,'A36-02','unproved claim',[(19,15,15),(23,57,67)],'H^i(X,O_X(−d))=0 ... i<n; EGA III 7',
 'For a projective equidimensional Cohen–Macaulay scheme of dimensionn, negative-twist cohomology vanishes in degreesi<n for sufficiently larged. An effective Cartier section gives cohomology isomorphisms fori≤n−2 and injection fori=n−1; the stated family is locally free and commutes with base change on the proper-section open.')
ai(363,'A36-02','unproved claim',[(20,27,27),(24,73,78)],'toutes les valeurs propres ... égales à 0 ou 1',
 'After a finite extension of a finite field, each of finitely many coherent Frobenius eigenvalues becomes0 or1, so the alternating trace contribution fromX becomes constant.')
ai(364,'A36-02','unproved claim',[(20,30,34),(21,46,47)],'un pinceau ... ne soit pas de niveau1; variante ... Bertini',
 'A sufficiently general high-degree Lefschetz pencil should have vanishing cohomology with no curve-level part. The proposed proof uses the strong point-count assertion and a fundamental-group-surjective general line.',
 'The margin defines an open in the Grassmannian of lines; it is not an open of the hypersurface parameter space itself. The inherited strong-trace proof gap remains.')
ai(365,'A36-02','reading question',[(21,37,47)],'1+q^{2n−1−i|2n−2−i}',
 'The trace decomposition pairs low-degree ambient cohomology with its high-degree Lefschetz twist and adds ambient middle cohomology and vanishing cohomology.',
 'WithdimX=n,dimY=n−1, the factor expected from hard Lefschetz is1+q^{n−1−i}. The transcribed exponents are dimensionally inconsistent; ink must decide.')
ai(366,'A36-02','unpursued implication',[(22,50,53)],'niveau ... égal à n−1; sans aucune conjecture',
 'Remark7.4 strengthens the desired vanishing-cohomology conclusion to maximal level in every dimension, using spread-out correspondence coniveau and Frobenius divisibility. It also queries equality of correspondence and support filtrations.',
 'The claim that the preceding proof is unconditional does not repair the explicit gap in strong7.1/7.2. The local divisibility argument remains useful independently.')
ai(367,'A36-02','unproved claim',[(24,81,81),(26,109,111),(27,116,118)],'V′_0⊂V_0 stable; La démonstration ... l’âne qui trotte',
 'The manuscript asserts that, for a locally free module with p-linear endomorphism on a normal base, the special Frobenius-fixed representation appears inside that at any generization t after an open subgroup, with the same finite image. Lemma7.5 applies the proposed mechanism to a characteristic polynomial.',
 'The arbitrary-point assertion is false: C-SA13-355 gives the smooth-ambient nodal counterexample. C-SA13-363 proves the repaired statement when t is the generic point of a normal integral base. The final generic-point reduction does not preserve normality of an arbitrary specialization closure. The subspace insertion also differs from constancy of the whole representation.')
ai(368,'A36-02','unproved claim',[(24,83,89),(25,93,97)],'Pour tout entierN≥0 ... card(Y_s)=N',
 'For a projective positive-dimensional scheme over a finite field, every sufficiently large degree admits, after a finite field extension, a hypersurface section of the expected dimension with exactlyN rational points; singular sections are allowed.',
 'A direct high-degree homogeneous interpolation proof verifies the existence statement. It does not by itself certify the sharper numerical bound suggested in the manuscript.')
ai(369,'A36-02','reading question',[(24,85,89),(25,93,97)],'N≥rd_1^n; ... (H_phi psi∩X)(k)=Z(k)',
 'The construction first obtains a finite split complete intersectionZ of size r d1^n, then selectsN of its points. Its inequality must permitN≤r d1^n, and the final zero set isH_n∩Z, not allZ.',
 'The same-degree interpolation and the statedd1=1 special case need a separate geometric argument; they are not justified solely by the cardinal inequality.')
ai(370,'A36-02','unproved claim',[(25,93,97),(26,107,107)],'formes normiques ... décomposables géométriquement en facteurs linéaires',
 'For everyd≥n+1 there is a homogeneous degree-d form inn+1 variables overFq with no nontrivialFq-zero, obtained by restricting the normF_(q^d)/Fq to ann+1-dimensional subspace. It splits into linear factors over an algebraic closure.')
ai(371,'A36-02','self-flagged step',[(23,69,69)],'se réduire au cas oùk est fini ... n’offre pas de difficultés',
 'The proof asserts that the generic trace assertion can be reduced to a finite base field by spreading and specialization. It provides no detailed compatibility argument for stable Frobenius parts or finite-image Galois representations.')
ai(372,'A36-02','unpursued implication',[(25,99,99),(26,103,105)],'au moins deux traces distinctes; meilleure majoration',
 'Remark7.7 proposes two whole-space traces as sufficient for the geometric application, and suggests improving degree bounds by disjoint unions and coprime degrees.',
 'Two traces on invariant subspaces are insufficient. The coprime-degree arithmetic is elementary, but geometric disjointness and the selection inequality must still be supplied.')
ai(373,'A36-02','title, date or page count',[(27,120,122)],'Relations heuristiques ... J’ai donné notes à Berthelot',
 'The last sheet announces a new heuristic comparison of crystalline, quasi-/topo-crystalline and vanishing cohomology, and records giving notes to Berthelot. No theorem or argument follows.',
 'Together A36-01/02 give manuscript pages1–18 on scans010–027, with no explicit date or total-page assertion. This is a heading and transfer note, not a crystalline comparison theorem.')

# claim helper uses the old item-number offset; these are exact ids, not classifications.
def ac(n,ids,statement,status,klass,fate,refs,search,**kw):
    return claim(n,[i-249 for i in ids],statement,status,klass,fate,refs,search,**kw)

ac(325,[343],
 'For proper smoothf:Y→S with connected regularS,ell invertible and the constant twistedell-adic coefficients in the manuscript, the kernel ofH^m(Y,F)→H0(S,R^mf_*F) consists of classes vanishing on one geometric fibre. It maps canonically toH1(S,R^{m−1}f_*F).',
 'stated without proof','B',
 'Exact published formalism in KatzSGA7IIXX1.1,1973, whose introduction credits Grothendieck’s algebraic argument. The elementary filtration construction is independently checked; no Leray degeneration is assumed.',
 ['SGA7XX'],['P3-A01'],computation='review.md §A36 Leray construction: first-quadrant filtration argument.')
ac(326,[344],
 'With the relative dimensions, degree shiftm=m′+N−2d′ and pairingF′⊗G→F(d′) written on the page, a smooth-proper cohomological correspondence preserves the Leray filtration and commutes with the primitive classu.',
 'stated without proof','B',
 'KatzSGA7IIXX1.3–1.4 explicitly constructs the morphism of Leray spectral sequences and proves this compatibility. The1973 publication is a direct match, not merely a later similar construction.',
 ['SGA7XX'],['P3-A01'])
ac(327,[345],
 'For a smooth proper geometrically connected relative curveC/S and two sections, the divisor-class difference is primitive. If a relative correspondenceC→Y induces zeroH1 map on one geometric fibre of connectedS, it givesu(cl(Z(t1)−Z(t0)))=0.',
 'proof sketched','B',
 'Exact comparison in SGA7IIXX1.5.3,1.6 and1.7. Lissity makes one-fibre zero imply the zero sheaf morphism; the relative degree of a difference of sections is zero.',
 ['SGA7XX'],['P3-A01'],computation='review.md §A36 Leray construction: degree and lisse-sheaf check.')
ac(328,[346],
 'Relative algebraic cycle classes and pullbacks in the displayed argument require defined cycle classes and proper intersections, or a cycle-class theory compatible with Chow pullback. The fibrewise inequality is not accepted literally until the scan is checked.',
 'open on the pages','C',
 'SGA7IIXX1.6 gives the published cycle-class assumptions. Modern intersection theory supplies a safe smooth-projective-over-a-field formulation, but the archive’s unspecified excellent-base alternatives and transcribed≤n are not silently generalized.',
 ['SGA7XX'],['P3-A01'],confidence='medium')
ac(329,[347],
 'An algebraic correspondence that retracts the image ofi*:H^{2n−1}(X,Q_l)→H^{2n−1}(Y,Q_l) is assumed. For a smooth hyperplane section the Lefschetz standard conjecture onX implies such an algebraic inverse.',
 'stated without proof','B',
 'KatzSGA7IIXX3.3–3.4 states the algebraic inverse condition(B) and its implication from algebraicity ofLambda, while explicitly retaining the latter as conjectural in general.',
 ['SGA7XX','Milne2022Standard'],['P3-A02'])
ac(330,[347],
 'The parenthetical assertion that a polarized lift to characteristic0 by itself proves algebraicity ofLambda is unsupported in general. Hard Lefschetz for the lift proves an isomorphism, while algebraicity of its inverse is the Lefschetz standard conjecture.',
 'stated without proof','C',
 'SGA7IIXX3.4 does not repeat the lift parenthesis and retains the standard conjecture. Milne2022 and Ancona–Cavicchi–Laterveer–Saccà2025 distinguish hard Lefschetz from algebraicity and prove only stated special cases. As of2026-11-19 no general lift-only theorem was found; this is an unproved assertion, not a known counterexample to the conjecture.',
 ['SGA7XX','Milne2022Standard','AnconaEtAl2025'],['P3-A02'],confidence='high')
ac(331,[348],
 'Conditionb is the cohomological statement that every algebraic correspondenceH1(C,Q_l(1))→H^{2n−1}(Y,Q_l(n)) has image inim(i*). Calling this absence of a maximal curve-level submotive requires a specified category and realization comparison.',
 'open on the pages','C',
 'KatzSGA7IIXX3.2 formulates the condition directly through the coniveau/correspondence filtration, avoiding unconditional existence of the manuscript’s motivic summand. The cohomological condition is precise; the stronger motivic interpretation remains conditional in this generality.',
 ['SGA7XX','SGA7XXI'],['P3-A02'])
ac(332,[349],
 'For smooth projectiveX,Y over an algebraically closed field, assuminga,b and working in rational Chow groups, every algebraically trivialcodimension-n classz onY is i*z′+z″ withz′ algebraically trivial andz″ a difference of fibres of a correspondence acting trivially onH1 of its curve.',
 'proved there','B',
 'The page gives the constructionZ′=vZ andZ″=Z−i*Z′. The corresponding decomposition is used explicitly in SGA7IIXX4.4. This run independently checks its two cohomological identities and denominator requirement.',
 ['SGA7XX'],['P3-A01'],computation='review.md §A36 decomposition: explicit correspondence calculation.')
ac(333,[350],
 'For a smooth proper family over a regular connected base, a cycle algebraically trivial on the geometric generic fibre has rational Leray class in the image fromX undera,b, after replacing the base by a nonempty open. The assertion that shrinking is unnecessary is separate and not proved.',
 'proof sketched','B',
 'KatzSGA7IIXX4.4 spells out finite extension, normalization, shrinking, descent and trace in the Griffiths proof. This verifies the version permitting these operations, not the manuscript’s hope to omit shrinking.',
 ['SGA7XX'],['P3-A01'],confidence='high')
ac(334,[351],
 'UnderSGA7XVIII5.8.4’s hard Lefschetz(LV) and pencil(A) hypotheses, the Griffiths map on primitive middle cohomology remains injective after quotienting the targetH1 by its fixed-part image, including the specified finite-base-change/open restriction version.',
 'stated without proof','B',
 'Exact resultSGA7IIXVIII5.8.7,1973, with hypotheses retained from5.8.4. The leaf calls the blow-up calculations trivial but does not give them; the published proof is the fate, not proof present on the manuscript page.',
 ['SGA7XVIII'],['P3-A03'])
ac(335,[352],
 'LetX be smooth projective connected of dimension2n≥4 over an algebraically closed field,ell invertible. For a Lefschetz pencil satisfying(LV),(A), non-curve-level vanishing cohomology and algebraic inverse(B), a codimension-n cycle whose geometric generic restriction is algebraically trivial has zeroQ_l-cycle class.',
 'proof sketched','B',
 'ExactSGA7IIXX4.1,printed355. Its four hypotheses are explicit; complete intersections admit sufficiently generalpencils of degreed>2dimX by4.2 andXXI5.2. No general standard-conjecture hypothesis is removed just by the high-degree condition.',
 ['SGA7XX','SGA7XXI'],['P3-A03'])
ac(336,[353],
 'Under the preceding Griffiths hypotheses, dim_Q(Griff^n(Y_generic)⊗Q)≥dim_Q Prim_alg^{2n}(X). The construction makes primitive algebraic cohomology a quotient of a subgroup of the Griffiths group; it gives no canonical injection in the opposite direction.',
 'proof sketched','B',
 'ExactSGA7IIXX5.1,printed361–362, states the dimension inequality and describes this quotient. The manuscript’s contains-as-subspace phrase is valid only as a noncanonical abstract vector-space consequence, if read that way.',
 ['SGA7XX'],['P3-A03'],computation='review.md §A36 Griffiths conclusion: quotient versus canonical embedding.')
ac(337,[354],
 'For fixed smooth projectiveX of even dimension2n≥4, sufficiently general sufficiently high-degree Lefschetz pencils satisfy conditionb: no curve correspondence contributes to the vanishing summand ofH^{2n−1}.',
 'open on the pages','C',
 'SGA7IIXX4.3 records the general positive-characteristic argument as heuristic, whereas the characteristic0 and complete-intersection cases are established there. Koblitz1975I§5 proves asymptotically growing Hasse–Witt stable rank for general high-degree sections of reduced equidimensionalCM varieties over finite fields; combined with spreading, the congruence formula and irreducibility this supplies a later route to the unit-root/nonconiveau consequence. It does not by itself establish the manuscript’s stronger every-trace theorem or the algebraic inversea. The exact global scope of this deduction is separated in review.md.',
 ['SGA7XX','SGA7XXI','Koblitz1975'],['P3-A04'],confidence='medium')
ac(338,[355],
 'Under theLefschetz assumptions, vanishing cohomology for a general pencil is absolutely irreducible. If the vanishing degree is odd, it remains so under every open subgroup because nonzero Picard–Lefschetz transvections remain nonzero under positive powers overQ_l.',
 'stated without proof','B',
 'ExactSGA7IIXVIII6.7.1 and6.7.2; the proof at6.7 uses powers of transvections. The oddness condition cannot be dropped: reflections can disappear under squaring.',
 ['SGA7XVIII'],['P3-A03'],computation='review.md §A36 transvections: (1+N)^r=1+rN forN²=0 in characteristic0.')
ac(339,[356],
 'In characteristic0, for high-degree smooth sectionsY of a fixed smooth projectiveX ofdimension2n,n≥2, the growth ofh^{0,2n−1}(Y) produces vanishing Hodge types outside(n,n−1),(n−1,n), so the irreducible vanishing cohomology is not generated by curve correspondences.',
 'proof sketched','B',
 'The Hodge argument is stated inSGA7IIXX4.3 and underlies Griffiths’s original characteristic0 method. The transcript’sE^{n−1} and “these values” are reading alarms, not mathematical alternatives accepted here.',
 ['SGA7XX','GriffithsIASBibliography'],['P3-A03'])
ac(340,[357],
 'A curve/abelian-level realization in a smooth proper family can be controlled by good-reduction methods after suitable finite extension. The much broader claim that motivic level always decreases under specialization is explicitly left unproved and lacks a unique category on the page.',
 'open on the pages','F',
 'The precise curve-level comparator isSGA7IIXX and the good-reduction criterionSGA7IX5.13. Searches in coniveau and standard-conjecture literature do not identify an unconditional theorem with all of the manuscript’s unstated motivic choices. A correspondence can be spread over an open, which is weaker than a theorem at every specialization.',
 ['SGA7XX','SGA7IX','SGA7XXI'],['P3-A04'],confidence='medium')
ac(341,[358],
 'If a weight2n−1 ell-adic representation overFq is a subquotient ofH1 of smooth proper curves twisted by−(n−1), its Frobenius eigenvalues are divisible byq^{n−1} as algebraic integers. Forn≥2, onep-adic unit eigenvalue excludes this realization.',
 'proof sketched','B',
 'KatzSGA7IIXXI and Deligne’s integrality appendix give the published integrality input. The Tate twist multiplies Frobenius eigenvalues byq^{n−1}; the assertion is about a specified correspondence realization, not arbitrary numeric weight alone.',
 ['SGA7XXI','SGA7XX'],['P3-A04'],computation='review.md §A36 integrality and twists.')
ac(342,[358],
 'The suggested converse from divisibility byq^{n−1} to curve-level motivic origin is a separate conjectural assertion. Divisibility is a necessary eigenvalue condition, not a demonstrated construction of algebraic correspondences.',
 'open on the pages','C',
 'The openedSGA7XXI integrality results prove the necessary direction. Generalized Tate/coniveau conjectures and standard-conjecture frameworks address converses only with extra hypotheses; no unconditional exact converse at this page’s generality was found.',
 ['SGA7XXI','Milne2022Standard'],['P3-A04'],confidence='medium')
ac(343,[359],
 'Strong7.1 would assert that for the generic high-degree section of an equidimensional projectiveCM scheme incharacteristicp, everya∈Fp occurs asTr(g|V0) for some element of the finite Galois image. The surviving inserted version permits an invariant subspaceV0′ depending on g anda.',
 'corrected by himself later','C',
 'The strong statement is marked not proved; the subspace insertion matches the weaker specialization mechanism of7.5/7.8. SGA7XXII supplies Frobenius-fixed representations but does not supply this every-whole-trace theorem. Koblitz1975 establishes stable-rank growth, a different quantified conclusion. No exact publication settlement of the every-trace version was identified.',
 ['SGA7XXII','Koblitz1975'],['P3-A05'],confidence='medium')
ac(344,[359,367,372],
 'The statement every residue occurs as a trace on an invariant subspace does not imply every residue occurs as a whole-space trace, non-p-group image, or the deleted dimension≥2 consequence. ForG={1} onFp^{p−1}, invariant subspaces have all dimensions0,...,p−1 but the sole whole trace isp−1.',
 'corrected by himself later','E',
 'This reviewer’s elementary counterexample checks the logical weakening and explains the explicit deletions; it is not a counterexample to strong7.1 for an actual geometric family. The casep=2 hasdimension1 and satisfies the weak assertion.',
 ['SGA7XXII'],['P3-A05'],computation='computations.py enumerates traces forp=2,3,5; review.md gives the general proof.',authorship='Reviewer diagnostic of a manuscript proof gap, not a theorem attributed to Grothendieck')
ac(345,[360,361],
 'For finitek, corollary7.2 claims every residue modulo p among#Y_t(k′), for some finite extensionk′ andt in any prescribed nonempty parameter open. The proposed Chebotarev proof requires an element with the desired whole-space trace onV0.',
 'open on the pages','C',
 'The margin expressly withholds the strong proof. SGA7XXII3.1–3.2 certifies the trace formula; it does not turn an invariant-subspace trace into a whole-space trace. No exact general publication of this strong point-count distribution theorem was found inSGA7, Koblitz1975, or the traced later literature.',
 ['SGA7XXII','Koblitz1975'],['P3-A05'],confidence='medium')
ac(346,[361],
 'For every proper schemeY overFq, #Y(Fq) modulo p equalsΣ_i(−1)^iTr(Fq|H^i(Y,O_Y)); equivalently its zeta function modulo p is the alternating determinant of theq-Frobenius operators on coherent cohomology.',
 'stated without proof','B',
 'ExactKatzSGA7IIXXII3.1 andCorollary3.2,1973, including nonsmooth proper schemes. This is the source explicitly credited toDeligne in the manuscript. Thecoherent operator must be theq-linear iterate, not a barep-semilinear trace overFq.',
 ['SGA7XXII'],['P3-A06'])
ac(347,[362],
 'For projective equidimensional Cohen–MacaulayX/k ofdimensionn, H^i(X,O_X(−d))=0 fori<n andd sufficiently large. IfY is an effective Cartier degree-d section, Hi(O_X)→Hi(O_Y) is an isomorphism fori≤n−2 and injective fori=n−1.',
 'proof sketched','E',
 'Serre duality forCM schemes plus Serre vanishing gives the negative-twist vanishing; the restriction exact sequence then gives the two conclusions. Koblitz1975I§2 explicitly uses and proves the relevant flat/base-change formulation for the general-section open.',
 ['Koblitz1975'],['P3-A06'],computation='review.md §A36 CM vanishing: duality and long exact sequence.')
ac(348,[362,367],
 'On the open of degree-d hypersurfaces meeting an equidimensionalCM X properly, for sufficiently larged the coherent cohomology sheaves needed in the construction are locally free and commute with base change. The generic Frobenius-stable part extends after shrinking to a locally free Frobenius-stable subbundle.',
 'stated without proof','B',
 'Koblitz1975I§2 proves the cohomological flatness/base-change input; SGA7XXII1 describes semilinear stable parts and fixed-point étale representations. Constancy of the full stable rank on the entire proper-section open is not inferred: shrinking is essential for the latter statement.',
 ['Koblitz1975','SGA7XXII'],['P3-A06'])
ac(349,[363],
 'For finitely many linear Frobenius endomorphisms over a finite field, a finite base-field extension raises their eigenvalues to a common power making each0 or1. Their alternating traces then equal the alternating sum of stable ranks and remain constant under further finite extension.',
 'proved there','E',
 'An eigenvalue is0 or lies in the finite multiplicative group of a finite extension; a common multiple of these group orders proves the assertion. Semisimplicity of the whole endomorphism is unnecessary because trace ignores nilpotent Jordan contributions.',
 ['SGA7XXII'],['P3-A06'],computation='computations.py finite-field eigenvalue-power checks; review.md general argument.')
ac(350,[364],
 'The proposed geometric corollary rules out curve-level vanishing cohomology for sufficiently general high-degree pencils, by obtaining point-count traces different from the fixed ambient contribution along a fundamental-group-surjective general line.',
 'proof sketched','C',
 'The manuscript proof depends on unproved strong7.2. SGA7IIXX4.3 retains the general positive-characteristic step as heuristic. The later Koblitz stable-rank result offers an independent unit-root route and does not validate this particular whole-trace argument.',
 ['SGA7XX','SGA7XVIII','Koblitz1975'],['P3-A04'],confidence='medium')
ac(351,[365],
 'Assuming hard Lefschetz and the usual primitive decomposition for smoothX ofdimensionn and smooth hypersurfaceY ofdimensionn−1, the low/high ambient trace pair isTr(F|H^iX)(1+q^{n−1−i}) for0≤i≤n−2, with separate ambient and vanishing terms in middle degreen−1.',
 'stated without proof','F',
 'The exponent follows from theGysin degree shift and the Lefschetz isomorphism. The transcribed alternatives2n−1−i and2n−2−i do not match these dimensions. This diagnoses a reading problem; the original ink is unavailable.',
 ['SGA7XVIII','SGA7XXII'],['P3-A06'],computation='review.md §A36 trace dimensions: degree and Tate-twist calculation.')
ac(352,[366],
 'If vanishing cohomology is an algebraic-correspondence quotient ofH^{n−3}(Z)(−1), this relation spreads over a nonempty open after finite extension, and at finite-field fibres its eigenvalues are divisible byq. Hence the presence of a unit eigenvalue rules out positive correspondence coniveau.',
 'proof sketched','B',
 'The spreading and integrality argument is the one used inSGA7IIXXI, with Deligne’s integrality appendix. It justifies the local implication independently of the manuscript’s unproved existence of the desired unit eigenvalue.',
 ['SGA7XXI'],['P3-A04'],computation='review.md §A36 integrality and twists.')
ac(353,[366],
 'Remark7.4 claims maximal leveln−1 for generic high-degree vanishing cohomology in all dimensions, and no nonzero lower-level subobject because the maximal such part is Galois-stable and the vanishing representation is irreducible.',
 'proof sketched','C',
 'The irreducibility argument is valid for a well-defined Galois-stable correspondence filtration. The unit-root premise is not supplied by the corrected7.1. Later stable-rank growth inKoblitz1975 supplies a separate finite-field route to nonconiveau for reducedCM X; identifying every motivic or support-filtration formulation still requires explicit conventions.',
 ['SGA7XVIII','SGA7XXI','Koblitz1975'],['P3-A04'],confidence='medium')
ac(354,[366],
 'The equivalence between the level defined by images of correspondences and the filtration defined by supports is queried; the author identifies resolution of singularities as the missing geometric input.',
 'open on the pages','C',
 'SGA7XXI defines and uses coniveau with its hypotheses. Modern niveau/strong-coniveau distinctions depend on coefficient ring and available resolutions/alterations; no unqualified integral equality is inferred here. The exact rationalell-adic statement must be fixed before attaching a general theorem.',
 ['SGA7XXI','BenoistOttem2021','AchterCasalainaVial2017'],['P3-A07'],confidence='medium')
ac(355,[367],
 'Lemma7.8 asserts that for every specialization s of any point t of a normal characteristic-p scheme, the special Frobenius-fixed representation occurs inside the representation at t after restriction to an open subgroup, with the same finite image. This is false for arbitrary t: on S=Spec F3[x,x^-1,y], F(v)=xv^3, take t generic on y²=x(x−2)² and s=(2,0). The representation at t is trivial, while the special representation has imageC2.',
 'false as stated','C',
 'The explicit counterexample is independently proved in review.md and checked in specialization_counterexample.py. Normality of S does not imply normality of the closure of t. The generic-point case on a normal integral base has the henselian fixed-locus proof C-SA13-363, using Stacks0BTN/04GK/02LP and SGA7XXII1; this is a valid repair, not an ink correction. The precise full assertion was not found as a published theorem.',
 ['SGA7XXII','Stacks0BTN','Stacks04GK','Stacks02LP'],['P3-A05','P3-A10'],confidence='high',computation='specialization_counterexample.py and outputs/specialization_counterexample.txt; review.md §A36 specialization lemma.')
ac(356,[368],
 'LetX⊂P^r_k be projective of pure positive dimension over a finite field andN≥0. There are a finite extensionk′/k andd0 such that everyd≥d0 has a degree-d hypersurface meetingX in the expected dimension with exactlyN points overk′. Singular sections are allowed.',
 'proof sketched','E',
 'Independently proved by choosingN geometric points plus one excluded point on each component, making them rational overk′, then using high-degree homogeneous interpolation at the finite setX(k′). Serre vanishing gives all large degrees. The proof verifies existence without the manuscript’s sharper bound; SGA7XXI/Koblitz use related singular-section specializations.',
 ['Koblitz1975','SGA7XXI'],['P3-A08'],computation='review.md §A36 interpolation: complete proof, without unproved numerical bound.')
ac(357,[369],
 'In the specific norm-form construction, selectingN points from a finite set ofcardinalityr d1^n requiresN≤r d1^n. The stated threshold(d1+1)(n+1) follows arithmetically once the same-degree interpolation and the zero-free auxiliary forms exist; those geometric existence assertions need their own proof.',
 'proof sketched','F',
 'The cardinal inequality and final zero-set symbol are reading alarms. Search ofSGA7XXI andKoblitz1975 did not identify the exact stated numerical bound as a published theorem. The general existence assertion is independently established inC-SA13-356, without pretending to settle this bound.',
 ['SGA7XXI','Koblitz1975'],['P3-A08'],confidence='medium',computation='computations.py cardinal inequality and degree arithmetic; review.md separates the interpolation step.')
ac(358,[370],
 'For finiteFq andd≥n+1, restrictingNorm_F(q^d)/Fq to an(n+1)-dimensionalFq-subspace gives a homogeneous degree-d form inn+1 variables whose onlyFq-zero is0. Over an algebraic closure it is a product ofd linear forms.',
 'stated without proof','E',
 'The norm is zero exactly at0 in a field, and an injective linear embedding preserves this property. The product over thed embeddings proves the factorization. This independently verifies the elementary construction used on the page, not smoothness of the resulting sections.',
 ['SGA7XXI','Koblitz1975'],['P3-A08'],computation='computations.py degree2,3,4 norm forms overF2; review.md general proof.')
ac(359,[371],
 'The text asserts reduction from an arbitrary characteristic-p field to a finite field for the generic Frobenius trace property, but does not specify the spreading, stable-rank and Galois-image compatibility needed to preserve its quantifiers.',
 'stated without proof','F',
 'SGA7XXII provides the finite-type semilinear machinery, andKoblitz1975 works overfinite fields. These are enough for specific unit-root specialization arguments after fixing the family, but no exact proof of every-trace preservation under the claimed reduction was found.',
 ['SGA7XXII','Koblitz1975'],['P3-A05'],confidence='medium')
ac(360,[372],
 'For a finitep-group acting on anFp-vector space, every element is unipotent and its whole-space trace equals the dimensionmodp. Thus two distinct whole-space traces imply the image is not ap-group. Two invariant-subspace traces do not imply this.',
 'proof sketched','E',
 'The minimal polynomial of an element ofp-power order divides(T−1)^{p^r}; the trace assertion follows. This proves the surviving conditional remark and pinpoints why it cannot be deduced from the weakened7.1.',
 ['SGA7XXII'],['P3-A05'],computation='review.md §A36 strong versus weak traces; computations.py trivial-group counterexample.')
ac(361,[372],
 'If two point-selection constructions have disjoint rational zero sets and coprime base degreesa,b, then products realize all sufficiently large degrees of the forma u+b v withu,v≥n+1. This arithmetic does not by itself supply disjoint geometric zero sets or the claimed optimal degree bound.',
 'open on the pages','C',
 'The coprime-degree assertion is the elementary numerical-semigroup fact; the improved geometric bound is only proposed. No exact theorem with the manuscript’s numerical parameters was found in the tracedSGA7XXI/Koblitz sources.',
 ['Koblitz1975','SGA7XXI'],['P3-A08'],confidence='medium',computation='review.md §A36 degree bounds: residue-class proof of eventual representability.')
ac(362,[373],
 'The final heading proposes heuristic relations among crystalline, quasi-/topo-crystalline and vanishing cohomology, but contains no formulated comparison map, hypothesis or theorem.',
 'open on the pages','F',
 'Oda1969,SGA7XXII and subsequent crystalline theory are contextual comparators only. The undecided word and absence of a statement prevent identification of one precise result or conjecture; giving notes toBerthelot is a provenance fact.',
 ['Oda1969','SGA7XXII'],['P3-A09'],confidence='high')

ac(363,[367],
 'Let S be normal integral noetherian of characteristicp, t its generic point, s any point, and V a locally free finite-rank module with p-linear endomorphism. The Frobenius-fixed representation at s occurs as a subrepresentation of the representation at t after a finite separable extension of k(t), with the same finite image group. The same repair applies if the relevant specialization is taken inside a normal integral closure of t with unchanged special residue data.',
 'proof sketched','E',
 'The fixed-point scheme is affine étale since the Jacobian of F(v)−v is−I. Over the henselization at s, its part meeting the closed fibre is a finite étale subgroup, with exactly the special Galois representation. Normality makes connected finite étale covers generically connected. Descent of the finite subgroup and its finite splitting torsor to an elementary étale neighbourhood supplies the required finite generic extension. Stacks0BTN,04GK,02LP were opened for the precise finite-part and henselian facts. This reviewer repair certifies the generic-point reduction, not the original arbitrary-point quantifier.',
 ['SGA7XXII','Stacks0BTN','Stacks04GK','Stacks02LP'],['P3-A10'],confidence='high',computation='review.md §A36 specialization lemma; algebraic proof, no numerical computation needed.',authorship='Reviewer refinement of the manuscript Lemma7.8')
