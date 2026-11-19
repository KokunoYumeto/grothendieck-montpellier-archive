"""Manually authored records after complete reading of IX14–18.
The locator helper only formats scan/line ranges; it makes no mathematical
verdict.  Status categories are supplied explicitly in every call.
"""
from pathlib import Path
import re

ROOT=Path('/workspace/scratch/4017236f14bf')
TEXTS=ROOT/'sources/texts/codex'
CLAIMS=[]
GROUPS={
 'relation':{'searches':['S9E-01','S9E-02','S9E-03','S9E-04'],'shared_searches':['S67-01','S67-04','S67-09','S67-10','S67-13'],'refs':['Ore1944','Massas2023','Janowitz1963','PasekaVetterlein2025'],'scope':'Relations, powerset homomorphisms, conjugate/adjointable maps; Foulis1960 followed backwards from Janowitz1963 and Brameret1961. The older Foulis original was not accessible; the latter two primary texts were opened.'},
 'ortholattice':{'searches':['S9E-01','S9E-02','S9E-03','S9E-05','S9E-06','S9E-07'],'shared_searches':['S67-07','S67-09','S67-10','S67-13'],'refs':['Janowitz1963','LindenhoviusVetterlein2023','HardingNavara2011','Ore1944'],'scope':'Orthomodularity, Boolean subalgebras, orthogonal families, commensurability, complete ortholattices and finite counterexamples; Dacey and Foulis references followed backwards, without claiming to have inspected the unavailable Dacey thesis.'},
 'poset':{'searches':['S9E-01','S9E-05','S9E-06','S9E-07'],'shared_searches':['S67-07','S67-10'],'refs':['Jenca2026','JencaCorrection2026','LindenhoviusVetterlein2023'],'scope':'Comparability versus incomparability orthosets. Jenča2026 Example2.6 was opened and checked; its incomparability classification is not identified with the manuscript question. The correction metadata were opened but its full theorem was inaccessible.'},
 'atelier':{'searches':['S9E-01','S9E-03','S9E-04','S9E-05'],'shared_searches':['S67-02','S67-03','S67-05','S67-08','S67-11','S67-12'],'refs':['CSGUnpublished','Malgoire2002','CruzMorales2021'],'scope':'Exact Grothendieck atelier, magasin, spatios, commensurability, support, morphism and excision wording; named zbMATH/arXiv/MathOverflow/Numdam searches, EGA/SGA term comparison, published/unpublished bibliographies. No exact publication of these axiom versions was identified.'},
 'localization':{'searches':['S9E-02','S9E-03','S9E-04','S9E-05'],'shared_searches':['S67-05','S67-08','S67-11'],'refs':['Stacks04VB','SGA4II','Esquisse1997','CSGUnpublished'],'scope':'Localization of categories/posets and calculus of fractions; constructible supports, gluing, subdivision, EGA/SGA and Esquisse comparison. General localization theory does not establish the atelier-specific support comparison.'},
}

def locations(spec):
    rows=[]; allscans=[]
    for folder,scans in spec:
        name=f'J156-9-{folder:02d}_transcription.tex'
        lines=(TEXTS/name).read_text().splitlines()
        marks=[(i+1,int(m.group(1))) for i,l in enumerate(lines) if (m:=re.search(r'\\scanpage\{(\d+)\}',l))]
        for k,(start,scan) in enumerate(marks):
            if scan in scans:
                end=marks[k+1][0]-1 if k+1<len(marks) else len(lines)
                rows.append(f'{name}: scan {scan}, lines {start}–{end}')
                allscans.append(scan)
    assert rows,spec
    return rows,sorted(set(allscans))

def C(n,spec,his,statement,status,category,group='atelier',cls='D',fate=None,refs=None,check=None,computation=None,confidence='medium',dates=None):
    lines,scans=locations(spec); g=GROUPS[group]
    if fate is None:
        fate='No exact published statement with these atelier hypotheses was identified in '+', '.join(g['searches']+g['shared_searches'])+'. '+g['scope']+' D means this bounded search found no exact match; it is not a proof of absence.'
    CLAIMS.append({'id':f'C-SA21-9-{n:03d}','items':[],'cote':'156-9','scans':scans,'lines':lines,
      'his_statement':his,'statement':statement,'status_on_pages':status,'status_category':category,
      'computation':computation or 'No numerical computation on these pages. Algebraic reasoning and independent finite certificates, when present, are identified separately; source reading is not recorded as proof checking.',
      'class':cls,'fate':fate,'fate_date':dates or {'searched_as_of':'2026-11-19','first_circulation':None,'publication':None},
      'present_status':'As of 2026-11-19: '+(check or status)+' Search family: '+group+';',
      'refs':refs or g['refs'],'confidence':confidence})

# IX105–111: the powerset analogy, orthomodularity and its limits.
C(81,[(14,[105])],
 'A: commutation à la disjonction, aux Inf non vides, à S∧CT; f′ injection.',
 'Let R⊆E×E′ be a relation, Γ=R its graph (no duplicate edges), f,f′ its projections, and u(S)={y:∃x∈S,(x,y)∈R}. The following are equivalent: u preserves disjointness; u preserves binary intersections; u preserves every nonempty intersection; u preserves S\\T for all S,T; it does so for T⊆S; f′ is injective. All joins, including the empty join, are already preserved. The graph hypothesis matters: an arbitrary span with repeated edges need not satisfy the projection characterization.',
 'Equivalences stated; proof not written out here.','stated without proof','relation','E',
 'Elementary relation/powerset calculus, within the pre1986 polarity framework of Ore1944 §4 and Theorem8. Massas2023 Theorem2.29 provides the complete Boolean-homomorphism comparison. Every equivalence is independently re-proved; no novel attribution to a later broad paper is made.',
 check='Valid for arbitrary sets and a genuine relation graph; independent proof in formalism_and_checks.md §2.',computation='check_ix_examples.py → finite_checks_output.json#set_relation_classification: every relation on sets of sizes0–3 tested.',confidence='high')
