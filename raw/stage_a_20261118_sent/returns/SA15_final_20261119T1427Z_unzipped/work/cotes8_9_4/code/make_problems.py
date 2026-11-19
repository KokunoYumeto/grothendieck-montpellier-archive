"""Problem index authored from the questions, doubts and self-corrections read."""
from pathlib import Path
import json
W=Path(__file__).resolve().parents[1]
ps=[]
def p(n,title,occ,a,b,s,refs,why='No source located documents why this exact question remained open or was dropped.',worth='Worth a focused verification of the exact formulation; no general open-problem claim is made.'):
    ps.append(dict(id=f'P894-P{n:03d}',title=title,occurrences=occ,as_he_states=a,plausible_today=b,state_of_art=s,why_open=why,worth=worth,refs=refs))
p(1,'Universal mod-p representation lifting obstruction',
 ['cote8:81,70–78; P894-I004; C004–C006'],
 'The rank-d universal obstruction vanishes for d≤1 and is expected nonzero for all d≥2.',
 'ReductionGL_d(Z/p²)→GL_d(Fp) splits in rank1 and the exceptional pairs(2,2),(2,3),(3,2).',
 'Singla2010introductionp3 gives this classification, citing Sah1977 and Ginosar2001; the (2,2) splitting is independently certified here. The original Sah proof was not read.',
 ['Singla2010','Ginosar2001'],worth='The claim is resolved; a short research run should document the original proof and its relation to the precise cotangent Ext² class.')
p(2,'Truncated Dieudonné dualizing bimodule and two coefficient actions',
 ['cote9:5,196–242;7,303–335;8,336–392; P894-I008; C012–C015'],
 'Construct a coefficient-functional duality through finite Dieudonné rings and their direct limit; the text warns about different W-actions.',
 'Fix a single convention forW_n, truncation exponents, twisted left/right actions and transition maps, then formulate the compatible duality. The literal V-dual formula needs the ink check.',
 'Oda1969Theorem3.19 establishes Cartier/Dieudonné duality. Small exact ring computations here show why the truncation index matters. Codex cancels a finite-ring isomorphism that Pro leaves live.',
 ['Oda1969','BerthelotMessing1979'],why='The pages themselves flag the coefficient actions; cancellation differs between textual witnesses and cannot be decided without scans.',worth='Worth a concise convention audit after the scans are available, because it could settle several apparent contradictions at once.')
p(3,'Direct Gauss–Manin construction through a torsor of chain maps',
 ['cote9:9,393–425; P894-I009; C016'],
 'The canceled sheet asks for a direct Gauss–Manin construction and proposes descent of local chain maps related by homotopies.',
 'Use a specified derived enhancement with coherent descent data, or the later direct construction. Pairwise null-homotopies alone are not a complete theorem.',
 'IllusiePisa2015§3.2 records the Katz–Oda1968construction. It does not identify this exact discarded torsor lemma.',
 ['IllusiePisa2015'],why='The whole sheet is canceled; no reason for the cancellation is supplied.',worth='Useful for the manuscript commentary; a new research task should first recover the missing coherence conditions, not treat the draft as an established lemma.')
p(4,'Filtration-independent virtual inertia character of a p-divisible group',
 ['cote9:11,430–441;12,442–472; P894-I010,I011; C017–C020'],
 'Assign equivariantK₀ classes to models of potentially-good filtration factors, and obtain an inertia trace independent of filtration and good-reduction extension.',
 'For a fixed potentially-good object, finite inertia trace is compatible with extension. For the filtered construction, define the exact category and prove additivity/refinement independence before assigning a virtual character.',
 'Tate full faithfulness is verified in Illusie§2.3.1; the modern elliptic finite-inertia framework appears in Dembélé–Freitas–Voight§3.2. No opened source established this exactK₀ construction.',
 ['IllusiePisa2015','DembeleFreitasVoight2025'],worth='Worth a narrowly scoped exact-category reconstruction; the key first step is to specify which filtrations and equivariant models are allowed.')
