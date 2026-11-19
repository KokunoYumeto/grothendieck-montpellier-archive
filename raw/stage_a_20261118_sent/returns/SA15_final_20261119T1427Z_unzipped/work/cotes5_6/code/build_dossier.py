"""Serialize the manually consolidated research records.

Semantic groups, statements and verdict reasons below are hand-authored after
reading all source passages. This program does NOT infer verdicts from keywords.
It supplies IDs, source coordinates, TSV escaping and consistency checks only.
"""
from pathlib import Path
import json, csv, re

ROOT=Path(__file__).resolve().parents[1]
PKG='MPL_5+6_001-037'
RUN='GPT-6 Astra Pro; effort not exposed; run SA15-20261119/cotes5_6'
DATE='2026-11-19'
notes={x['ordinal']:x for x in json.loads((ROOT/'outputs/supplemental_note_inventory.json').read_text())}
pages={(int(x['cote']),x['scan']):x for x in json.loads((ROOT/'outputs/page_inventory.json').read_text())}
items=[]; claims=[]; problems=[]; events=[]; groups={}; entry_verdict={}

def coords(ns):
    ks=sorted({(int(notes[n]['cote']), notes[n]['scan']) for n in ns})
    return sorted({c for c,s in ks}), [{'cote':c,'scan':s} for c,s in ks], [dict(cote=c,scan=s,transcription_file_lines=f"{pages[c,s]['start']}–{pages[c,s]['end']}") for c,s in ks]

def I(key,ns,kind,quote,statement,reconstruction='',reason='',check='agrees'):
    assert key not in groups
    assert all(n not in entry_verdict for n in ns),(key, [n for n in ns if n in entry_verdict])
    ident=f'P56-I{len(items)+1:03d}'; groups[key]=ident
    cote,scans,lines=coords(ns)
    reason=reason or 'The entry preserves the assertion, its local qualifications and its evidential status in the quoted transcription passage.'
    obj=dict(id=ident,sources=[notes[n]['id'] for n in ns],kind=kind,cote=cote,scans=scans,lines=lines,his_words=quote,statement=statement,reconstruction=reconstruction or 'No unstated theorem is supplied; the modern formulation fixes only the notation and hypotheses explicitly identified here.',check=check,check_reason=reason,internal_key=key)
    items.append(obj)
    for j,n in enumerate(ns):
        entry_verdict[n]={'entry_id':notes[n]['id'],'item_id':ident,'verdict':'kept' if j==0 else 'merged','reason':reason}
    return ident

# Cote 5. The sources are actual ## ordinal identifiers, not NOTES_INDEX IDs.
I('points',[1],'self-flagged step','détermination des points de ces topos ?',
  'Determine points of the different connection, stratification, infinitesimal and PD topoi in the diagram. This is a question, not an asserted equivalence with Zariski points.',
  'Each topos must first be fixed; points mean geometric morphisms Set→T. No answer is inferred from the diagram alone.')
I('comparison_q',[2,90,257,263],'unproved claim','équiv -- car 0; tenseur courbure',
  'For a smooth morphism over a Q-scheme, ordinary stratifications on modules correspond to integrable connections. Factorial invertibility is essential; the phrase characteristic zero is insufficient for arbitrary base rings.',
  'The Q-scheme and smoothness hypotheses are the precise published version, not a silent replacement of the manuscript wording.',
  'The notes expressly demand factorial invertibility and preserve the diagrammatic, unproved status; the later BO comparison supplies the restricted theorem.')
I('chern_rank_one',[3],'unproved claim','NS; une connexion intégrable',
  'The page proposes necessity and sufficiency of vanishing of a displayed first Chern class for an invertible module to arise from the relevant crystalline topos. Its coefficient group and superscript are not secure.',
  'Modern crystalline Chern vanishing gives a necessary condition for a line bundle underlying a locally free crystal over W(k), for X smooth over perfect k. It does not by itself prove the page’s converse.')
I('diagram_readings',[4],'reading question','isomorphismes de localisation',
  'The adjective gerbienne/galoisienne and the Chern-class superscript remain unresolved. They affect both the diagram and the last obstruction statement.',reason='The notes retain the local alternatives; without scans neither reading is promoted to current ink.')
I('serre_tate_leaf',[5,6,7],'other','THEOREM 12',
  'A pasted foreign theorem: for a CM abelian variety A of dimension d over a number field K, with the degree-2d CM field acting over K, the conductor of A is the 2d-th power of the associated Hecke character conductor. Its support is the bad-reduction locus.',
  'The exact match is Serre–Tate 1968, §7, p.514, Theorem12, with §§4–5 hypotheses. The publication does not date the particular typescript leaf.',
  'Exact title, theorem and preceding local conductor argument were matched; this is not attributed as an original Grothendieck theorem.')
I('universal_pd',[8,9],'unproved claim','On va construire un objet initial de cette catégorie',
  'The finite p-typical presentation is proposed as the initial ν-truncated divided-power Artinian ring with residue field k; its maximal ideal is the displayed J and it has residue k.',
  'Use the manuscript’s precise truncation convention and W=W(k). Existence of divided powers and the universal property are separate from a calculation of the underlying quotient ring.')
I('pd_basepoint',[10],'unpursued implication','Λ_i=λ_i+Θ_i',
  'Translation by λ_i=p^(p^i)/(p^i)! centers the universal presentation at the canonical divided powers of p.',
  'This describes a coordinate change. It does not assert a deformation representability theorem absent from the text.')
I('pd_normalform',[12,13,15,16,18,19],'self-flagged step','La vérification est facile et laissée au lecteur',
  'For A=W[Λ_0,…,Λ_ν]/(Λ_i^p−q_iΛ_(i+1),Λ_ν^p), q_i=(p^(i+1))!/((p^i)!)^p, write Θ_i=Λ_i−λ_i. The quotient by (Θ_0,…,Θ_r) has independent bounded monomials with coefficient moduli p^(i−r) at first nonzero index i>r and constant modulus p^(c(ν)−r).',
  'The general ideal-stability proof is independently supplied in reviews/independent_proofs.md. The 20 Smith tests corroborate but do not prove arbitrary parameters.',
  'These entries concern one normal-form theorem, its valuation input, its explicitly omitted necessity check and its r-quotients; none is read as already fully proved on the pages.')
I('pd_finite_certificate_idea',[17,23],'idea of the earlier run','La vérification est facile et laissée au lecteur',
  'Earlier notes propose finite reductions and carry-system computations for the universal PD algebra.',
  'Executed here as exact multiplication/Smith computations for 20 parameter triples, with a separate general proof. These checks are not claimed to be Lean certificates.',
  'Kept as the earlier run’s proposal, not as words or work performed by Grothendieck.')
I('pd_weighted_nilpotence',[21],'unproved claim','Ceci implique',
  'A monomial in the Λ_i vanishes whenever its p-weight Σa_i p^i is at least p^(ν+1), by successive carries and Λ_ν^p=0.',
  'The carrying order must terminate; weight is preserved by an internal carry, and the bounded normal-form digits have maximum weight p^(ν+1)−1.')
I('pd_early_readings',[11,14,20,22],'reading question','λ_r; C_i^p; a_i=pq_i+a′_i',
  'Factorial placement, the upper summation bound p−1/p, the coefficient index i/α, the first-nonzero quotient index, and changing carry variables need inspection of the scans.',reason='All alternatives are preserved. The mathematical normal form raises alarms but does not decide the ink.')
I('height_dimension',[24,25],'unproved claim','Ceci est impossible',
  'In the foreign quasi-function fragment, a divisor in A^5 cannot project to codimension at least two in A^4 under the stated finite-dimensional integral product hypotheses. The subsequent ratio identity is a proposed specialization/cocycle relation.',
  'The dimension argument requires A geometrically integral finite type and the closed subset genuinely codimension one; specialization must avoid zeros and poles.')
I('height_dimension_idea',[27],'idea of the earlier run','Ceci est impossible',
  'The earlier run supplies the fiber-dimension reconstruction: dim Z=5d−1 and projection fibers have dimension at most d, so dim image≥4d−1.',
  'This elementary proof is independently rechecked; it supplies no missing hypotheses or absent quasi-function definitions.',reason='The note marks its hypotheses and is a reconstruction, not an additional manuscript paragraph.')
I('height_descent',[31],'unproved claim','est définie sur K',
  'A limiting quasi-function value μ(q,a) is asserted to descend to K. The limit must exist and be independent of the extension of a valuation before descent follows.',
  'Only the conditional descent argument can be identified from this isolated leaf; the preceding definitions and normalization are absent.')
I('height_descent_idea',[33],'idea of the earlier run','la limite',
  'Earlier notes propose comparing the same approximating sequence under two extensions of a valuation, then using uniqueness of the limit to establish descent.',
  'This is conditional on equality of the finite terms and existence in the relevant complete value group, not a proof of convergence.')