C(82,[(14,[105,106])],
 'Corollaire1: disjonction et1→1; Inf quelconques; C; comorphisme g^{-1}.',
 'For the same relation-induced join map u:P(E)→P(E′), the following are equivalent: disjointness preservation and u(E)=E′; binary-meet preservation and u(E)=E′; preservation of all finite meets including the empty one; preservation of all meets; complement preservation; f′:Γ→E′ bijective. These conditions are exactly u=g^{-1} for a uniquely determined function g:E′→E.',
 'Corollary stated, with margin indicating its dependence on A and B.','stated without proof','relation','E',
 'Complete powerset Boolean homomorphisms are the classical inverse-image maps; modern exact formulation Massas2023 Theorem2.29, with older Boolean duality background. The elementary proof uses the disjoint images of singleton sets, not a topological sobriety assumption.',
 computation='set_relation_classification in finite_checks_output.json; empty underlying sets included.',check='Valid; all empty-operation conventions included.',confidence='high')
C(83,[(14,[106])],
 'B: α_*(1)=1 iff β_*(S)=∅⇒S=∅ iff f′ surjectif.',
 'For a relation R and its transpose, u(E)=E′ iff the transpose direct-image v:P(E′)→P(E) reflects0, iff every y∈E′ occurs in an edge of R (f′ is surjective).',
 'Equivalence stated.','stated without proof','relation','E',
 'Standard relation converse/powerset calculation, already in the general pre1986 Galois framework (Ore1944 Theorem8); independently re-proved here. Paseka–Vetterlein2025 Lemma3.8 is an exact modern kernel/orthogonal-image analogue, not the first occurrence of the elementary set fact.',
 computation='set_relation_classification in finite_checks_output.json.',check='Valid, including empty sets.',confidence='high')
C(84,[(14,[106])],
 'Corollaire2: commutation fidèle à la disjonction.',
 'For relation-induced u:P(E)→P(E′), preservation and reflection of disjointness is equivalent to preservation of disjointness plus u(S)=∅⇒S=∅, and to f′ injective and f surjective. Equivalently u is inverse image under a surjection E′_0→E followed by extension of subsets along E′_0↪E′.',
 'Corollary stated.','stated without proof','relation','E',
 'Elementary relation calculus; Ore1944 supplies the relation/polarity framework and Massas2023 Theorem2.29 the total powerset-homomorphism case. Independent proof and exhaustive finite verification identify the exact injective/surjective projections.',
 computation='set_relation_classification in finite_checks_output.json.',check='Valid; faithfulness alone does not make the relation a direct injection E→E′.',confidence='high')
C(85,[(14,[106])],
 'Corollaire3: C et réflexion du zéro; disjonction fidèle et1→1; g surjective.',
 'For relation-induced u:P(E)→P(E′), complement preservation and zero reflection are equivalent to faithful disjointness preservation plus top preservation, and to u=g^{-1} for a surjection g:E′→E. The map u is then injective as a powerset map.',
 'Corollary stated.','stated without proof','relation','E',
 'Classical inverse-image calculus and complete atomic Boolean duality; exact contemporary formulation compared with Massas2023 Theorem2.29. The surjectivity/zero-reflection step is independently proved from singleton fibers.',
 computation='set_relation_classification in finite_checks_output.json.',check='Valid.',confidence='high')
C(86,[(14,[107,108])],
 '“dans quelle mesure ces équivalences ... restent valables”; hypotheses of commensurability/constructibility hoped for.',
 'Question for complete ortholattices L,M: if u:L→M preserves all joins and orthogonality, does it preserve meets or relative differences, and does u(1)=1 force uC=Cu? The text explicitly restricts its expectation to unspecified suitable commensurable/constructible supports; it does not state a precise universal restricted theorem. In unrestricted ortholattices the implication to complement is false even when u preserves every meet too.',
 'Open on the pages; author says his existing arguments require strong hypotheses close to Booleanity.','open on the pages','relation','D',
 'S9E-01–04 and shared S67 relation/support searches locate adjointable-map theory, but no exact constructible-support theorem for these ateliers. Janowitz1963 and Paseka–Vetterlein2025 concern explicitly specified lattice/orthoset hypotheses. The unrestricted implication is independently refuted here, not claimed as an identified later Grothendieck theorem.',
 computation='general_spatios_corollary_failure: B4→O6 preserves all joins/meets, top and orthogonality, has the exact conjugate transpose, but fails complement preservation.',check='Negative in the unrestricted formulation; the proposed geometric restriction remains unspecified. R-SA21-9E-001.',confidence='high')
C(87,[(14,[108])],
 'NB: commutation à C implique toujours1→1 et compatibilité à la disjonction.',
 'If u:L→M preserves all joins between complete ortholattices and commutes with orthocomplementation, then u(0)=0, u(1)=1, u preserves all meets, and a⊥b implies u(a)⊥u(b). This requires the standing join-preservation hypothesis, not merely a set map commuting with C.',
 'Formal observation stated.','stated without proof','relation','E',
 'A direct De Morgan/monotonicity consequence of classical ortholattice axioms, compared with Janowitz1963 pp1241–1242 and the adjointable-map framework. Independently re-proved; no claim of a new theorem.',check='Valid with standing join preservation; proof in formalism_and_checks.md.',confidence='high')
C(88,[(14,[108])],
 '“Si α_* et β_* commutent à C ... iso. ... inverses?” marginal “oui”.',
 'Let u:L→M and v:M→L satisfy u(a)⊥b iff a⊥v(b) for all a,b, with L,M complete ortholattices. If both commute with C, they are mutually inverse ortholattice isomorphisms. The conjugacy is the exact one in IX90 Proposition3, not an arbitrary pair of join maps.',
 'Question answered affirmatively in a marginal insertion; no proof supplied.','corrected by himself later','relation','E',
 'This is an elementary consequence of the pre1986 Galois-adjunction formalism: complement conjugacy gives both u⊣v and v⊣u. Ore1944 provides that framework; Janowitz1963 p1242 treats the orthogonal adjoints. The exact short proof is supplied independently, not attributed verbatim to those sources.',check='Valid. Two opposite adjunctions give vu=id and uv=id. R-SA21-9E-002.',confidence='high')
C(89,[(14,[108])],
 'B(i)⇔(ii) “se vérifie trivialement dans tout spatios”.',
 'For conjugate join maps u:L→M, v:M→L between complete ortholattices, u(1)=1 iff v reflects0. Indeed v(b)=0 iff u(1)⊥b, so ker v is the principal ideal ↓C(u(1)).',
 'Formal generalization stated as trivial.','stated without proof','relation','E',
 'Classical adjoint/annihilator calculation, already present in the pre1986 orthogonal-adjoint framework of Janowitz1963 p1242; modern exact orthoset identity in Paseka–Vetterlein2025 Lemma3.8. Independent proof supplied.',check='Valid without Booleanity or orthomodularity.',confidence='high')