p(5,'Brauer character from generic mod-p torsion',
 ['cote9:13,473–477; P894-I012; C021,C022'],
 'Try to identify the p-regular special-fiber inertia trace with the Brauer character of generic mod-p torsion, then retract the general claim.',
 'The comparison works for an actual finite integral representation, such as a potentially constant p-divisible group, and fails without that hypothesis.',
 'The manuscript counterexampleμ_p∞ overQp,p>2 is valid: good special-fiber inertia is trivial, mod-p cyclotomic inertia is not. This run checks that exact distinction.',
 ['DembeleFreitasVoight2025'],why='The manuscript explicitly gives the obstruction and withdraws the unrestricted comparison.',worth='Resolved as a negative claim; retain it to prevent the later elliptic question from being mistaken for the same statement.')
p(6,'Can constant p-torsion conceal potentially-good elliptic inertia?',
 ['cote9:13–14,477–487; P894-I013; C023,C024,C025,C077'],
 'Withμp⊂K, do potentially-good elliptic curves with the same mod-p module have the same p-regular inertia character? A constant-torsion version is followed by an uncertain “faux par Tate” leader.',
 'The answer is no even forp5 and with a supersingular potentially-good curve. Finite WD/ℓ≠p inertia must be distinguished from rawT_p inertia.',
 'proofs.md§1 gives an independent pair overK=F(5^(1/8)), F/Q5 unramifieddegree4: y²=x³+5⁴ andy²=x³−x have constant5-torsion, but order3 finite-inertia traces−1 and2. The saved exact polynomial andF25 certificate checks the Hensel hypotheses. Modern type classification corroborates the finite inertia; Tate’s historical example is not identified.',
 ['DembeleFreitasVoight2025'],why='The margin may record a negative answer by Tate, but its attachment is unresolved and no example is written.',worth='The mathematical question is refuted; the remaining useful task is historical identification of the margin and comparison with Tate’s actual communication.')
p(7,'Full F,V-compatible stratification of universal abelian deformations',
 ['cote9:15–18,488–563; P894-I014–I016; C026–C029'],
 'Seek a functorial full k-stratification ofH¹_dR for all infinitesimal deformations, compatible withF,V and base change; expect ordinarity to be necessary.',
 'Ordinary unit-F pieces have canonical local-system stratifications. Necessity must retain “all deformations” and specify compatibility and Hodge behavior; a constant nonordinary family does not address that universal question.',
 'Katz1981gives ordinary formal parameters and explicit Gauss–Manin formulas. Illusie§4.2.1 gives the smooth deformation space. No exact necessity theorem for this formulation was found.',
 ['Katz1981','IllusiePisa2015'],worth='Worth a short formulation task separating the Hodge-preserving unit-F stratification from Gauss–Manin before asking a necessity theorem.')
p(8,'Descending equality through Frobenius on a nilpotent base',
 ['cote9:17,526–544;18,545–563; P894-I015; C028'],
 'The equality after Frobenius pullback is not enough if the base is nonflat; the next page uses the smooth universal deformation space.',
 'Faithfully flat Frobenius detects equality of the subbundles; arbitrary Frobenius does not.',
 'The two-line dual-number example independently confirms the obstruction. Formal smoothness supplied by the deformation theorem validates the author’s later repair.',
 ['IllusiePisa2015'],why='This doubt is resolved by the author on the next page, not left open.',worth='No new research is needed; the commentary should join the warning and its continuation.')
p(9,'Polarization class, tangent map and transpose p-torsion map',
 ['cote9:20,605–640; P894-I018; C032'],
 'Identify the middle deRham component of a Néron–Severi class with the tangent map induced by its homomorphismA→A*, compatible with the transpose map on étale p-torsion.',
 'The statement is expected with fixed covariant/contravariant conventions and the live corrected arrow direction.',
 'Oda’s deRham realization and crystalline Dieudonné duality provide the framework, but this run has not certified every sign in the manuscript’s altered diagram.',
 ['Oda1969','BerthelotMessing1979'],worth='Worth checking jointly with the determinant normalization because the same duality conventions control both.')
p(10,'Unpolarized determinant line and Hasse compatibility',
 ['cote9:22,663–688;29,901–909; P894-I020,I025; C034,C044'],
 'The top-trace/Hodge constructionω_A≃ω_A* should respect ordinary unit-F structures and Hasse invariants, and match the later mod-p Tate determinant.',
 'A determinant-level compatibility with a fixed order of exterior factors is plausible. It does not imply an isomorphism of the full rank-g p-torsion modules.',
 'The Hasse determinant criterion is exact in CaraianiLemma4.1.7. Standard duality is established, but no source located gives this precise comparison of the author’s two normalizations.',
 ['Caraiani2017','Oda1969','Katz1981'],worth='A few-hour normalization audit could settle a precise rank-one compatibility; first fix all determinant and biduality signs.')