I('height_quasifunctions',[114,115,116],'unproved claim','ne dépend que; un homomorphisme',
  'The pasted quasi-function leaves assert independence of representatives, a translation-compatible divisor/principal-class homomorphism ξ_0, and symmetry relations (15), whose proof begins but is not complete.',
  'The likely Néron height context does not identify the missing definitions or prove exact bibliographical provenance; the statements remain only partially identifiable.')
I('height_dyadic',[125,126],'unproved claim','|φ(m)|≤d',
  'If |φ(2^hm)−2^hφ(m)|≤(2^h−1)d and φ(2^hm)/2^h→0, then |φ(m)|≤d. The source writes the positive-excursion contradiction but not its negative analogue.',
  'The two-sided conclusion follows by division by 2^h and passage to the limit; the recurrence and normalized limit are the hypotheses.')
I('height_dyadic_idea',[127,128],'idea of the earlier run','par récurrence sur h',
  'Earlier notes complete the omitted negative half by replacing φ with −φ, or directly by dividing the absolute-value estimate by 2^h.',
  'Both arguments are independent re-proofs of the same conditional inequality; neither reconstructs the preceding missing height argument.')
I('height_readings',[26,32,117,118,129],'reading question','q_a=∏_i m_i q_(a_i); p.45',
  'Foreign-leaf orientation and source pagination are distinct from scan numbering. Baseline m_i versus exponent, q versus underlined q, and missing preceding context need checking before assigning a full divisor formula.',reason='The notes distinguish orientation, typography and missing context; no external title is treated as an exact match.')
I('legendre',[29,34,195],'unproved claim','v_p(n!)=(n−Σa_i)/(p−1)',
  'Legendre’s digit formula implies sup_n v_p(n!)/n=1/(p−1). The valuation of π^n/n! is positive for all n≥1 at the weak threshold v_p(π)≥1/(p−1), but tends to infinity exactly at the strict threshold.',
  'At equality choose n=p^h, for which the digit sum is one. The n=0 term is excluded from positivity.')
I('valuation_ideas',[30,36,108,197],'idea of the earlier run','chif(n)',
  'Earlier notes use digit sums to test p-units, factorial coefficients, convergence and the DVR boundary.',
  'Recomputed exactly and proved from Legendre here. These are mathematical reconstructions, not new transcript readings.')
I('factorial_digit_readings',[28,35,107],'reading question','v_p(p²)=p+1; chif(n)≤1',
  'Several literal valuation arguments omit factorial signs. The surviving bounds chif(n)≤1 and chif(n)≤(p−1)ν conflict with the base-p expansion indexed from 0 through ν.',
  'Likely alternatives are the factorial argument and 1≤s_p(n)≤(p−1)(ν+1) for n≥1. The scans must decide these forms.',reason='The notes report the discrepancy without silently restoring the missing signs.')
I('covers_c5',[37,38,39,57,206],'title, date or page count','Frobenius; à puissances divisées; Lettre Deligne',
  'Correction-sheet markings, cover headings and the Deligne-letter docket are documentary evidence only. The correction target on pages64–76 is unidentified, and tick/diagonal marks are not automatically deletions.',reason='These entries have no independent mathematical claim; they are retained for documentary continuity.')
I('topos_transport',[40,41,42],'unproved claim','Fait analogue pour E dans une catégorie dérivée',
  'Direct and inverse image transport an object equipped with an endomorphism-comparison map. A derived analogue is announced without boundedness or coherence data.',
  'The elementary sheaf construction is distinguished from the deleted complex/abelian restrictions and the separate derived expectation.')
I('topos_universal',[43,44,47,48,51],'self-flagged step','L(α,β) est un topos; à vérifier',
  'For parallel geometric morphisms α,β the category of pairs (E,α*E→β*E), with an invertible variant, is asserted to be a topos representing the displayed two-categorical universal property. The small-generator step and precise section-category model are not completed.',
  'SGA4 I9.25 gives a generator theorem for section/cartesian-section categories with accessibility hypotheses. Applying it to the noninvertible construction requires an actual indexed-category construction.')
I('topos_set_idea',[46],'idea of the earlier run','les couples (E,F_E)',
  'At X=X′=Set and α=β=id, the category is Set with an N-action; the invertible variant is Set with a Z-action.',
  'This explicit presheaf-topos model is checked, but it proves only this test case of the general topos assertion.')
I('topos_generator_idea',[49],'idea of the earlier run','sections cartésiennes',
  'The earlier run proposes constructing the noninvertible parallel-arrow category as an indexed section category before using SGA4.',
  'The proposal remains a research lead; the present run checks the cited SGA statement, not an unwritten equivalence of models.')
I('topos_derived',[52,53,56],'conjecture','on aimerait savoir que ce sont des isoms',
  'The forgetful functor from the comparison topos is expected to commute with higher direct images. The proposed reduction asks that underlying objects of injectives be acyclic and invokes adjoints/product conditions.',
  'An exact left adjoint, rather than merely a left adjoint, ensures preservation of injectives. The manuscript does not prove the required exactness or the general derived comparison.')
I('topos_derived_idea',[54],'idea of the earlier run','injectif; acyclique',
  'Earlier notes propose the α=β=id test and construction of an adjoint to isolate the acyclicity issue.',
  'The Set/module-with-endomorphism case has the exact free action functor ⊕_(n≥0)M. This does not establish all geometric-morphism cases.')
I('topos_readings',[45,50,55],'reading question','ω_X*(R^iv_*(E))',
  'Ambiguous arguments X/X′/Y and underspecified two-cell drawings affect the universal property. The higher-direct-image formula uses ω_X on an object over the target comparison topos.',
  'ω_Y is a type-correct candidate in that display, pending ink inspection.',reason='The notes flag the source/target mismatch and do not erase the literal X.')
I('pd_axioms',[58,59,61],'unproved claim','Pseudo-anneau; n!π^n(x)=x^n',
  'The positive-degree PD identities are formulated first on a nonunital algebra, with extra ambient scalar compatibility for an ideal. The multinomial and factorial identities follow, and Z-scalar compatibility is automatic.',
  'Degree zero requires the unit of an ambient ring. Integer homogeneity follows from addition, inverse elements and the factorial-free PD identities.')
I('pd_torsion_idea',[60],'idea of the earlier run','n!π^n(x)=x^n',
  'The earlier run notes that the factorial identity forces uniqueness in torsion-free rings but leaves factorial-torsion ambiguity otherwise.',
  'This is a necessary uniqueness test, not a sufficient construction of a PD structure on an arbitrary torsion ideal.')
I('free_pd',[62,65,66,75,76],'unproved claim','On va les prolonger; un rôle universel',
  'The graded divided-power algebra Γ(M) with its positive ideal is the free PD algebra on M; Γ(Sym(M),Sym⁺(M)) identifies with Γ(M) by matching their universal properties.',
  'All six PD identities and scalar compatibility are required, not only the iteration formula on pure generators.')
I('free_pd_idea',[64],'idea of the earlier run','(x^(p))^(n)',
  'Earlier notes propose checking the extension on free modules and arbitrary sums before descending to all modules.',
  'Kept as a verification strategy; the actual published construction is in Roby and the Stacks Project.')
I('pd_envelope',[67,70,71,73,103,105],'unproved claim','universel; Il faut introduire sur J des puiss. div',
  'The manuscript presents a universal PD envelope of an ideal map by generators and relations, including the relation γ_1(x)=x. Quotient descent requires PD stability; a canceled multiplication calculation does not prove the proposed more general pushout.',
  'The established universal PD envelope is compared with the surviving presentation. The abandoned nonunital/ambient-ring variant is not silently treated as a completed construction.')
I('pd_quotients',[77,79],'unproved claim','Oui; et pour un tel seulement',
  'A quotient of a PD algebra inherits the operations exactly when the quotient ideal is stable under divided powers. The smallest such ideal killing generators x_i is generated by all γ_n(x_i), n≥1.',
  'Representative independence follows by the PD addition formula; ideal stability of this generated ideal uses scalar, addition and iteration formulas.')
I('pd_quotient_idea',[78],'idea of the earlier run','λ_ni π^n(x_i)',
  'Earlier notes propose checking PD stability term by term for finite sums of scalar multiples of γ_n(x_i).',
  'The exact argument is established in Stacks23.4.4 and has been checked against the manuscript’s generators.')
I('pd_nilpotence_exp',[80,81,82],'unproved claim','J^(Nn+1)=0; deux isom de groupes inverses',
  'A nil ideal with N generators each killed by exponent n+1 satisfies J^(Nn+1)=0. Uniform and elementwise PD truncation differ. Under suitable terminating PD sums, exp(x)=Σγ_n(x) and log(1+x)=Σ(−1)^(n−1)(n−1)!γ_n(x) are inverse group maps.',
  'The displayed manuscript logarithm has the opposite sign and is false literally; the corrected formula is stated separately as reconstruction.')
I('pd_log_reading',[83],'reading question','(−1)^n(n−1)!',
  'The logarithm begins with −x under the current transcription. Over Q[ε]/ε² it therefore sends exp(ε)=1+ε to −ε.',
  'Suggested exponent n−1; the mathematical counterexample does not decide whether the manuscript or transcription contains the error.',reason='The note’s sign alarm is confirmed by the square-zero test.')