C(90,[(14,[109])],
 'Lemme1: b≤c, existence de b*⊥b avec b∨b*=c; b*_0=Cb∧c.',
 'In any ortholattice, for b≤c there exists d⊥b with b∨d=c iff c=b∨(c∧Cb). When this holds c∧Cb is the largest such d. Completeness is unnecessary for this finite statement.',
 'Lemma stated, with the maximality observation.','stated without proof','ortholattice','E',
 'The identity is exactly the local orthomodular law, standard before1986; Janowitz1963 p1241 states it. The maximality assertion follows directly from d≤c and d≤Cb and is independently re-proved.',check='Valid; the condition need not hold in a general spatios.',confidence='high')
C(91,[(14,[109,111])],
 'Lemme2 and Corollaire2: b,c generate Boolean2^n; α=b, β=c∧Cb, γ=Cc.',
 'For b≤c in a nontrivial ortholattice, the subortholattice generated by b,c is Boolean iff both c=b∨(c∧Cb) and Cb=Cc∨(Cb∧c). Its nonzero atoms are the nonzero members of b,c∧Cb,Cc; its cardinal is2^n with1≤n≤3. If the one-element ortholattice is allowed, n=0 must also be admitted. The displayed alternative residual equations contain a transcription alarm.',
 'Lemma and subsequent corollary stated; several marginal rewritings and index ambiguities.','stated without proof','ortholattice','E',
 'Classical Boolean-block/orthomodular calculations; Janowitz1963 Lemma1 supplies the familiar comparable/commuting context. Here the two local identities are checked directly in the weaker arbitrary-ortholattice setting, without assuming global orthomodularity.',check='Valid with the nontriviality qualification and the explicit two identities; uncertain displayed alternatives remain reading questions.',confidence='high')
C(92,[(14,[109,111])],
 'Corollaire: all comparable pairs; all orthogonal pairs; finite orthogonal families.',
 'For an ortholattice L, the following are equivalent: every b≤c satisfies the law in Lemma1; every comparable pair generates a Boolean subortholattice; every orthogonal pair does so; every finite pairwise orthogonal family does so. These are orthomodularity. In a complete orthomodular lattice every orthogonal family also lies in a complete Boolean subortholattice.',
 'Equivalences stated, with proposed finite-chain and family versions added in the margins.','stated without proof','ortholattice','E',
 'Known before1986: Janowitz1963 pp1241–1242, especially Lemma1(i)–(v), gives orthomodularity, commuting comparables and closure of commutants under existing joins. The complete-family conclusion follows from those facts and is explained separately, not mistaken for distributivity of all L.',check='Valid. This is the precise classical identification of the manuscript’s condition.',confidence='high')
C(93,[(14,[111])],
 '“Ces conditions sont-elles toujours ...? ... entraînent-elles que Σ est booléen?” including infinite families.',
 'A general complete ortholattice need not satisfy the orthomodular conditions. Even if every arbitrary orthogonal family lies in a complete Boolean subortholattice, the whole lattice need not be Boolean: the six-element orthomodular lattice MO2 (two Boolean4 blocks sharing0,1) is a counterexample. Every orthogonal family has at most two distinct nonzero elements.',
 'Questions open on the page; margin announces a ten-element counterexample on scan113.','open on the pages','ortholattice','E',
 'NonBoolean orthomodular lattices and Boolean blocks predate1986; Janowitz1963 explicitly works with nondistributive Hilbert-subspace lattices. Harding–Navara2011 identifies MO2 and studies Boolean subalgebras, confirming the exact finite model. The answer is not a newly discovered modern resolution.',
 computation='orthomodular_does_not_force_Boolean and P4_comparability_counterexample in finite_checks_output.json; all comparable pairs and all orthogonal subsets of MO2 checked.',check='Both universal hopes are negative; even the infinite-family strengthening does not force Booleanity. R-SA21-9E-003.',confidence='high')
C(94,[(14,[111])],
 'Σ associated to an ordered set L and xδy iff x<y or y<x: “avoir le coeur net”.',
 'If orthogonality on a poset P is strict comparability (x<y or y<x), must the lattice of double-orthogonal closed subsets be orthomodular? No: take the height-two poset with strict pairs0<1,2<1,2<3. Its comparability graph is P4, whose six-element closed-set lattice is O6.',
 'Explicit unresolved special-case question.','open on the pages','poset','B',
 'The exact P4 closed-set counterexample is published in Lindenhovius–Vetterlein2023 Example3.3 and appears in Jenča’s23Jan2024 preprint Example2.6, published2026. The orientation making P4 a comparability graph is our explicit identification. Jenča2026 Theorem4.2 is about INcomparability and is not substituted for this statement; an Aug2026 correction exists, whose full corrected theorem was inaccessible.',
 computation='P4_comparability_counterexample: strict-order/transitivity, graph equality, complete ortholattice and orthomodular failure checked.',check='Negative; exact finite graph matches later published example. R-SA21-9E-004.',confidence='high',dates={'searched_as_of':'2026-11-19','first_circulation':'2022-07-19 (LV preprint metadata; exact Example3.3 checked in2023 version)','publication':'2023-03-10 (LV);2026-02-05 (Jenča)'})
C(95,[(15,[113])],
 'Ten-element diagram; j∨k=A, k∨a′=B, a′∨j=C; “C↓a pasOK”.',
 'The page intends a ten-element ortholattice violating the local complement law. An explicitly labeled analyst reconstruction uses I={i,i′,j,k}, the Boolean8 of unions of blocks{i,i′},{j},{k}, plus{i} and its complement{i′,j,k}, ordered by inclusion with set complement. For b={i}<c={i,i′}, c∧Cb=0, so c≠b∨(c∧Cb). The literal transcribed second disjunct and the marked edge c<C do not define this model and remain unresolved ink questions.',
 'Counterexample diagram and set recipe written; literal transcription has incompatible features.','proof sketched','ortholattice','D',
 'Searches S9E-01–07 and shared S67 support searches identify standard O6/nonorthomodular examples and Boolean-block theory, but no exact publication matching this ten-element recipe was located. D concerns the exact diagram/recipe; it does not assert novelty of finite nonorthomodular lattices.',
 computation='scan113_reconstruction checks the10-element lattice, complement, all joins displayed on the page and failure; separately tests the literal set family and reports its lack of complement closure.',check='Reconstruction verified; original ink not adjudicated. The independent six-element counterexample does not depend on this repair.',confidence='medium')