p(11,'Explicit ordinary connected–étale extension data',
 ['cote9:23,689–713; P894-I021; C035,C036'],
 'Beyond perfect-base splitting, explicate the extension of multiplicative by étale factors over a general deformation base.',
 'For ordinaryA over algebraically closedk and artinian localR, the extension is encoded by bilinear mapsT_pA_et×T_pA*_et→1+m_R; global bases require descent.',
 'KatzTheorem2.1 answers this exact formal-neighborhood problem. Illusie’s discussion of Grothendieck’s letter6.7 distinguishes a more general extension-deformation explanation.',
 ['Katz1981','IllusiePisa2015'],why='Illusie says the extension-deformation part of the letter was not discussed in two later accounts; he does not give a reason for that omission.',worth='Established locally; a useful historical task would compare the letter’s general extension argument with the manuscript’s short question.')
p(12,'Polarization-independent ordinary Tate determinant',
 ['cote9:24–25,731–793;27–28,830–864; P894-I022; C037–C040'],
 'Prove thatdetT_p(λ)_et/√degλ is independent of polarization and identifies integral determinant lattices; an intermediate sign remains doubtful before scan27.',
 'The positive Rosati-symmetric proof and Cartier-self-dual kernel argument give the claimed determinant isomorphism for ordinary abelian varieties over perfect fields.',
 'The author ends the sign argument “cqfd” and then proves integrality. MilneTheorem11.1 and§14 supply standard ingredients. Searches did not locate the exact normalized construction as a named later theorem.',
 ['Milne2008','Katz1981'],why='The sign doubt is resolved within the same text; it did not remain open in these pages.',worth='Worth editorial reconstruction and a precise reference search, not another attempt to solve the already completed sign step.')
p(13,'Naturality with the correct dual variance',
 ['cote9:15,488–498;23,710–713;28–29,866–900; P894-I024; C041'],
 'A broad functoriality objective is canceled, then the author identifies the wrong variance and usesu*⁻¹ for automorphisms.',
 'The normalized determinant intertwines an isomorphism with its contragredient dual, and the two determinants for an isogeny multiply to its degree.',
 'The product identity follows from ordinary étale/multiplicative duality. It does not give equality of individual determinants under unrestricted endomorphisms.',
 ['Oda1969','Milne2008'],why='The manuscript explicitly identifies “mauvaise variance” and narrows the assertion.',worth='Resolved at the stated scope; retain the cancellation so the opening objective is not reinstated.')
p(14,'Biduality and product signs for the Tate determinant',
 ['cote9:29,901–909; P894-I025; C042,C043'],
 'Check compatibility withA**, products, and the sign of the duality identifications.',
 'Product compatibility follows with ordered determinant factors and product polarizations. Biduality requires fixing the alternating-form convention; a convention-free sign is not supplied.',
 'Milne’s duality and Rosati discussion supply standard background. No exact published sign computation for this normalization was located.',
 ['Milne2008','Oda1969'],worth='A compact determinant-functor calculation is realistic in one research run; the scan check must precede assigning the final sign.')
p(15,'Transpose of the auxiliary F/V middle sequences',
 ['cote4:2–3,938–1019; P894-I026; C045–C048'],
 'The two middle-degree sequences are “sans doute” transposes; the superscript/subscript ss refers to different stable operators.',
 'Derived crystalline duality should identify them with the correct twist and adjacent torsion degree. A naïve same-degree transpose is not enough.',
 'Illusie1976§2.4 gives crystalline duality/Gysin formalism. KatzXXII(3.3.4) supplies the F-stable augmentation. Uncertain F/V labels prevent a unique exact comparison.',
 ['Illusie1976','KatzSGA7XXII'],worth='Worth a limited derived-duality diagram audit once the uncertain indices are read on the scans.')