I('pd_presentation_readings',[63,68,69,72,74,104],'reading question','Γ^n(xy)−x^nΓ^n(y)',
  'Raised exponents, ideal letters I/J, overwritten pushout domain and canceled multiplication need preservation. The side condition x∈I,y∈A puts the PD argument y outside its domain.',
  'The standard scalar relation uses x∈A,y∈I; this is a mathematical alternative, not an emendation.',reason='The sources explicitly distinguish live and canceled formulas; their domain alarm is valid.')
I('restricted_sites',[84,85,89],'unproved claim','cette rétraction n’entre pas dans la structure',
  'The PD site uses nilpotent truncated PD thickenings of opens, with Zariski coverings. A restricted variant requires existence of a local retraction without choosing one; formal smoothness is invoked to compare these topoi.',
  'Formal smoothness supplies local lifts, but the comparison must keep the ambient base and the locally retractive restriction fixed.')
I('restricted_sites_idea',[87,93],'idea of the earlier run','il existe une rétraction; les produits fibrés',
  'Earlier notes propose testing comparison and finite limits by explicit envelope/pushout constructions.',
  'These are leads. The manuscript’s doubt about finite limits is not a counterexample, and a chosen splitting is not extra site data.')
I('site_limits_question',[91],'self-flagged step','il semble douteux',
  'The page doubts existence of fiber products and equalizers in the proposed Cris/Strat object categories while affirming them in related categories.',
  'The exact object categories must be fixed; a modern crystalline-site statement is not automatically the same question.')
I('cech_nerve',[92,95],'unproved claim','couvre l’objet final; ind-représentable',
  'The local thickening object covers the final object; its powers are presented by a two-index filtered system of infinitesimal PD diagonal envelopes and truncations, giving a Čech spectral sequence.',
  'The colimit is a sheaf/ind-object, not a single representing finite scheme. Face/degeneracy maps and the distinction between levels i,j must be retained.')
I('local_cohomology',[97,99,100,101],'self-flagged step','à vérifier; si X est affine',
  'Localized crystalline-site cohomology is compared with Zariski cohomology of a thickening. The affine case is used for inverse-limit acyclicity and cosimplicial function complexes, then globally for Zariski hypercohomology.',
  'The modern PD and characteristic-zero completed-diagonal comparisons need their distinct hypotheses. A countable cofinal surjective system permits the intended affine inverse-limit step; arbitrary inverse limits are not exact.')
I('local_cohomology_idea',[98,102],'idea of the earlier run','varprojlim_(i,j)',
  'Earlier notes propose affine testing and checking a countable cofinal subsystem with surjective transition maps before suppressing Rlim terms.',
  'This is a valid conditional method. It does not identify every uncertain truncation map on these pages.')
I('site_readings',[86,88,94,96],'reading question','i:U→U′; E_2^(pq)',
  'Diagram direction U′→U versus prose immersion U→U′, cosimplicial index alternatives, missing tildes and an uncertain diagonal exponent remain reading questions.',reason='The notes retain graphical and prose evidence separately; no source category is changed to fit a diagram.')
I('p_typical_generators',[106,109,110,111,112],'conjecture','Quelles sont les relations?; On se demande s’il suffit',
  'Over a p-local ring, all divided powers are generated by p-power operations using p-unit digit coefficients. Whether the displayed adjacent-power relations and restricted addition relations suffice is left open.',
  'Generation, determination by γ_p and a complete list of defining identities are different assertions. Stacks23.5.3 settles a precisely stated γ_p extension criterion, not every corrupted presentation here.')
I('p_typical_carry_idea',[113],'idea of the earlier run','Γ^(p^ν)(x)^p',
  'Earlier notes suggest a digit-carry induction to derive multiplication relations from adjacent p-power relations.',
  'The induction must also prove addition and annihilator compatibility; it is not taken as a completed presentation theorem.')
I('principal_relations',[119,120,121],'conjecture','Les premières relations se réduisent, semble-t-il',
  'For a principal ideal (λ), generator operations must satisfy annihilator relations so γ_n(λx) depends only on λx. The p-local reduction and final boxed relation are tentative and heavily overwritten.',
  'The clean annihilator requirement (x^n−y^n)γ_n(λ)=0 whenever λ(x−y)=0 is identifiable; the final boxed simplification is not.')
I('principal_relation_ideas',[122,123],'idea of the earlier run','(x−y)λ=0; e=p+a',
  'Earlier notes propose substituting x=y+z with λz=0 and organizing the possible relation reduction by carries.',
  'Kept as a lead only. The uncertain final formula is not repaired into a conjecture for further proof.')
I('principal_relation_readings',[124],'reading question','ici | car',
  'The connector, factorial parenthesis and overwritten final boxed exponents/range need scans. They prevent a precise strongest version of the last relation.',reason='The note does not infer a finished claim from canceled draft material.')
I('ordinary_derham_examples',[130],'unproved claim','Lemme de Poincaré vrai',
  'The page lists characteristic-zero formal curve and finite local-algebra examples for a Poincaré lemma. It does not specify continuous versus algebraic differentials on formal series rings.',
  'For the positively graded finite monomial quotients, ordinary Kähler de Rham cohomology is k in degree0 and zero above. The formal-curve assertions need a separate definition and proof.')
I('local_m3',[131],'unproved claim','d_(A/k)x=0',
  'For a local k-algebra A with residue field k and char k=0, x∈m and dx=0 imply x∈m³; the Artinian hypothesis is canceled.',
  'An independent proof passes to A/m³, grades it using a complement to m² in m, and contracts by the Euler derivation.')
I('ordinary_derham_ideas',[133,134],'idea of the earlier run','k[x,y]/m²; ext. résiduelle triviale',
  'Earlier notes supply Euler contraction for graded examples and the A/m³ proof of the local kernel lemma.',
  'Both are independently proved here; exact quotient de Rham matrices check five finite examples only.')
I('ordinary_derham_counterexample',[135],'idea of the earlier run','Lemme de Poincaré vrai',
  'Earlier-run stress test: f=x⁵+y⁵+x³y³ and A=Q[x,y]/(f_x,f_y,(x,y)^7). Then A is local Artinian of dimension16, df=0, and f=y⁵/3≠0.',
  'The exact Gröbner calculation was rerun. This refutes an extrapolation to all ordinary Artinian de Rham complexes, not the listed graded examples or completed/derived comparisons.')
I('derham_biblio_reading',[132],'reading question','Ann. Éc. N. Sc.; J. de Liouville',
  'The journal/year alternatives give a bibliographical lead without an author or title. No exact publication is assigned from this shorthand.',reason='Kept as an unresolved identification, not a source citation.')
I('ega_normality',[136,137],'unproved claim','sans utiliser',
  'In the étale integral-closure argument, the reductions of EGA IV6.14.4 avoid the difficult theorem6.14.1; normality follows from17.5.7, and only elementary lemma6.14.1.1 remains.',
  'The exact published paragraph is EGA IV₄18.12.15, p.184. The canceled qualifier is not needed to identify the surviving dependency claim.',
  'The manuscript paragraph is an exact match to the published proof, including its qualified étale/noetherian reduction.')
I('ega_dependency_ideas',[138,139],'idea of the earlier run','sans utiliser; normal',
  'Earlier notes propose auditing the proof dependency graph and separating the ambient noetherian reduction from the étale normality step.',
  'The exact dependency paragraph has been located and read. A full reconstruction of all four referenced EGA proofs is not claimed.')
I('gamma_p_uniqueness',[140,141,142],'unproved claim','sont connus quand on connaît π_p',
  'All γ_n are determined by γ_p over a p-local ring. The two iteration orders have coefficients with valuations s_p(n)−1 and0 respectively, so the unit orientation must be used.',
  'The recursion n=pm+r,0≤r<p combines the unit iteration coefficient with a binomial coefficient prime to p; determination is distinguished from existence.')
I('gamma_p_recursion_ideas',[144,145],'idea of the earlier run','les π_n sont connus',
  'Earlier notes propose an explicit recursion and then separate tests of the admissibility axioms for a candidate γ_p.',
  'The uniqueness recursion is rechecked, and the existence problem is compared with the complete modern criterion.')
I('gamma_p_readings',[143,146,156,159],'reading question','x^iy^i; ν_p(c_n)',
  'Subscript versus raised operation labels, m/n in a valuation, mixed-term exponent i versus p−i and overwritten digit terms remain uncertain.',
  'Mixed terms must have total degree p for the usual γ_p identity; this dimensional test is not a reading of the missing ink.')
I('gamma_p_existence',[152,153,154,155],'conjecture','peut on définir; Est-ce tjs 1 ?',
  'A candidate p-th divided power with the displayed addition and scalar rules is proposed to extend to all divided powers. The digit formula has p-unit coefficients c_n=(p!)^(v_p(n!))/n!, but their reductions need not equal1.',
  'The exact criterion includes the p! relation, derivable from the proper addition/scalar rules as in Stacks23.5.4. At p=3,n=2, c_n≡2, answering the normalization question negatively.')