# IX115–128: admissibility, commensurability and intrinsic supports.
C(96,[(15,[115,116])],
 'Lemme1: e_i≠0 orthogonaux, ∨e_i=1; P(I)→Σ, J↦e_J.',
 'Let L be a complete ortholattice and(e_i) a pairwise orthogonal family of nonzero elements with join1. It is contained in a complete Boolean subortholattice iff h:P(I)→L, h(J)=∨_{i∈J}e_i, preserves orthocomplementation. The map is always injective and preserves all joins; under the condition it preserves all meets and its image is the least complete Boolean subortholattice containing the family.',
 'Lemma, injectivity justification and minimality claim stated.','proof sketched','ortholattice','E',
 'Standard complete Boolean partition calculus, compared with Massas2023 Theorem2.29 and pre1986 ortholattice/commutant facts in Janowitz1963. A direct proof in arbitrary complete ortholattices is supplied; no global Booleanity is assumed.',refs=['Massas2023','Janowitz1963'],check='Valid; nonzero elements and the total join1 are essential to the stated powerset identification.',confidence='high')
C(97,[(15,[116])],
 'Cor1: add e_0=C∨e_i; admissible; Σ_e≅P(I⊔{e_0}).',
 'For nonzero orthogonal(e_i), put e=∨e_i. Boolean commensurability is equivalent to C e_J=e_{I\\J}∨Ce for every J⊆I, equivalently e_J=e∧C e_{I\\J}. The least complete Boolean subortholattice has atoms the e_i together with Ce WHEN Ce≠0. If e=1, the added zero must be omitted: the displayed uniform isomorphism with P(I⊔{e_0}) otherwise fails.',
 'Corollary/definition stated; the zero-complement degeneracy is not separated.','definition/construction','ortholattice','E',
 'Classical Boolean partition construction, with the degeneracy corrected explicitly here. The underlying powerset/atom mechanism is the complete Boolean duality in Massas2023 Theorem2.29; no atelier-specific later resolution is claimed.',refs=['Massas2023','Janowitz1963'],check='Criterion valid; cardinality/isomorphism formula needs omission of a zero added atom. R-SA21-9E-006.',confidence='high')
C(98,[(15,[117])],
 'Axiome supp1; nonredundant for Figelspat_fin(Σ); e′=Ce∧(e∨e′).',
 'Supp1 requires the virtual open supports{X°:X∈F} of every admitted figure F to be Boolean-commensurable. In the standard atelier of finite spatial figures over a complete ortholattice L, this is equivalent to e′=Ce∧(e∨e′) for every orthogonal e,e′, hence to orthomodularity of L. Thus it is not implied by the primitive atelier axioms.',
 'Axiom introduced; nonredundancy reduced to the earlier lattice criterion.','definition/construction','ortholattice','E',
 'The lattice identity is the pre1986 orthomodular criterion (Janowitz1963 p1241 and Lemma1). The translation uses the explicit spatial-figure model of IX50–60, not a claim that all ateliers have orthomodular support lattices. O6/P4 gives the exact failure.',check='Correct lattice reduction under the stated standard spatial construction; the new atelier terminology itself has no exact later publication identified.',confidence='high')
C(99,[(15,[118])],
 'Figspatdisc(Σ); B≪A iff every b≤some a; a′=∨B_a, a″=... .',
 'For finite sets A,B of nonzero pairwise orthogonal elements of a complete ortholattice, define B≪A iff each b∈B is below some a∈A. Such a is unique because distinct a are orthogonal and b≠0. Put B_a={b∈B:b≤a}, a′=∨B_a and a″=a∧Ca′. The last formula is an analyst reconstruction of the transcribed b∧Cb′, and the deletion of “non” before “nuls” must be checked on the scan.',
 'Definition/construction; literal variable and nonzero-status alarms.','definition/construction',check='Pointwise refinement and uniqueness valid with nonzero supports; literal formula not silently corrected.',confidence='high')
C(100,[(15,[118]),(16,[119])],
 'Lemme2: A∪B in a complete Boolean subspatios iff a=a′∨a″ and Bhat admissible.',
 'For the data in C-SA21-9-099, A∪B is Boolean-commensurable iff every a=a′∨a″ and Bhat=B∪{a″:a∈A,a″≠0} is admissible. In that case the least complete Boolean subortholattice generated by A∪B equals that generated by Bhat. It is P(Bhat) only when ∨Bhat=1; otherwise its additional nonzero atom C∨Bhat must be included.',
 'Lemma and minimality stated; the final powerset identification omits the exterior atom.','stated without proof','ortholattice','E',
 'A standard partition/refinement argument inside a Boolean subalgebra, directly re-proved here from C-SA21-9-096. Janowitz1963 and Massas2023 supply the established Boolean/orthomodular context. No later source is used to conceal the displayed missing-atom exception.',refs=['Janowitz1963','Massas2023'],check='Equivalence valid with the reconstructed a″; the unrestricted final cardinality formula is false. R-SA21-9E-006.',confidence='high')
C(101,[(16,[119,120,121])],
 'Axiom γ²; a subset is “commensurable dans leur ensemble”.',
 'A subset T of a complete ortholattice L is commensurable iff some complete Boolean subortholattice of L contains T. The proposed pair-support axiom γ² requires joint commensurability of all virtual open supports from G and F whenever G≪F. This is stronger than separate admissibility of each figure. For arbitrary ortholattices pairwise commensurability of elements need not imply joint commensurability; that distinction disappears for pairwise commuting families in a complete orthomodular lattice.',
 'Definitions and proposed strengthening of supp1.','definition/construction',check='Definition precise; non-equivalence of pairwise and joint conditions demonstrated in the18-element certificate. Orthomodular special case uses Janowitz1963 Lemma1(v).',refs=['Janowitz1963','HardingNavara2011','CSGUnpublished'],confidence='high')