p(16,'Integral weak Lefschetz with saturated cokernel',
 ['cote4:4–7,1020–1124; P894-I029,I032; C051,C056'],
 'Admit an integral weak Lefschetz theorem strong enough that the critical restriction is injective with free cokernel for the smooth hypersurface sections under discussion.',
 'The claim is established for all sufficiently high powers of a chosen ample line bundle under the coherent-vanishing hypotheses. The fixed-embedding all-degree version needs separate examination.',
 'BMSLemma2.12 proves the sufficiently ample form and cites Berthelot’s1973note. Rational weak Lefschetz does not imply saturation.',
 ['BMS2016','Illusie1979metadata'],worth='High value: resolving the exact all-degree scope determines the domain of several subsequent manuscript formulas.')
p(17,'Injectivity of stable coherent restriction',
 ['cote4:8,1147–1152; P894-I034; C060'],
 'Expectv:H^(n−1)(O_X)_st→H^(n−1)(O_Y)_st injective; state it forn2 and coherent-vanishing high degree.',
 'The two stated cases are valid. The all-dimensional, all-smooth-hyperplane version is not certified here.',
 'Stable-F/Artin–Schreier interpretation is in KatzXXII; the high-degree assertion follows from the coherent long exact sequence. The surface case uses π₁ Lefschetz. Searches did not find a precise broader theorem.',
 ['KatzSGA7XXII','BerthelotEsnaultRulling2012'],worth='Worth a targeted étale-cohomological Lefschetz search because a positive answer simplifies the entire relative correction term.')
p(18,'Relative vanishing unit-F local system and constant kernel',
 ['cote4:8–10,1158–1214; P894-I035; C061–C064'],
 'On the generic maximum-rank open, the amended sequence should vary as finiteFp local systems with kernel coming from the base field.',
 'Shrink for locally free stable images and base change, and controlker v. High degree withker v0 gives the claimed constant torsion kernel.',
 'The unit-F dictionary and Hasse–Witt variation are established in Katz/Koblitz. The full relative integral sequence for exactly the manuscript’s initial open was not located.',
 ['KatzSGA7XXII','Koblitz1975'],worth='Worth a precise base-change construction; the first step is to separate stable-rank openness from crystalline saturation and constant-kernel hypotheses.')
p(19,'Eventual generic positive stable vanishing rank',
 ['cote4:9,1173–1183; P894-I036; C065'],
 'Show generic stable coherent vanishing cohomology is nonzero for every sufficiently large degree; margin says section7 already proves it, but that section is absent.',
 'The exact positivity statement holds for all projective equidimensional Cohen–MacaulayX of dimension≥1, with a degree bound depending onX and its embedding.',
 'KatzSGA7II,XXI,Theorem1.4,pp374–376 is an exact published match. It is stronger in its allowableX than a smooth-complete-intersection-only result.',
 ['KatzSGA7XXI'],why='The local text claims an internal resolution. The supplied pages do not contain that proof; the later theorem is verified independently.',worth='Resolved; the remaining task is historical comparison of the absent section7 with the SGA proof, if that manuscript is supplied.')
p(20,'Unit roots and maximal motivic level',
 ['cote4:9,1173–1176; P894-I036; C066'],
 'The nonzero unit-root condition should imply, and perhaps be equivalent to, motivic leveln−1 of generic vanishing cohomology.',
 'A unit root obstructs positive coniveau. The converse needs a precise notion of level and additional input; it is not asserted for allX.',
 'KatzXXICorollary2.2 proves eigenvalue divisibility for coniveau, andTheorem4.2 proves a complete-intersection maximal-level result. These do not prove the general equivalence.',
 ['KatzSGA7XXI'],worth='Worth a formulation task only after recovering the author’s definition of level; otherwise an apparent conjecture may conflate distinct notions.')
p(21,'Comparing the crystalline torsion criterion with a characteristic-zero lift',
 ['cote4:10,1222–1230; P894-I037; C068'],
 'IfX and polarization lift to characteristic0, express the sufficient torsion condition forφ-bijectivity through p-adic étale cohomology of the lift.',
 'Integral comparison gives inequalities and criteria under extra hypotheses; an unrestricted equality of crystalline and étale torsion is false.',
 'BMSTheorem1.1 and§2.3 give the precise torsion-length comparison and strict examples. They do not directly settle the author’s stable-F condition.',
 ['BMS2016'],worth='Worth a narrow comparison of the exact stable piece with integral p-adic realizations, keeping the known strict inequalities visible.')