I('gamma_p_existence_ideas',[157,158],'idea of the earlier run','On va construire; Est-ce tjs 1 ?',
  'Earlier notes propose free-algebra identity checks and the n=2,p>2 normalization counterexample.',
  'The coefficient counterexample was recomputed exactly; a finite identity test is not substituted for the general extension theorem.')
I('kuiper_program',[147,148,149],'other','Professeur Nicolaas H. Kuiper',
  'A foreign course program lists Hilbert-manifold and infinite-dimensional topology results. GL(H) contractibility needs infinite dimension and the norm topology; the punctured-space analytic diffeomorphism and remaining headings need their own hypotheses.',
  'Illusie’s 1965 Bourbaki exposition verifies Kuiper’s norm-topology theorem for real, complex or quaternionic H. A course heading is not an original crystal theorem.')
I('kuiper_program_ideas',[150,151],'idea of the earlier run','Théorème de Bessaga; Théorie de Morse',
  'Earlier notes propose a hypothesis/reference table and tentative course dependency diagram.',
  'The dependency diagram is not asserted by the source. Only references actually located are treated as matches.')
I('course_k_theory',[160,161,162,163],'other','Coefficients locaux; the - complex',
  'Foreign K-theory and Kohn course fragments include Thom/Fredholm topics and nonelliptic differential complexes. Karoubi’s bibliography matches several cited CR volume/page pairs; the blank before “- complex” is not filled.',
  'Author identification is a bibliographical inference with exact matches, distinct from mathematical proof. Page347 versus published341 is a reading alarm.')
I('course_reference_ideas',[164,165],'idea of the earlier run','t.263; t.267; not elliptic',
  'Earlier notes propose resolving each CR page separately and comparing symbol failure with boundary-value problems.',
  'The bibliographical part has been checked against the author’s publication list. The analytical comparison is a lead, not a result of this run.')
I('polynomial_laws',[166,167,168,169],'conjecture','les t_i des indéterminées; réciproque',
  'A polynomial law yields multihomogeneous coefficient maps compatible with refinement and permutations; binary refinement implies arbitrary finite refinement by induction. Reconstruction additionally needs scalar extension/naturality, not just additive identities.',
  'Roby1963 IV1 and IV4 give the precise functorial formulation and homogeneous representability by Γ^n; the manuscript’s abbreviated converse is not assumed complete.')
I('polynomial_law_ideas',[171,172],'idea of the earlier run','deux termes; indéterminées',
  'Earlier notes propose the three-summand associativity test and evaluation on finite linear combinations after arbitrary scalar extension.',
  'These are checks of consistency/naturality; a single finite test does not prove the universal reconstruction.')
I('polynomial_law_readings',[170,173],'reading question','q_(1,i_2) | q_(2,i_2)',
  'Summation constraints, last index, decorated module symbols and arrow/dash alternatives affect the coefficient refinement formula.',reason='The note preserves the constrained-index uncertainty and page-edge loss.')
I('thom_fragment',[174,176],'other','Théorème1.1; une équivalence de catégories',
  'A foreign typed fragment states a Clifford-module Thom isomorphism and announces a spinor-bundle categorical equivalence whose target categories/functor continue beyond the page.',
  'The first is in Karoubi’s K-theory context. The unprovided final equivalence is not reconstructible solely from this leaf.')
I('spin_sequence',[175],'unproved claim','x*x=1',
  'The norm-one even Clifford group is claimed to give a central double cover of SO(p,q). With the literal real indefinite convention this misses components.',
  'For (p,q)=(1,1), norm-one a+b e_1e_2 gives boosts with diagonal a²+b²≥1; −I∈SO(1,1) is absent. Restrict the target component or specify a different group convention.')
I('spin_ideas',[178,179],'idea of the earlier run','e_i*=−e_i',
  'Earlier notes propose checking Clifford signs and the image of Spin before applying a principal-bundle lift, then testing the missing equivalence locally.',
  'The real (1,1) image test was carried out. The gluing proposal is deferred because the claimed categories are absent.')
I('spin_readings',[177,180],'reading question','v_1 cos+ε^i sinθ; type(q,p)',
  'Missing θ, swapped signatures, epsilon forms and zero endpoints in a group exact sequence are retained literally.',reason='Convention and typographical alarms do not license repairing the source formula.')
I('principal_pd_construction',[181,182,185],'unproved claim','J=πA; sans ambiguïté',
  'A normalized sequence π^[n] already lying in πA, satisfying multiplication and iteration, defines γ_n(πy)=π^[n]y^n. Membership in πA kills annihilator ambiguity. The canonical sequence for π=p is p^n/n!.',
  'If πz=0 and c∈πA, then c((y+z)^n−y^n)=0. Addition, homogeneity and iteration must then be checked with the stated identities.')
I('principal_pd_bad_criterion',[184],'unproved claim','leur existence équivaut',
  'The torsion-free example asserts that existence of PD on (π) is equivalent to π^n∈n!A. This is too weak: the divided powers must belong to (π).',
  'Correct torsion-free criterion: π^n/n!∈πA for all n≥1. The finite free Z-algebra x²=2y,xy=y²=0 gives a fully checked counterexample to ring-membership sufficiency.')
I('principal_pd_ideas',[186,187],'idea of the earlier run','πz=0',
  'Earlier notes isolate representative independence and propose checking the remaining axioms after it.',
  'The binomial annihilator argument is re-proved here, with the assumption π^[n]∈πA kept explicit.')
I('principal_pd_counterexample',[188],'idea of the earlier run','π^n∈n!A',
  'Earlier-run counterexample A=Z1⊕Zx⊕Zy, x²=2y,xy=y²=0, π=x. All π^n/n! lie in A, but γ_2(x)=y∉xA.',
  'Associativity, torsion-freeness, every n≥3 and the principal ideal are checked in the independent proof and exact code.')
I('principal_pd_reading',[183],'reading question','π^(n)z^n',
  'The representative-independence equation inside the canceled block and its unfinished endpoint remain abandoned draft text.',reason='The note does not use the canceled expression as an axiom of the surviving construction.')
I('dvr_pd',[194,196,198],'conjecture','À quelle condition peut-on trouver des; e≤p−1',
  'For a mixed-characteristic DVR with uniformizer π and v_π(p)=e, the maximal ideal admits its unique divided powers exactly when e≤p−1. On V/(π^m), m>1, the structure induced from V is PD nilpotent exactly when e<p−1.',
  'The general integral-ring question is wider. The DVR result follows from the exact valuation n−e v_p(n!) and is BO1978 Proposition3.28.')
I('finite_target_differentials',[189,199,200,201,205],'unproved claim','intersection des noyaux des homomorphismes',
  'For semilocal noetherian B with its radical-adic topology, derivations to finite B-modules are continuous. The quotient of Ω^1_(B/A) by kernels of all maps into finite modules retains these Hom functors; if finite itself, it represents derivations in the finite-module category.',
  'EGA0_IV20.4.5 and20.4.8 justify the topology and continuous universal property under broader conditions. They do not assert finite generation of this quotient or identify it with completion.')
I('analytic_transitivity',[190,193],'unproved claim','topologies préadiques',
  'Draft18.13.5 asserts finite-generation implications and transitivity maps for the finite-target differential quotients, with an extra ordinary-Ω finite-generation hypothesis in one branch.',
  'The displayed bottom sequence has no completed proof here. EGA0_IV20.7.17 warns that completed transitivity need not be exact and is only a comparison, not the same quotient construction.')
I('finite_target_ideas',[203,204],'idea of the earlier run','Prendre un anneau topologique plus général ?',
  'Earlier notes compare the finite-target quotient with separated/completed differentials. For B=k[[t]], finite-target derivations are D(f)=f′(t)D(t), so the quotient is Bdt.',
  'The power-series calculation follows from continuity and separated finite modules; no global identification for arbitrary topological rings is claimed.')
I('analytic_order_readings',[191,192,202],'reading question','co-; ïncide; style ambigu',
  'Typescript scan048 (page22) precedes046 (page23), joined by co-ïncide. Draft18.13.4–5 has not been identified with an identically numbered published passage; deletion of uniqueness is only a local editorial fact.',reason='The local order follows two independent transcript anchors, without reordering or filling missing text.')
I('etale_duality',[207,208,209,211],'conjecture','éviter tout recours au théorème de pureté relative',
  'The 10December1965 letter proposes relative/global étale duality for a compactifiable smooth morphism and a morphism of torsion coefficient ring sheaves, with n invertible, a relative dimension twist/shift, and internal Hom over the target coefficients.',
  'The general coefficient form and the proof avoiding purity are distinct from the constant Z/n case; the author doubts that the latter alone implies the former.')
I('duality_readings',[210],'reading question','On définit alors',
  'Blank arrows, missing shift brackets/inequality and uncertain dimension notation in the typed duality formula require the scans or an exact letter edition.',reason='The note preserves the gaps rather than silently supplying a full six-functor identity.')