C(102,[(16,[121,122])],
 'Lemme3: residual families A_i″ are mutually orthogonal.',
 'For a finite chain A0≪A1≪⋯≪An of finite nonzero orthogonal sets under pointwise containment, define r_i(a)=a∧C∨{b∈A_{i−1}:b≤a}, omit zero residues, and set R0=A0. The union of all residue sets Ri is pairwise orthogonal. This part does not require Booleanity or the decomposition a=a′∨a″.',
 'First part of Lemma3 stated without a proof.','stated without proof','ortholattice','E',
 'Elementary order/orthogonality calculation within classical ortholattice theory; independently proved by following a receiving ancestor through the chain. Janowitz1963 supplies the surrounding standard terminology; no exact later atelier theorem is asserted.',check='Valid as a standalone ortholattice statement; proof in formalism_and_checks.md §4.',confidence='high')
C(103,[(16,[121,122])],
 'Lemme3: diagram commensurable iff the union of nonzero residues is admissible.',
 'The forward implication holds for every such chain. The converse holds if each intermediate element is the join of its predecessor fiber and its residue; in particular it holds under the preceding pair axiom γ². Without this condition, the general-spatios formulation is false: in O6 take A0={a}, A1={b}, 0<a<b<1 on one branch, with b∧Ca=0. The residual family is{a}, Boolean-commensurable, whereas{a,b} is not.',
 'Equivalence stated in the general formulation. The role of the preceding γ² as a standing assumption is not restated; source has an A0 omission later corrected in the union index.','stated without proof','ortholattice','D',
 'S9E-01–07 locate the standard Boolean-block and orthomodular background, but no exact published residual-diagram criterion for this generality. The missing decomposition is exposed by an independent finite model and restored explicitly; no unconditional refutation of a reading retaining γ² is claimed.',
 computation='residual_lemma_missing_hypothesis in finite_checks_output.json.',check='Valid under the explicit decomposition hypothesis; false as a standalone unrestricted criterion. R-SA21-9E-007.',confidence='high')
C(104,[(16,[122])],
 'Axiome γ³, “englobant les deux précédents”.',
 'The proposed γ³ requires that, for every finite refinement chain F0≪⋯≪Fn of admitted figures, the union of all their virtual open-stratum supports be contained in one complete Boolean subortholattice. It implies supp1 and γ² by taking chains of lengths0 and1. It demands joint commensurability of the whole chain, not merely of consecutive pairs.',
 'New axiom introduced.','definition/construction',check='The implication to the earlier axioms is immediate; no claim that primitive atelier axioms imply γ³.',confidence='high')
C(105,[(16,[122,123])],
 'Figspatcomm(Σ); “il n’est pas clair que ... soit transitif”; g,g′,f′ obstruction.',
 'Consider commensurable discrete spatial figures in a complete ortholattice and strengthen pointwise refinement B≪A by requiring A∪B commensurable. This strengthened relation need not be transitive. A checked18-element ortholattice has figures A0={g,g′}, A1={g∨g′}, A2={g∨g′,f′}; adjacent pairs generate Boolean8, while A0∪A2 generates nonBoolean18. This also verifies the author’s triple obstruction. It does not establish his stronger parenthetical suspicion using only one-stratum figures.',
 'Construction proposed, then doubted/abandoned because transitivity is not established.','open on the pages','ortholattice','D',
 'S9E-01–07 and backward commutation references locate Boolean-block theory, but no exact published theorem for this proposed strengthened atelier refinement. The negative answer for discrete figures is an independent finite certificate, not inferred from broad quantum-logic similarity.',
 computation='commensurable_refinement_not_transitive in finite_checks_output.json, including full order and complement table.',check='Construction fails in this stated generality. R-SA21-9E-008. The orthomodular or Boolean ambient case avoids this obstruction.',confidence='high')
C(106,[(16,[124])],
 'Faithful external support (VIIIp62) ⇒ γ³? comparison with a Corollaire1.',
 'Does a faithful external support in the exact sense of VIII68–71 force γ³? No. For the P4 atelier with both primitive orders equality, realize each stratum x by a private point plus one shared point for each nonorthogonal pair containing x. These supports satisfy all four external-support axioms, normalization and faithful disjointness. Nevertheless the middle-edge figure has virtual supports generating O6 and fails even supp1. The stronger VIII fully faithful condition is not assumed.',
 'Explicit question; its cited page for Corollaire1 is uncertain.','open on the pages','atelier','D',
 'Exact atelier/support searches S9E-01,03–05 and shared S67-02,03,05,08,11,12 found no published theorem matching the faithful hypothesis. Standard P4 ortholattice calculations are published (LV2023 Example3.3), but the external-support realization and comparison with VIII’s four axioms are checked independently here. VIII87 itself uses full faithfulness and cannot answer the weaker question.',
 refs=['LindenhoviusVetterlein2023','CSGUnpublished','Malgoire2002'],computation='faithful_external_does_not_imply_commensurability: every primitive atelier clause and VIII68(i)–(iv), normalization, VIII71 faithfulness checked.',check='Negative under the exact faithful hypothesis. R-SA21-9E-005; MP-SA21-9-25.',confidence='high')
C(107,[(16,[124,125]),(17,[126,127,128])],
 'Replace global Σ by constructible supports with C everywhere and Sup/Inf only for commensurable families.',
 'The proposed object is a collection of constructible supports with an everywhere-defined complement and partially defined joins/meets for suitable commensurable families, built intrinsically from figures and subdivisions rather than from all double-polar closed subsets. The pages do not yet specify all admissible operations or a universal property. This is a program, not an asserted reconstruction theorem.',
 'Explicit unresolved structural concern and proposed direction.','open on the pages','localization','D',
 'Searches S9E-02–05 and shared S67-05,08,11 compare categorical localization, constructibility in EGA/SGA and Esquisse§5. Those sources do not define this partial support algebra or settle its relationship to Σ_A. No exact matching construction was identified; D is bounded.',check='The intended replacement is identifiable as a program; no missing axioms are supplied as his text.',confidence='high')