p(22,'Examples where the revisedφ is not bijective',
 ['cote4:10–11,1232–1277; P894-I038,I039; C067,C069,C070,C072'],
 'Find examples whereφ fails to be bijective; the earlier nonsurjectivity wording and product examples are canceled.',
 'For a Serre freeZ/p quotient surface withH¹_cris0 andH¹_et(Fp)=Fp, the stableH² crystalline torsion gives a one-dimensionalkerφ, under the admitted section hypotheses.',
 'Berthelot–Esnault–RüllingRemarks9.2 verifies the historical quotient mechanism. The short crystalline implications are checked in proofs.md. No new high-dimensional geometric example is asserted.',
 ['BerthelotEsnaultRulling2012','Illusie1976'],why='The author replaces nonsurjectivity by nonbijectivity after correcting his exact sequence; the original product is crossed out.',worth='The surface example is adequate for the live request; a higher-dimensional construction would be a separate task with all cohomology and saturation assumptions checked.')
p(23,'Equality criterion and preceding-degree stable torsion',
 ['cote4:11,1254–1260; P894-I039; C071'],
 'Assert thatφ-bijectivity is equivalent to equality in the stable coherent versus free-crystalline dimension inequality.',
 'Underker v0 and absence of preceding-degree stable torsion the equivalence holds. In general the inequality defect isb+c whereasdimkerφ=c−dimker v.',
 'The exact elementary derivation in proofs.md§2 uses the opened base-change and stable-augmentation results. It shows a missing-hypothesis issue without claiming a geometric counterexample.',
 ['KatzSGA7XXII','Illusie1976'],why='The manuscript does not discuss the extra preceding-degree term; whether an omitted hypothesis or a reading explains it is unresolved.',worth='High priority for the next scan-based commentary: first check whether a missing qualification removes the extra term.')
p(24,'FullGL_r(Fp) monodromy for fixed-X hypersurface sections',
 ['cote4:12,1280–1296; P894-I040; C073'],
 'Is the varying stable coherent vanishing representation irreducible, or even fullGL_r(Fp), for generic hypersurface sections of a fixed smooth projectiveX?',
 'Specify geometric versus arithmetic image, degree range, rank, and fixed constant subquotients. Established full-image theorems for other parameter spaces do not imply this one.',
 'Achter–PriesProposition4.8 proves full modp andp-adic monodromy on components of curve p-rank strata. Stienstra–van derPut–van derMarel studies specified unit-root families. Neither gives the exact arbitraryX theorem; searches recorded no matching general result.',
 ['AchterPries2008','StienstraPutMarel1991'],worth='Highest research interest, but one short run should test a concreteX and degree and audit arithmetic determinants before attempting the universal claim.')
p(25,'Growth of generic stable vanishing rank',
 ['cote4:9,1179,deleted growth replaced by positivity;12,1307–1312; P894-I036,I041; C065,C074'],
 'The early growth expression is weakened to positivity, but unbounded rank is needed again for the final monodromy/congruence programme.',
 'For a fixed smooth projective n-foldX of degreeD, the generic stable vanishing rank has leading term Dd^n/n!, hence tends to infinity.',
 'KoblitzI§5Theorem1 explicitly states the leading term for a constructed section; Lemma4 transfers the stable-rank lower bound to a generic open for Cohen–MacaulayX in sufficiently high degree, and Theorem2 combines them. The unread displayed defect inequality is not needed for this conclusion.',
 ['KatzSGA7XXI','Koblitz1975'],worth='The unboundedness branch is settled; the remaining research obstacle is the separate monodromy question.')
p(26,'Every-open hypersurface point-count residues',
 ['cote4:12,1295–1312; P894-I041; C075,C076'],
 'Use fullGL monodromy and every residue as a matrix trace to force specified point-count congruences in every nonempty parameter open after suitable finite field extension.',
 'The conclusion is conditional on geometric monodromy and allowed Frobenius cosets, with fixed cohomological contributions controlled after extending constants. Variable extension degrees are part of the statement.',
 'The trace-surjectivity calculation is proved independently. KatzXXIICorollary3.2 gives the modp cohomological trace congruence. The missing allX monodromy prevents an unconditional conclusion.',
 ['KatzSGA7XXII','AchterPries2008'],worth='Worth a concrete-family experiment only after its monodromy is established; the elementary trace input is already complete.')

(W/'problems.json').write_text(json.dumps(ps,ensure_ascii=False,indent=2)+'\n')
print('Wrote',len(ps),'problems, including locally resolved and withdrawn questions explicitly labeled.')