I('naive_padic_comparison',[212,214,215,219,220],'conjecture','un excès d’optimisme; j’ai de grands doutes',
  'The letter explores a constant-Z_p/de Rham comparison and an ordinary rigid analytic Poincaré lemma, then immediately doubts them and recalls an unverified Tate elliptic objection. A “true” p-adic cohomology remains a hope.',
  'Modern continuous étale and period-sheaf comparisons are precise successors, with different coefficient sheaves and sites; they do not prove the literal constant-sheaf proposal.')
I('analytic_etale_comparison',[213],'conjecture','On espère que les arguments habituels prouveront',
  'The letter expects torsion étale cohomology of an algebraic variety to compare with its rigid analytification.',
  'The analytic site, coefficient class and properness/finiteness hypotheses must be fixed. The exact unrestricted phrase on this page is not treated as a theorem.')
I('padic_comparison_ideas',[216,217,218],'idea of the earlier run','coéfficients constants Z_p',
  'Earlier notes separate lim torsion cohomology from the ordinary discrete constant Z_p sheaf, and propose a Galois-compatible Hodge–Tate obstruction.',
  'For a connected elliptic curve over an algebraically closed characteristic-zero field, H¹_et(E,Z_p discrete)=0 while lim H¹_et(E,Z/p^n)=Z_p². Finite Mittag–Leffler does not erase this distinction.')
I('frob_derham',[222,223,227],'unproved claim','homomorphisme de Frobenius',
  'The characteristic-p pages factor Frobenius through the de Rham complex and discuss closed functions. On a smooth scheme over a perfect field the correct statement uses relative Frobenius and the Frobenius twist; without smoothness/perfectness it is not an isomorphism onto closed functions.',
  'F_p[x] has H⁰_dR=F_p[x^p] and H¹_dR=F_p[x^p]x^(p−1)dx. On F_3[ε]/ε², Frobenius kills ε although dε≠0. These are tests, not new ink readings.')
I('frob_derham_idea',[229],'idea of the earlier run','homomorphisme de Frobenius',
  'Earlier notes make the chain maps O[0]→Ω•→O[0] explicit; their composite is Frobenius as F_p-linear sheaf maps.',
  'The chain-map identity holds even when the first map is not an isomorphism; the necessary twist for O-linearity is retained.')
I('true_padic_cohomology',[221,228],'conjecture','Il reste plausible néanmoins; vraie cohomologie p-adique',
  'After doubting the ordinary constant-sheaf mechanism, the author retains a role for rigid topology and a still unspecified true p-adic cohomology.',
  'This broad expectation is recorded separately from the definite Poincaré proposal; it cannot be identified uniquely with one later theory.')
I('tate_recollection_idea',[224],'idea of the earlier run','un peu plus que pour la cohomologie étale',
  'The earlier run suggests that the recalled Tate objection might compare discrete constant coefficients rather than the adic inverse-limit groups.',
  'This is a possible interpretation only. Tate’s missing argument and intended analytic curve have not been recovered.')
I('scholze_comparison_note',[225],'unpursued implication','lemme de Poincaré',
  'The earlier notes compare the hoped-for lemma with Scholze’s period-sheaf Poincaré sequence and proper smooth B_dR comparison.',
  'The exact later theorem is kept as a comparison point: complete discretely valued base with perfect residue field, proper smooth rigid space, pro-étale period coefficients. It is not the original constant-sheaf assertion.',
  'The earlier note explicitly states the coefficient/site change, and the cited author-version theorem and corollary have been read.')
I('frob_nonreduced_idea',[226],'idea of the earlier run','évident',
  'The earlier run tests the closed-function assertion on F_p[ε]/ε², p>2: H⁰_dR=F_p, and Frobenius on O is not injective.',
  'The exact calculation is rerun and shows a missing reducedness/smoothness hypothesis; it does not change the uncertain O/Ω reading.')

# Cote 6, scans1–37.
I('crystal_project',[230,231,232,233],'conjecture','projet de théorie; une section cartésienne',
  'The Pisa letter proposes crystals as cartesian sections over nilpotent thickenings in a variable fibred category, with tensor operations transported by cartesian functors.',
  'This first definition is explicitly preliminary. A later repair uses opens and requires a Zariski stack; arbitrary fibred categories do not automatically have descent.')
I('pisa_verso',[234],'title, date or page count','UNIVERSITÀ DI PISA',
  'The letterhead face with folio2 is not a second mathematical letter passage. The notes distinguish reverse show-through from writing on the face.',
  'No scans are available to recheck the physical diagnosis; the transcription contains letterhead and foliation only.',reason='The transcript supports absence of a second body text; physical show-through remains an inherited observation, not a fresh image inspection.')
I('global_pushout_retracted',[235,236,240,340,341,342],'withdrawn in the same text','construction évidente de somme amalgamée; Un retour en arrière',
  'The claimed inverse-image construction using global pushouts of schemes is revised in §1.16: the pushout can leave schemes, so one uses nilpotent thickenings of varying opens and requires stack descent.',
  'Scans004 and017 are read together. The local repair, not the original global formula, is the supported basis for later functoriality.')
I('evaluation_nonfaithful',[237,241,242,247,248,291,292],'unproved claim','n’est pas fidèle; module de type fini',
  'At a perfect characteristic-p field the proposed finite crystal category is modeled by finite W(k)-modules or compatible p-adic systems, with evaluation given by reduction modulo p and Frobenius pullback by the Witt automorphism.',
  'For modern PD crystals this model is precise. Ordinary absolute crystals require the source’s coefficient-lifting hypotheses and local definition; mod-p evaluation is certainly not faithful in the W-module model.')
I('evaluation_test_ideas',[239,243,253],'idea of the earlier run','valeur en S',
  'Earlier notes test nonfaithfulness by multiplication by p on W(k), which is nonzero before evaluation and zero on k.',
  'This is an exact conditional counterexample once the W-module equivalence has been specified.')
I('charzero_field',[238],'unproved claim','supposons k algébrique sur Q',
  'The inserted algebraicity-over-Q restriction belongs to the characteristic-zero point example; it is not a restriction on the perfect characteristic-p case.',
  'A formally étale algebraic extension of Q has unique nilpotent lift behavior. Arbitrary characteristic-zero fields can have nonzero differentials over Q.')
I('etale_completion_examples',[244,246,249],'unproved claim','objet final; d’où on conclut facilement',
  'For an étale S/R, the identity has a unique extension over nilpotent thickenings, so the relevant category has a final object. For a closed immersion into a noetherian ambient scheme, its infinitesimal neighborhoods are cofinal and coherent crystals correspond to compatible coherent formal data. The unramified case is local.',
  'Formal-completion equivalence needs noetherian/coherence hypotheses; an arbitrary unramified morphism is not globally a closed immersion.')
I('completion_reading',[245],'reading question','voisinage infinitésimal de R dans S',
  'The phrase reverses the preceding closed immersion S⊂R. The displayed V(J^(n+1)) is an infinitesimal neighborhood of S in R.',reason='The reading is retained and the direction alarm is registered separately.')
I('stratification_definition',[250,251,252,254],'unproved claim','pseudo-stratification; la diagonale de',
  'Compatible infinitesimal identifications become a stratification only with a cocycle on the triple diagonal. Formally unramified morphisms have trivial finite diagonals and unique such structures; evaluation need not be faithful for absolute crystals.',
  'The canonical stratification records horizontal nilpotent variation, not all mixed-characteristic lifting data.')
I('smooth_crystal_strat',[255,256,258,259],'conjecture','formellement lisse; je n’ai pas écrit',
  'The crystal/stratification equivalence is asserted for formally smooth maps. Its extension to flat locally finitely presented maps, removal of smoothness in the connection comparison, and analogues for arbitrary fibred categories are explicitly open or unwritten.',
  'Published smooth ordinary and smooth PD comparisons settle restricted cases. They do not settle the arbitrary fibred-category or singular version on these pages.')
I('cartier_frobenius',[260,261,264,265],'unproved claim','connexion sans torsion; Il y a loin de là',
  'For a smooth characteristic-p morphism, zero p-curvature integrable connections descend along relative Frobenius. A stratification involves compatible successive Frobenius descents, not a single such descent.',
  'The identification of “sans torsion” with zero p-curvature is the modern comparison, not a new ink reading. Katz1970 Thm5.1 and Gieseker1975 Thm1.3 have different hypotheses/categories.')
I('frobenius_descent_idea',[262],'idea of the earlier run','Il y a loin de là',
  'Earlier notes propose iterating Cartier descent with coherent comparison isomorphisms to reconstruct all higher stratifications.',
  'The smooth-field locally free result is Gieseker/Katz; it does not apply to an isolated arbitrary integrable connection.')
I('charzero_counterexample_idea',[267],'idea of the earlier run','tenseur courbure',
  'Earlier-run test over Z[x]: the rank-one integrable connection ∇e=e dx has rational Taylor coefficients1/n! and cannot extend to an integral stratification already at order2.',
  'The obstruction is re-proved; it diagnoses the need for a Q-base rather than broad “characteristic zero”.')