C(108,[(17,[126,127,128])],
 'Invert subdivision arrows in(F,≪); will the category of fractions be an ordered set and embed into Σ?',
 'Let F be the chosen figure poset under refinement and W its subdivision arrows. The question is whether F[W^{-1}] is thin, whether its posetal reflection maps order-embed­dingly into Σ_A by support, and whether its image is the closed constructible supports. Existence of a categorical localization alone proves neither thinness nor this support comparison. A suitable calculus of fractions/common refinement condition must be verified for the actual W.',
 'Author explicitly doubts both thinness and identification with a subset of Σ.','open on the pages','localization','D',
 'Stacks Project§4.27, Definition4.27.1 and Lemma4.27.2, opened, gives the exact multiplicative-system conditions and fraction construction; it traces Gabriel–Zisman1967 ChapterI§2 (original book not inspected). This settles only the general categorical mechanism. No exact published verification for these ateliers was found.',check='Open for the manuscript’s W within the documented search. General poset localization need not be thin; no unrelated localization counterexample is presented as an atelier counterexample.',confidence='high')
C(109,[(17,[127,128])],
 'Σ Boolean for point ateliers and maquettes; “peut-être” for faithful ateliers.',
 'For a maquette, disjointness is inequality, so every subset is double-polar closed and Σ_A=P(A). In a point atelier with the stated complete point-separation/detection hypotheses, the analogous powerset description is the earlier result. The extrapolation to all faithfully externally realized ateliers is only tentative and is false under VIII’s faithful definition, by C-SA21-9-106.',
 'Established examples recalled; faithful case explicitly qualified as a hope.','stated without proof','ortholattice','E',
 'The discrete-polarity powerset calculation is elementary pre1986 material (Ore1944 polarity framework; complete Boolean powerset comparison Massas2023 Theorem2.29). The faithful-atelier extrapolation is not supported by those sources and has a separate counterexample.',refs=['Ore1944','Massas2023','CSGUnpublished'],check='Maquette case verified directly; do not turn the tentative faithful extension into a theorem.',confidence='high')

# IXbis130–137: sub-ateliers, pointed morphisms and excision.
C(110,[(17,[130])],
 'Sousat: X≪°Y′◁Y with X,Y∈A′⇒Y′∈A′.',
 'For an atelier A with incidence, open refinement and disjointness, a subset A′ satisfying Sousat (whenever X,Y∈A′ and X≪°Y′⊴Y, then Y′∈A′) inherits an atelier structure from the three relations. Its derived refinement relation equals the restriction of that of A. The least receiver remains in A′ precisely by the displayed condition; no blanket claim is made for arbitrary subsets.',
 'Definition/recall with inheritance and refinement assertion.','definition/construction',check='The receiving-stratum argument supports the assertion; full source axiom version retained, not replaced by the older VI lower-subfamily notion.',confidence='high')
C(111,[(17,[130])],
 'Ex1: Omb°(φ) is a subatelier for a prefigure φ.',
 'If φ⊆A is pairwise compatible (its incidence-lower closure is a figure), the open shadow Omb°φ={X:∃Y∈φ, X≪°Y} satisfies Sousat and hence is a subatelier with the induced relations. The source cites IXp27 for the earlier argument.',
 'Example recalled without repeating its proof.','stated without proof',check='Recorded with the prefigure/compatibility hypothesis; cross-reference checked against IX31.',confidence='medium')
C(112,[(17,[130])],
 'Ex1bis: a figure φ is itself a subatelier, a maquette.',
 'The set of strata of an admitted figure φ, with the three relations restricted, is a subatelier and has open refinement equal to equality and disjointness equal to inequality. Its incidence order remains the face order. The proof uses compatibility to infer X=Y′ from X≪°Y′⊴Y with X,Y in the figure.',
 'Short proof on the page.','proved there',check='Valid for an admitted figure and the current primitive relations; not the assertion that every lower subset of arbitrary data is an atelier.',confidence='high')
C(113,[(17,[131])],
 'Ex2: strict residual {X:X∥S}.',
 'For S⊆A, take the strict residual of strata X totally disjoint from S, meaning every face of X is internally disjoint from every face of each stratum in S. This subset is closed under derived refinement and incidence faces, hence satisfies Sousat and is a subatelier. Total disjointness ∥ must not be replaced by primitive internal disjointness δ.',
 'Example justified by the two closure properties.','proof sketched',check='The distinction between total and internal disjointness is retained; no theorem for the unqualified polar S⊥ is inferred.',confidence='medium')
C(114,[(17,[131])],
 'comp°S generally not a subatelier; for prefigureφ add compatibility.',
 'The primitive polar {X:XδS} need not satisfy Sousat. If φ is a prefigure, the smaller set {X:Xδφ and X compatible with every member ofφ} is a subatelier. In the Sousat test the candidate Y′ is compatible withφ; if Y′ equaled a stratum Z ofφ, X≪°Z and XδZ would force XδX, a contradiction.',
 'Negative general observation recalled; positive modified construction proved.','proved there',check='The added compatibility hypothesis is essential to the displayed proof; the cancellation/restoration in its compatibility sentence remains an ink alarm.',confidence='high')
C(115,[(17,[131])],
 '“Dans ces quatre cas ... Σ_A′↪Σ_A?”',
 'For each of the four subatelier constructions just listed, is there a canonical embedding of the associated double-polar support lattices into Σ_A, and which operations does it preserve? Inclusion of the underlying orthosets alone does not provide an inclusion of orthoclosed subsets: closure depends on the ambient orthogonality relation. The text does not specify a complete-lattice versus ortholattice embedding.',
 'Explicit verification question.','open on the pages','atelier','D',
 'Exact subatelier/support searches found no matching theorem. Paseka–Vetterlein2025 Lemmas3.7–3.8 and its closure functor explain what adjointability adds, but ordinary inclusion is not automatically adjointable. No exact embedding is inferred without checking the needed condition for each of the four constructions.',refs=['PasekaVetterlein2025','Ore1944','CSGUnpublished'],check='Unresolved in this run for all four typed constructions; the missing morphism/operation specification is recorded.',confidence='medium')