I('modular_obstruction_comparison',[266],'unpursued implication','Il y a loin de là',
  'The earlier notes connect the warning to Grothendieck’s published modular-elliptic H¹ de Rham obstruction to an ordinary stratification compatible with all base changes and endomorphisms.',
  'The precise published result is §3.5,p.330 (1968; lectures1966); it concerns ordinary stratifications, not PD crystals.')
I('absolute_base_change',[268,303,304],'unproved claim','cela reviendrait au même; il est inoffensif de se localiser',
  'For characteristic-p schemes and nilpotent thickenings, the text compares absolute Z, Z_p and W(k) constructions, then localizes on the special scheme before lifting smooth affines.',
  'Z→Z_p factorization uses p-nilpotence. A W(k)-structure uses perfectness and the source’s coefficient-lifting statement; localization relies on the corrected stack definition.')
I('dieudonne_families',[269,270,271,272,274,275,277],'conjecture','devrait permettre; semble tout à fait adéquate',
  'The author proposes algebraic families of Witt and Dieudonné modules: an F-crystal initially means a morphism F:M^(p)→M, without invertibility or a height bound; adding V and FV=VF=p is meant to capture p-divisible groups and H¹.',
  'Established Dieudonné-crystal classification uses PD sites, finite locally free objects and specified base hypotheses. It is not a classification by all unrestricted F-crystals.')
I('integral_dual_idea',[273],'idea of the earlier run','définir le',
  'For M=W/p, the W-dual is0 while the dual after evaluation over k is k. Earlier notes use this to show why ordinary duals do not commute with arbitrary crystal base change.',
  'The calculation is exact. Dualizability requires finite locally free hypotheses, not finite type alone.')
I('fv_readings',[276,278,293,297,339],'reading question','VF=id; bicristal de Tate de poids1; motif',
  'The first relation FV=p,VF=1 conflicts with the later symmetric weight-i formula. F=V=p^i has product p^(2i), while a nearby sentence retains weight1. “Motif” is only local terminology; characteristic zero may mean a Q-scheme.',
  'FV=VF=p and the later symmetric formulas suggest corrections, but the current ink readings remain unchanged.')
I('isogeny_rationalization',[279,283,284,285,286,288,294,295,298],'unproved claim','nouveaux Hom; pleinement fidèle',
  'Finite perfect-field modules with symmetric FV=VF=p^i pass to finite-dimensional isocrystals; after p is inverted V=p^iF^−1 is determined. Fixed-weight forgetting is fully faithful on the appropriate finite category, and dual F is transpose inverse with the Frobenius twist.',
  'Identifying a Q-linearization with a quotient by torsion needs uniformly p-power-killed torsion in the finite setting. Integral Cartier duality of finite groups and rational vector-space duality are distinct.')
I('unbounded_torsion_idea',[280],'idea of the earlier run','objets de',
  'Earlier notes test an unrestricted quotient assertion using M=⊕_(n≥1)W/p^n: M is torsion but id_M is killed by no fixed p-power, so survives End(M)⊗Q.',
  'This is an abstract W-module counterexample to dropping finiteness/uniformity. It is not represented as an object of every completed crystal category.')
I('rational_operator_ideas',[281,289],'idea of the earlier run','bi-cristal de poids; objets de type fini',
  'Earlier notes derive V=p^iF^−1 and the dual formula F∨(λ)(m)=σ(λ(F^−1m)) for finite-dimensional K-spaces over a perfect residue field.',
  'The semilinearity and pairings are rechecked. The formula does not repair the earlier asymmetric relation on the page.')
I('h1_dieudonne',[282,372,375],'conjecture','C’est bien celui défini par Dieudonné',
  'The proposed H¹ de Rham/crystalline invariant of an abelian scheme is to recover the Dieudonné module of its p-divisible group, rather than only its connected formal group.',
  'Oda1969 Cor5.11 proves the perfect-field mod-p comparison with the Dieudonné module of p-torsion. Messing’s crystalline construction gives the stronger integral framework under its stated PD conditions.')
I('effective_lattices',[290,299,300,301,302],'unproved claim','c’est une pure tautologie; il faut et il suffit',
  'At a finite-dimensional perfect-field point, bounded orbits under F and V=p^iF^−1 are equivalent to a common stable lattice. Some weight i exists exactly when positive F-orbits are bounded; after a sufficiently large Tate scaling, any invertible F becomes effective.',
  'The noetherian lattice proof is supplied explicitly. The “tautology” is not immediate without finite rank; extension from a point to a family requires uniform bounds.')
I('lattice_ideas',[287,296,305,306,307,308],'idea of the earlier run','pour tout; on n’a pas ajouté plus de nouveaux objets',
  'Earlier notes give the finite-basis bounded-orbit lattice argument, clearing denominators for V, and scaling F by p^a; they also warn that a whole family may lack a single uniform bound.',
  'The pointwise arguments are independently proved. No general family theorem is inferred from these finite-dimensional proofs.')
I('nilinvariance_lifts',[309,310,312,316],'unproved claim','il résulte encore facilement des définitions',
  'The corrected ordinary infinitesimal crystal category is asserted invariant under nilpotent thickening. Smooth affine schemes admit compatible lifts, and stratifications on a lift describe crystals independently of that lift.',
  'Ordinary nil-invariance, PD crystalline nil-invariance and a smooth PD-envelope comparison are different statements. BO’s quasi-nilpotent connection equivalence does not justify a broad ordinary-to-PD identification.')
I('proper_algebraization',[311,317],'unproved claim','hypothèse évidemment bien restrictive',
  'Assuming an actual proper lift X over complete noetherian W, formal coherent modules and their compatible higher stratification maps algebraize.',
  'Proper coherent existence applies also to finite infinitesimal diagonal neighborhoods, so maps and cocycles can be algebraized. Mere formal existence of a proper scheme is not automatic.')
I('algebraization_ideas',[315,318],'idea of the earlier run','restriction; hypothèse évidemment bien restrictive',
  'Earlier notes propose algebraizing each finite-order comparison map on the proper diagonal neighborhoods, then using full faithfulness for the cocycle identities.',
  'This conditional argument is checked. It does not prove that every connection on the generic fiber has an integral higher stratification.')
I('stratified_local_freeness',[314,333,334],'conjecture','nécessairement localement libre; Il est bien probable',
  'The pages assert local freeness of coherent ordinary stratified modules over locally finite-type field schemes and noetherianity of coherent crystal categories, then question how much survives without smoothness.',
  'BO1978 Proposition2.16 and Note2.17 prove local freeness of coherent ordinary stratified modules for arbitrary finite-type schemes over a field, without smoothness. Arbitrary PD crystals and broader noetherian-category assertions remain separate.')
I('local_freeness_test_idea',[319],'idea of the earlier run','nécessairement localement libre',
  'Earlier notes exhibit k[x]/(x^p) with its derivation d: it is coherent with zero p-curvature but not locally free.',
  'This refutes a connection/PD-category overgeneralization, not local freeness of full ordinary stratifications; no full stratification is supplied on this module.')
I('proper_monodromy',[320,321,322,328],'conjecture','approche transcendante; on conclut par descente',
  'Under a proper smooth lift and an embedding of its characteristic-zero fraction field into C, the author uses complex monodromy to predict constancy when the relevant fundamental group is trivial, then proposes descent and application to formal-group families.',
  'Riemann–Hilbert controls the complex proper connection. Descent and the integral essential image require separate arguments; the positive-characteristic crystalline category is not identified with arbitrary complex local systems.')
I('generic_essential_image',[313,323,324,325,326,329,330,331,332],'conjecture','image essentielle; trop optimiste; un groupe plus ou moins discret',
  'The proposed functor from coherent isocrystals on the special fiber to generic-fiber stratified modules/connections is asserted fully faithful; essential surjectivity is questioned and called too optimistic. A local essential-image condition and an analogue of a fundamental group for rigid connections are requested.',
  'Formal lift, actual proper algebraic lift and rigid generic fiber are distinct contexts. Modern convergence, quasi-nilpotence and Frobenius-divided conditions give different full subcategories; no single unrestricted equivalence follows.')
I('essential_image_idea',[327],'idea of the earlier run','image essentielle',
  'Earlier notes propose testing integral Taylor operators and denominator growth separately for algebraic proper and formal generic-fiber comparisons.',
  'The proposal is retained as a research direction, not an established essential-image characterization.')
I('frobenius_lift',[335,336,337],'unproved claim','ne dépend pas, essentiellement, des choix faits',
  'On a smooth affine formal lift, relative Frobenius can be lifted successively. Stratifications identify pullbacks for two such lifts, compatibly with composition.',
  'Smoothness, affineness and the compatible base Frobenius are required; independence is by canonical comparison isomorphisms, not equality of chosen lifts.')
I('all_prime_structure',[338],'unpursued implication','d’une nature essentiellement arithmétique',
  'One crystal is proposed with separate weight-i F_p,V_p structures on the fibers at every prime.',
  'No compatibility between different primes or realization theorem is specified. It is a programmatic arithmetic object, not a proven theory of motives.')
I('local_site_definition',[343,345,346],'unproved claim','site cristallogène; Modules quasi-cohérents',
  'The corrected site uses nilpotent thickenings of opens and open coverings of their targets. Sheaves have comparison maps for all morphisms, invertible for open restrictions; a crystal requires all cartesian comparison maps to be invertible. Quasi-coherent modules and local finite presentations are then compared with crystals.',
  'The sheaf/crystal distinction is essential. The page’s topos functoriality is only partially constructed and is compared with the published infinitesimal site.')
I('local_site_idea',[344],'idea of the earlier run','un ouvert induit non précisé',
  'Earlier notes propose a two-affine-open descent test of the repaired local construction against the original global-arrow definition.',
  'This is kept as a test plan. It is not an executed counterexample to a particular global pushout.')
I('ordinary_cohomology_retracted',[347,348,351,352,354],'withdrawn in the same text','on voudrait trouver; une hypothèse ou un voeux pieux',
  'The author hopes ordinary crystallogenic-site structure-sheaf cohomology recovers de Rham and its relative Gauss–Manin object, then marks failure in characteristic p and suggests deriving in quasi-coherent crystals or passing to isocrystals.',
  'The later PD theory is a replacement of the site. It does not validate the unrepaired ordinary characteristic-p proposal.')
I('cohomology_site_ideas',[350,356],'idea of the earlier run','puiss. div.; seuls Modules quasi-cohérents',
  'Earlier notes propose comparing the ordinary and PD sites on a smooth affine and comparing all-module versus quasi-coherent derived constructions.',
  'The A¹ characteristic-p de Rham calculation is executed; the unrestricted derived-category comparison remains a lead.')
I('gauss_manin',[349,355,357,358,359],'conjecture','nullité de la courbure; interprétation purement algébrique',
  'The author reports a Gauss–Manin connection for smooth morphisms, asks for algebraic integrability and an algebraic construction of the entire Leray spectral sequence, and notes that ordinary characteristic-p stratification cannot always result.',
  'Katz–Oda1968 Theorem1 proves the canonical integrable connection for smooth X/S and smooth S/k; Theorem3 and its addendum identify the de Rham Leray spectral sequence. The ordinary-stratification obstruction remains distinct.')
I('gauss_manin_readings',[360],'reading question','C_(S^an)',
  'The analytic Leray display appears to place the constant sheaf on the target while the direct image has source X. The source/target of the coefficient needs an ink check.',reason='This is a type alarm, not a reconstruction of missing spectral-sequence notation.')
I('monsky_program',[353,365,398],'unpursued implication','des dénominateurs; calcul-clef',
  'The author associates Monsky–Washnitzer invariance with denominators and wants a nonproper theory, but deliberately does not formulate it here. Later he proposes examining its key calculation to find the needed enlargement of ordinary crystals.',
  'Overconvergent de Rham/rigid cohomology is a precise later framework. The page alone neither defines it nor proves its independence of choices.')
I('derived_crystalline_program',[361,362,363,364,366],'conjecture','voilà la théorie qu’on voudrait',
  'For proper smooth f, the author requests a perfect derived crystalline object, arbitrary derived base change, functoriality, Künneth and duality with Tate twist/shift2d, compatible with de Rham comparison; Frobenius is then extracted conditionally by functoriality.',
  'The ordinary-site formulation is not silently replaced by modern PD cohomology. BO’s specified flat-coefficient derived comparison and base change settle a precise successor, not every individual cohomology base-change claim.')
I('frobenius_duality_weights',[367,369,370,371],'withdrawn in the same text','je m’étais canulé',
  'The pages propose constructing V by duality and assert FV=VF=p^(2d); they predict individual rational base change and then withdraw automatic integral weight-i bicrystals, recognizing the need for a polarization/Lefschetz isomorphism up to isogeny.',
  'Frobenius normalization on top de Rham/crystalline cohomology must be checked separately from Tate’s stated weight2d. Derived base change alone does not imply arbitrary base change on each H^i.')
I('frobenius_target_reading',[368],'reading question','X_p^(p/S)→X',
  'The relative-Frobenius source base and target in the display are inconsistent with the neighboring S_p notation unless a composite is intended.',reason='The note preserves the literal target and requests a separate type check.')
I('h1_lift_independence',[373,374,377],'withdrawn in the same text','pas du choix du prolongement; Je n’ai pas vérifié',
  'The first two abelian assertions posit a canonical locally free rank2g H¹ evaluation independent of an abelian lift across arbitrary nilpotent thickenings, with gluing after removing affineness. They are explicitly unverified and later retracted in that generality.',
  'Modern H¹ crystalline/de Rham comparison uses a specified nilpotent PD base. Canonical invariance on arbitrary ordinary thickenings is not restored by citing Messing.')
I('hodge_deformation',[378,379,380],'conjecture','est une équivalence de catégories',
  'The third abelian assertion proposes equivalence between lifts and locally free Hodge filtrations/quotients lifting the canonical one, while stressing that the filtration itself is not crystalline.',
  'Grothendieck–Messing gives the precise p-divisible-group equivalence over locally nilpotent PD thickenings with p locally nilpotent, and Serre–Tate supplies the abelian bridge. Those hypotheses are essential.')
I('hodge_idea',[381],'idea of the earlier run','pas de nature cristalline',
  'Earlier notes separate the canonical underlying crystal from a variable Hodge filtration and propose checking composition through successive nilpotent extensions.',
  'The distinction is retained; the run reads Messing’s admissibility hypotheses rather than asserting a proof for all thickenings.')
I('abelian_word_idea',[376],'idea of the earlier run','multiplicatif; foncteur additif',
  'Earlier notes suggest checking whether a canceled adjective concerns compatibility with products, while keeping it separate from the later additive-functor assertion.',
  'This remains an interpretive reading lead, not a mathematical new property.')
I('motivic_variation',[382],'conjecture','refléter fidèlement',
  'The varying Hodge filtration is expected to reflect variation of the underlying motive; the author explicitly says the foundations are not yet firm enough for a theorem.',
  'No precise category, faithfulness quantifier or realization functor is supplied. Modern filtered theories are context, not a match to an unidentified claim.')
I('serre_tate_deformation',[383],'unproved claim','pareil qu’étendre le groupe p-divisible correspondant',
  'For p-nilpotent bases with a nilpotent thickening, deformation of an abelian scheme is equivalent to deformation of its p-divisible group together with the special-fiber identification.',
  'The criterion is Serre–Tate, not equivalence with an arbitrary Hodge filtration. Katz1981 Thm1.2.1 and MessingV2.3 state the exact deformation category.')
I('universal_extension_abelian',[384,385,387,388,390],'unproved claim','universelle parmi les extensions; et même unique',
  'Universal vector extensions of abelian schemes are proposed to be functorial and base-change compatible, with Lie sequence dual to Hodge. The text further claims lift-independent smooth group crystals and recovery of a lifted abelian scheme by quotienting a lifted vector subgroup.',
  'Existence of universal extensions is established separately from the overstrong group-level ordinary crystal and Lie-submodule-to-subgroup assertions. Characteristic-p vector subgroups are not determined merely by tangent submodules.')
I('extension_readings',[386,410],'reading question','où A est le schéma abélien dual de A; imposer la variation infinitésimale',
  'Missing dual stars and S/T base notation in the extension sequence affect the Hodge duality. The final phrase literally says variation, not non-variation.',reason='These are explicitly retained reading alarms; familiar formulations are not inserted into the text.')
I('manin_picard_fuchs',[389],'unpursued implication','simplifier la construction de Manin',
  'The author traces his universal-extension/derivative construction to an attempt to simplify Manin’s Picard–Fuchs construction.',
  'This is internal motivation. The missing differential operator and unprovided exact bibliographical citation are not inferred from the allusion.')
I('manin_derivative_idea',[391],'idea of the earlier run','déterminé modulo',
  'Earlier notes propose expressing the derivative class in a quotient of a twisted de Rham complex and identifying an operator or functional giving the proposed function.',
  'Kept as a lead; no Picard–Fuchs operator is constructed in these pages or in this consolidation.')
I('group_rigidity_revisions',[392],'withdrawn in the same text','que j’ai vérifiés; faux; à vérifier',
  'In §2.6 the claimed lack of infinitesimal automorphisms is marked false; the first-order assertion is separately marked for verification and possibly false.',
  'The initial “verified” sentence does not override the later local annotations. The two claims retain distinct uncertain statuses.')
I('modular_counterargument',[393,394],'withdrawn in the same text','elles sont fausses telles quelles',
  'The abelian hopes are retracted as stated. On a modular elliptic family, naturality of ordinary stratification and Frobenius would propagate F²=0 from a supersingular fiber, contradicting neighboring ordinary fibers.',
  'Grothendieck1968 §3.5 is an exact published match with smooth integral modular-base hypotheses. It refutes universal ordinary stratification compatible with endomorphisms/base change, not the PD Gauss–Manin crystal.')