C(116,[(17,[132])],
 'f*:Figures(E)→Figures(E′); elementary figures allegedly go to A′∪{∅}.',
 'For a set map f:E′→E, the full set-figure pullback defined in VIII55 retains f^{-1}(S) exactly when f^{-1}(S°)≠∅. It need not send an elementary figure to elementary-or-empty: pull back closed strata{a},{b},{a,b,c} along{a,b}↪{a,b,c}; the two surviving singleton strata have no greatest element. A different partial map on elementary generators, killing the top when its open preimage is empty, can be considered but is not the displayed full-figure pullback.',
 'Elementary-or-empty claim stated; no convention change for the displayed Figures map is given here.','false as stated','atelier','D',
 'S9E-01,03–05 and shared S67 atelier/gluing searches found no exact published construction resolving this degeneracy. Ordinary inverse-image Boolean algebra facts are standard (Massas2023 Theorem2.29), but do not imply preservation of elementary figure type. Both source endpoints VIII55–56 and IX132 were read.',refs=['Massas2023','CSGUnpublished'],computation='elementary_figure_pullback_not_elementary in finite_checks_output.json; original figure, open strata, corrected pullback and absence of greatest stratum checked.',check='False for the same full-figure pullback. Partial-generator reinterpretation is explicitly an analyst reconstruction; R-SA21-9E-009.',confidence='high')
C(117,[(17,[132])],
 'Injective g:E→E′ gives injective direct figure map; supports preserve Sup, nonemptyInf, notC unless bijective.',
 'An injective set map g:E→E′ transports each closed/open stratum without collisions and gives an injective map of set figures, preserving the stated incidence, open-refinement and disjointness relations. On ordinary supports it sends S to g(S), preserves arbitrary unions and all nonempty intersections, but preserves complements relative to whole E,E′ iff g is surjective too.',
 'Example and support calculation stated.','stated without proof','relation','E',
 'Elementary set-image calculus and powerset duality; independent direct proof from injectivity. Relation classification in C-SA21-9-081–085 supplies the exact scope, and no noninjective generalization is inferred.',check='Valid for injective g; empty meets/top and complements fail when the image is proper.',confidence='high')
C(118,[(17,[133])],
 'Common span Γ→E′ injective; test for direct-injection case questioned in margin.',
 'A relation graph with f′ injective yields on supports the composite inverse image under f followed by direct image under f′. It is inverse image under an actual total E′→E iff u(1)=1. It is direct image under an injection E→E′ iff f is bijective; equivalently, given disjointness preservation by u, its transpose v preserves complement. The last criterion is our precise resolution of the marginal question; the transcribed “β commutes à α” is not a well-typed complement condition. The elementary-generator output has the caveat in C-SA21-9-116.',
 'Span construction stated; direct-injection criterion left as a question with uncertain marginal symbols.','open on the pages','relation','E',
 'Standard relation/powerset calculation in the older Galois framework; S9E-01–04 and shared S67 relation searches supply the context. The exact criterion is independently derived and tested, not attributed to an unread source.',computation='set_relation_classification includes direct_injection_characterization on every relation of sizes0–3.',check='Support-level criterion resolved; the figure-level degeneracy and marginal reading are retained separately.',confidence='high')
C(119,[(17,[133])],
 'No direct figure map for noninjective g; does every atelier morphism induce a correspondence on spatios?',
 'For a noninjective set map, direct images of distinct open strata can overlap, so the naive direct-stratum image need not be a figure. No canonical replacement/coarsening is defined. More generally the author asks whether the proposed atelier morphisms induce conjugate join maps on virtual supports. Preservation of the three primitive relations alone is weaker than the closure compatibility required in IX90–97.',
 'Negative expectation and explicit open functoriality question.','open on the pages','atelier','D',
 'Exact atelier morphism searches found no published resolution. The checked adjointable-map results of Paseka–Vetterlein2025 require an orthogonal adjoint; they do not assert that every relation-preserving map has one. The bare-kernel counterexample in C-SA21-9-121 demonstrates a concrete obstruction to that automatic passage.',refs=['PasekaVetterlein2025','Ore1944','CSGUnpublished'],check='Naive direct-image failure is clear; a general corrected pushforward is not ruled out. Bare support functoriality needs stronger conditions.',confidence='high')
C(120,[(18,[134,135,136])],
 'Provisional hom A→A′⊔{∅}, preserving three relations; pointed composition.',
 'Adjoin a formal0 to each atelier. Extend incidence by X⊴0 and0⊴X for every X, open refinement by0≪°X and X≪°0 iff X=0, and disjointness by0δX for every X including0. A provisional homomorphism is a basepoint-preserving function between these extensions preserving the three typed relations. Such maps compose and have identities. The extended incidence is not a partial order when A is nonempty; the extended open refinement is a partial order with bottom0. The earlier optional face-bijection condition VIII36–37(d) is expressly omitted.',
 'Definition marked provisional; composition is explained on scan136.','definition/construction',check='The elementary category construction is valid under exactly these zero conventions; no support functor is automatic.',confidence='high')
C(121,[(18,[135])],
 'ker f lower for≪°; support-closedness expected to need extra conditions.',
 'For a provisional pointed homomorphism as in C-SA21-9-120, ker f is lower for open refinement. It need not be a virtual support (double-polar closed): in the discrete P4 atelier, kill one endpoint and retain the induced three-vertex target. All three relation-preservation conditions hold, but the killed singleton has a two-element orthoclosure. This uses only primitive At1–4, not additional support-admissibility axioms.',
 'Lowerness proved by inspection; orthoclosedness explicitly flagged as requiring supplementary conditions.','proof sketched','atelier','D',
 'S9E-01–05 and shared support searches found no exact theorem for these provisional maps. Paseka–Vetterlein2025 Lemma3.8 proves orthoclosed kernels for adjointable maps, precisely a stronger condition. Our finite example verifies that the manuscript’s caution is necessary.',refs=['PasekaVetterlein2025','CSGUnpublished'],computation='bare_morphism_kernel_not_closed in finite_checks_output.json with all primitive orders, zero conventions and relation tests.',check='Lowerness valid; automatic support-closedness false. R-SA21-9E-010.',confidence='high')
C(122,[(18,[135,136,137])],
 'Excision A/N universal among homomorphisms with kernel⊇N; exact kernelN or possibly larger?',
 'For N⊆A lower under open refinement, seek an atelier A/N and provisional pointed hom p:A→A/N such that every pointed hom killing N factors uniquely through p. The author separately asks whether ker p=N or only ker p⊇N. The universal property is meaningful in the provisional category, but closure under such quotients is not established.',
 'Explicit open construction problem; author postpones support formalism.','open on the pages','atelier','D',
 'Exact excision/atelier searches S9E-01,03–05 and shared S67-02,03,05,11,12 found no published solution. General categorical localization or quotient terminology does not prove existence inside this axiom class. No reason for historical abandonment beyond the author’s explicit postponement is inferred.',check='Open for general ateliers in this run; maquettes handled separately in C-SA21-9-123.',confidence='high')