I('modular_propagation_idea',[395],'idea of the earlier run','grimpant sur les voisinages',
  'Earlier notes propose separating formal-neighborhood propagation from passage to nearby points, with finiteness and regularity explicit.',
  'The published argument was read and its scope checked; no blanket propagation theorem on singular/nonnoetherian bases is asserted.')
I('modular_regular_reading',[396],'reading question','S_rég; régulier',
  'The source has rég, not réd, and a revised dimension bound. Both the regularity condition and the negative marginal annotations must survive consolidation.',reason='The note protects a mathematically significant literal distinction.')
I('ordinary_retreat',[397,399,400,402,403,404,405,407,408,409],'withdrawn in the same text','Faux; jamais; Il n’est pas exclu entièrement',
  'The pages cancel an ordinary-case lifting-independence conjecture and a purity extension argument, then leave a narrower everywhere-ordinary positive-characteristic possibility with acknowledged Frobenius and arithmetic gluing gaps. The provisional “too fine” diagnosis concerns the current ordinary crystal definition.',
  'The blanket negative margin and canceled block are not a final theorem that every ordinary family fails. PD crystals and canonical Serre–Tate lifts address different assertions.')
I('ordinary_retreat_ideas',[401,406,411],'idea of the earlier run','relèvements canoniques; provienne d’un cristal',
  'Earlier notes separate canonical lift selection from all-lift independence, and separate connection, higher stratification, arithmetic extension and Frobenius compatibility.',
  'These distinctions are retained. The hypothetical arithmetic gluing and purity arguments are not accepted as proofs.')
I('bt_universal_extension',[412,413,414,415],'conjecture','je n’ai pas essayé de tirer au clair',
  'For p-divisible groups the author seeks a universal extension, its Lie Hodge sequence and base change, while leaving the additive formal coefficient object and complete versus first-order independence unsettled.',
  'Messing’s universal vector extension/crystal makes a precise construction with a specified coefficient category. Group-cohomological H² is not automatically the same as the requisite extension functor.')
I('bt_extension_idea',[416],'idea of the earlier run','le groupe formel associé',
  'Earlier notes propose fixing the additive coefficient formal group and comparing the proposed cohomology with Ext before testing deformation claims.',
  'This is a well-posed prerequisite, retained as a lead rather than a completed identification.')
I('adic_bt_deformation',[417,418],'conjecture','par passage à la limite; entièrement équivalente',
  'The extension invariant is asserted to persist over a separated complete noetherian adic ring, and a special residual p-divisible group is expected to have lifts classified by its lifted filtration over a complete DVR.',
  'Passing through finite quotients needs effectiveness. Grothendieck–Messing applies at PD-nilpotent stages; arbitrary ramification without compatible PD structure is not covered.')
I('recover_tate',[419,420],'conjecture','Il serait bien intéressant d’essayer de déterminer',
  'Recover the generic-fiber Tate module from lifted filtered Dieudonné data and determine how much information the universal-extension invariant retains for more general p-divisible groups.',
  'A rational filtered isocrystal and an integral Tate lattice differ. Modern prismatic classification supplies a stronger integral invariant, under its precise quasisyntomic/admissibility hypotheses.')
I('elliptic_cover',[421],'title, date or page count','Réduction des courbes elliptiques',
  'A sparse heading and reference to Serre’s Abelian l-adic representations introduce the elliptic notes without proving a claim.',reason='The entry is documentary; the named book is a lead rather than an automatically checked source for the following pages.')
I('ordinary_elliptic_extension',[422,423,424,427,428,429,436],'unproved claim','bien ramifié; exponentiation',
  'For good ordinary elliptic reduction over a complete mixed-characteristic DVR, T_p(E) has the canonical extension 0→L∨(1)→T_p(E)→L→0 with L unramified rank1; the class lies in H¹(K,L^−2(1)). After trivializing L in the strictly henselian case, Kummer gives a parameter, with a square-unit change of basis.',
  'Identifying the Kummer unit kernel with principal units uses perfect/algebraically closed residue hypotheses, not separable closedness alone. Canonical lift corresponds to the split parameter only in the precise Serre–Tate setting. The unfinished equal-characteristic continuation in note436 is retained separately and is not asserted to satisfy this mixed-characteristic description.')
I('ordinary_recovery_idea',[426],'idea of the earlier run','L^−2⊗T_p(G_m)',
  'Earlier notes recognize the ordinary extension class as a concrete test of the filtered-invariant-to-Tate-module recovery question.',
  'The comparison is local to ordinary elliptic curves and does not solve general filtered integral reconstruction.')
I('ordinary_parameter_readings',[425,435,437],'reading question','T_p(K); L^−2⊗',
  'The Kummer denominator is overwritten; the equal-characteristic paragraph changes T_p(K)/T_p(E_K) and ends with an unfinished tensor product. Connected p-divisible information cannot be replaced by Galois points in equal characteristic.',reason='The notes retain incomplete and inconsistent symbols, without manufacturing a finished parameter group.')
I('supersingular_open_image',[430],'conjecture','J’ai envie de conjecturer; un sous-groupe ouvert',
  'The page speculates that the Tate representation in the supersingular case is simple and perhaps has open image in its full automorphism group. The symbol before simple is uncertain.',
  'The unrestricted open-GL₂ claim is false for a supersingular CM elliptic curve over a field containing its CM endomorphisms. A non-CM refinement is a distinct question.')
I('cm_counterexample',[432],'idea of the earlier run','un sous-groupe ouvert',
  'Earlier-run example E:y²=x³−x over Q₃(i) has good supersingular reduction and a K-defined CM endomorphism. Its Galois image centralizes Q₃(i), hence is not open in GL₂(Q₃).',
  'Discriminant, point count, endomorphism relation and centralizer dimension are rechecked. This does not decide the uncertain adjective before simple.')
I('potential_good',[431],'unproved claim','méta-abélienne',
  'Integral j is equivalent to potentially good reduction. The ordinary versus supersingular alternative concerns a finite extension with good reduction; a potentially ordinary representation is virtually metabelian.',
  'The qualifier virtually matters: passing to an extension does not prove the original whole Galois image is metabelian.')
I('tate_valuation',[433,434],'conjecture','est-ce tjrs un entier',
  'The fragmented continuation asks whether the valuation component of the multiplicative parameter is a nonzero positive integer and uses it to obstruct extension of the p-divisible group.',
  'For a split Tate curve with normalized discrete valuation, v(q)=−v(j)>0 is an integer. A potentially multiplicative curve may require a quadratic character and an extension of the base.')
I('tate_valuation_idea',[438],'idea of the earlier run','modules galoisiens',
  'Earlier notes separate the valuation component from connected p-divisible data lost by a purely Galois description in equal characteristic.',
  'The split mixed-characteristic valuation check is carried out. The equal-characteristic unfinished notation is not resolved.')
I('bt_good_reduction',[439],'conjecture','on peut conjecturer',
  'The elliptic notes ask whether good reduction of the curve is equivalent to extension of its generic p-divisible group over the valuation ring.',
  'SGA7 IX5.10 and5.13(a) prove this for abelian varieties over a trait, with generic characteristic0 in the p-primary case. This is a checked precise fate, not merely a same-topic citation.')
I('tate_twist_counterexample',[440,441],'idea of the earlier run','forme de; forme finiment tordue',
  'Earlier-run test: over Frac W(F̄₅), twist the split Tate curve q=5 by d=5. The invariants have valuations v(c₄)=2,v(Δ)=7,v(j)=−1, so reduction is additive potentially multiplicative. The Tate sequence has the ramified quadratic twist χ_d.',
  'Minimality follows from v(Δ)<12. This refutes nonintegral-j⇒multiplicative reduction and the omission of a possible quadratic quotient character, even with algebraically closed residue field.')
I('tate_parameter_ideas',[442,444],'idea of the earlier run','élément canonique; A**',
  'Earlier notes question the claimed canonical multiplicative parameter: a Kummer kernel must be distinguished from principal units, and simultaneous subgroup/quotient basis changes act by p-adic unit squares.',
  'The square action is computed from the extension coefficient Hom(L,L∨(1)); a canonical parameter requires fixed identifications. The residue-field condition is explicit.')
I('elliptic_order_reading',[443],'reading question','Je conjecture; que cet élément a une image',
  'Scan037’s unfinished sentence plausibly continues on036, but the source scan order and foliation are retained.',reason='Both text endpoints were read. Sentence continuation is evidence for a local order hypothesis, not permission to reorder the diplomatic text.')

def save_items():
    assert sorted(entry_verdict)==list(range(1,445))
    (ROOT/'items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
    with (ROOT/'supplementary_entries.tsv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason','heading','notes_file_lines'],delimiter='\t')
        w.writeheader()
        for n,row in sorted(entry_verdict.items()):
            w.writerow(dict(row,heading=notes[n]['heading'],notes_file_lines=f"{notes[n]['start']}–{notes[n]['end']}"))
    print(f'Saved {len(items)} manually consolidated items and {len(entry_verdict)} supplementary note verdicts.')

if __name__=='__main__':
    save_items()