C(123,[(18,[137])],
 'For a maquette and arbitraryN, “la maquette A\\N simplement”.',
 'For a maquette A (an arbitrary incidence poset, open refinement=equality, disjointness=inequality) and any N⊆A, the induced maquette A\\N together with p(x)=x for x∉N and p(x)=0 for x∈N has kernelN and the stated universal property among provisional pointed homomorphisms. A map killing N factors by restriction; the bidirectional incidence convention at0 makes p preserve incidence even when N is not an incidence ideal.',
 'Simple-case solution asserted.','stated without proof','atelier','D',
 'No exact publication using this provisional maquette category was found in the documented atelier searches. The construction is independently proved directly from the universal property; ordinary pointed-set quotients alone would omit the incidence check.',check='Valid in the exact provisional category. Independent proof in formalism_and_checks.md §6.',confidence='high')
C(124,[(18,[136,137])],
 'Set example: N={X:|X|⊂E\\E′}; quotient should be Figélem(E′).',
 'For the full set-figure atelier on E and a subset E′, the author proposes excision by N={X:the displayed closed support |X| lies in E\\E′}, with quotient the elementary figures on E′. He wants a construction as a quotient of A\\N. This is not established; it must distinguish killing a whole closed support from killing only a top open stratum, and must address the elementary-pullback problem of C-SA21-9-116.',
 'Expected model followed by explicit admission that even the set case is not obvious.','open on the pages',check='Not proved here. The literal closed-support kernel is preserved; it is not silently changed to the open-support condition.',confidence='high')

# IX138–140: final subdivision definition and canceled strengthening.
C(125,[(18,[138,139])],
 'Subdivisions: fiberwise supp°φ^{-1}(X)=X°; total suppG=suppF under Atmag supp².',
 'For G≪F with the monotone least-receiver map φ:G→F, the fiber condition is ∨_{Y:φ(Y)=X}Y°=X° for every X∈F. It implies equality of total supports. Conversely total equality implies every fiber equality when all the open supports of F and G lie in one complete Boolean subortholattice (the pair commensurability condition): the fibers partition the join below mutually orthogonal X°. The written named hypothesis is “Atmag supp²”; its identification with scan119γ² remains an ink/notation question.',
 'Equivalence asserted with a short formal discussion.','proof sketched','atelier','D',
 'Exact subdivision/support searches S9E-01,03–05 and shared S67-05,08,11 found no published theorem in this formulation. The Boolean partition part is independently verified using C-SA21-9-096; general subdivision/triangulation literature does not settle the remaining atelier-local detection step.',check='Fiber/total equivalence valid under explicit joint Boolean commensurability. The named-axiom ambiguity is not resolved by guessing.',confidence='high')
C(126,[(18,[138,139])],
 'Equivalent(iii): no Z∈A with Z≪F and ZδG; if divisible, no such locusx.',
 'The source asserts that support equality/fiber coverage is equivalent to absence of an elementary refinement Z≪F internally disjoint from every stratum of G, using Atmag supp²; with divisibility it may test only loci. The forward implication follows from nonzero supports. The converse needs a local supply of refinements detecting a nonzero support remainder; pair commensurability alone does not provide it. A three-stratum atelier with Boolean support lattice violates that converse under bare At1–4 plus all commensurability axioms.',
 'Equivalence asserted; named support axiom invoked rather than expanded.','proof sketched','atelier','D',
 'Searches locate no exact theorem identifying “Atmag supp²” beyond these manuscript pages. Existing Boolean/orthogonal closure theory handles lattice remainders but not their realization by local refinements. The finite obstruction is therefore conditional on interpreting supp² as scan119 pair commensurability, not an unconditional refutation of a potentially stronger source axiom.',computation='commensurability_alone_not_local_subdivision_detection in finite_checks_output.json; primitive typed relations and Boolean support lattice checked.',check='Local converse not established from the explicit commensurability condition alone. R-SA21-9E-011; exact axiom label must be checked on scan.',confidence='medium')
C(127,[(18,[139])],
 'Under divisibility, G maximal among refinements ordered by⊂; all conditions implyφ surjective.',
 'With the source’s divisibility hypothesis, the no-disjoint-locus condition is claimed equivalent to G being maximal under face inclusion among figures refining F. The source explicitly replaces “maximal for≪” by “maximal for⊂”. Fiber coverage implies φ is surjective because every stratum X has X°≠0. These statements do not justify the preceding local support-detection converse without its separate hypothesis.',
 'Equivalent criterion and surjectivity stated; the order symbol is self-corrected.','corrected by himself later','atelier','D',
 'Exact atelier searches found no later publication of this precise maximality criterion. It matches the earlier manuscript’s subdivision formulations, not a general claim that maximal objects for the refinement order are subdivisions. The source-order correction is decisive.',check='Surjectivity checked directly; maximality argument uses loci and compatibility, carried with the exact divisibility assumption. No stronger source axiom is silently inserted.',confidence='medium')
C(128,[(18,[139,140])],
 'Canceled: target order topology quotient of source, “ou encore” every comparison lifts to one comparable pair.',
 'The deleted strengthening asks for the order topology of F to be the quotient of that of G and identifies this with single-pair lifting: for X≤X′ choose Y≤Y′ in the respective fibers. As a general assertion for surjective finite-poset maps, these conditions differ: two disjoint two-element chains mapped successively onto0<1<2 have the quotient Alexandrov topology, but the comparison0<2 has no single comparable lift. Only the generated transitive relation is forced by quotient topology.',
 'Entire additional requirement and its continuation are canceled; it is absent from the retained final subdivision definition.','corrected by himself later','localization','D',
 'S9E-02–05 and shared S67 order/gluing searches found no exact retained atelier theorem for the deleted requirement. The finite-poset calculation independently checks the general topological equivalence and is expressly not represented as a full atelier subdivision counterexample.',computation='deleted_quotient_topology_equivalence: all8 target subsets checked for the final topology; single-pair lifting fails.',check='Withdrawn on the pages. General equivalence false; no claim that the finite map realizes every preceding subdivision hypothesis. R-SA21-9E-012.',confidence='high')

assert [int(c['id'].split('-')[-1]) for c in CLAIMS]==list(range(81,129))
