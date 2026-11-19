"""Human-assigned page statuses and individual development judgments.

These ID lists are explicit judgments after reading, not a keyword classifier.
"""
categories={
 'proved there':[1,5,13,18,19,46,79,100],
 'proof sketched':[4,8,9,10,12,14,16,20,22,25,26,35,36,39,42,43,44,49,52,56,59,64,67,69,71,76,77,80,81,82,83,87,89,90,97,106],
 'stated without proof':[17,30,32,38,41,53,74,78,86,96,103,109,110],
 'corrected by himself later':[23,45,51,55,65,75,84,92,98,105],
 'false as stated':[3,7,21,28,33,47,48,50,58,66,68,70,93,94,95],
 'open on the pages':[2,6,11,15,24,27,29,31,34,37,40,54,57,60,61,62,63,72,73,85,88,91,99,101,102,104,107,108,111,112,113],
}
assigned={}
for category,ns in categories.items():
    for n in ns:
        assert n not in assigned, n
        assigned[n]=category
assert set(assigned)==set(range(1,114)), sorted(set(range(1,114))-set(assigned))
for c in claims:
    n=int(c['id'].rsplit('-',1)[1])
    c['status_category']=assigned[n]
    c['status_assignment']='Manually assigned from the actual source and its correction/cancellation history; rich status_on_pages retains mixed clauses and transcription-dependent qualifications.'
    c['record_origin']='source assertion' if n!=111 else 'source fragment, not an identifiable assertion'
    c['reconstruction_boundary']='The his_statement field is a short quotation or explicitly labeled paraphrase. The modern statement, hypotheses, proofs and counterexamples are this run’s reconstruction unless expressly attributed to the page or an opened source.'

worth={
 1:'Commentary work only: the two-object adjunction counterexample completely answers the requested one-object test.',
 2:'Commentary work only: triangle identities settle the fixed-part and reflection claims once the idempotence hypothesis is stated.',
 3:'Commentary work only: descent of the representing local object gives the adjoint formula without a new research problem.',
 4:'Worth a convention-focused companion: specify the free-family arrows and the missing flattening coherence before interpreting the symmetric tensor construction.',
 5:'Worth a short proof comparison with the Picard pages: the self-braiding scalar answers the inverse-pairing question and explains the strict-commutativity obstruction.',
 6:'Worth a bounded commentary reconstruction: state the exact density/comodel hypotheses and use the existing counterexamples to remove the proposed cofinality shortcut.',
 7:'Scan-first for the undefined filtered-F-crystal comparison endpoint: identify its categories and functor before developing a claimed equivalence; the cocharacter identity is separately settled.',
 8:'Commentary work for the false finality shortcut; a bounded follow-up should state Kelly’s exact comodel relations for the intended dense subcategory.',
 9:'Worth a bounded formal reconstruction: define the missing successor operation and preexactness for one explicitly small mixed doctrine.',
 10:'Commentary work only: the cylinder and fold extension tests settle the stated faithfulness conditions with their marked-cone compatibility.',
 11:'Worth a focused localization comparison: identify which site quotient makes the left adjoint lex; ordinary fullness alone is already insufficient.',
 12:'Commentary work only: SGAIV9.1.4 and9.1.6(b,c) settle the representably fully faithful inclusion criterion with all2-cells retained.',
 13:'Worth a bounded theorem-identification task after specifying whether the model limits are created by the underlying-object interpretation and preserved under every base change.',
 14:'Worth an explanatory lattice diagram with the exact six examples and a cardinal-bound counterexample; a classification of the entire quotient lattice is not a realistic one-run target.',
 15:'Commentary work only for constancy: the Cantor-space filtered-colimit witnesses give the negative answer; constructibility first needs a chosen ambient convention.',
 16:'Worth a small worked classifier example: separate group torsors from G-sets and flat monoid actions from arbitrary endomorphism structures.',
 17:'Commentary work only: restore Beck’s missing split-coequalizer condition and the source/target of the coalgebra comparison.',
 18:'Commentary work only: the sheaf inclusion into a presheaf topos answers the requested direction and should be separated from Boolean covers.',
 19:'Worth a sharply bounded fppf comparison: retain the explicit noetherian counterexample and work through one nonnoetherian fppf-local test ring from Schröer’s construction.',
 20:'Worth a reading-led commentary: induced versus reduced structures on irreducible components change the classifier, while the ultraproduct settles coherence only in the stated ring signature.',
 21:'Worth a convention-focused commentary: fix the empty-scheme convention and separate all zero-dimensional local tests from the canceled artinian-testing shortcut.',
 22:'Worth a compact algebraic companion: verify the idempotent decompositions and distinguish the affine coproduct from the presheaf coproduct; the reflection theorem is established.',
 23:'Commentary work only: the Q-algebra example already refutes the presheaf inverse-limit shortcut and identifies the valid filtered localization.',
 24:'Worth a short clarification of the chosen meaning of perfect in characteristic0; the positive-characteristic Frobenius construction itself is established.',
 25:'Worth a bounded gluing task after specifying the overlap and local factorization conditions; open/closed recollement alone does not prove the general claim.',
 26:'Commentary work for the accepted characteristic-site construction; a worked point calculation can clarify how it differs from the canceled infinite-open-intersection attempt.',
 27:'Worth a constructive comparison of component-rank bounds and decomposition torsors: the Set-level calculation is settled and exact-rank closure is refuted, but the internal assignment remains a precise residual issue.',
 28:'Commentary work only: finite relation witnesses prove geometric flatness, while the multiplication-by2 system refutes the full-module faithful-flatness claim.',
 29:'Worth a convention-focused comparison of property categories and structured moduli; the listed full-property and ordinary injectivity readings already have explicit counterexamples.',
 30:'Worth a focused logical comparison of formal smoothness and formal étaleness: first retain a fixed finite presentation and write the exact internal lifting quantifiers.',
 31:'Commentary work only: decidable zero is the precise constructive fraction-field hypothesis and the localization proof is complete.',
 32:'Commentary work only: tensor invertibility gives local rank1, and the nonprincipal ideal explains why the canceled global monogenicity step fails.',
 33:'Commentary work only for the universal rank claim: the countable-power counterexample and the sharply-larger theorem determine the exact quantifiers.',
 34:'Worth a bounded bicolimit investigation with one specified morphism/rank convention; the checked flexible-limit theorem does not answer that independent question.',
 35:'Worth a precise historical translation of the changing generator list into an adjoint-functor-theorem solution set; the standard locally presentable case is settled.',
 36:'Commentary work only: the comma-category variance and density distinction are settled by the explicit small counterexamples and Kelly’s exact criterion.',
 37:'Worth a historical comparison of the manuscript’s density terminology with boundedness: the modern universal assertion is already classified by Vopěnka’s principle.',
 38:'Commentary work only: the singular-cardinal diagonal argument refutes the unrestricted filtration equality and identifies the required sharp-cardinal repair.',
 39:'Worth a bounded translation of the tensor-product variance; the locally presentable version is established, so any further task must isolate a specific merely accessible case.',
}
for p in problems:
    n=int(p['id'].rsplit('-',1)[1])
    if n in worth:p['worth']=worth[n]

# Proof-audit refinements, not changes to the archival transcription.
for c in claims:
    if c['id']=='C-SA23-groupes-056':
        c['statement']=c['statement'].replace('a Boolean idempotent algebra with at most n atoms','a finite Boolean idempotent algebra with at most n atoms')
    if c['id']=='C-SA23-groupes-064':
        pr='Write the inverse image of1 under evaluation as a finite sum of tensors m_i⊗phi_i; the values phi_i(m_i) generate the unit ideal. Locally where one is invertible, m_i is unimodular and M splits as A⊕N. The cross term N⊗A lies in the kernel of evaluation, so injectivity forces N=0. This finite open cover proves M finite locally free rank1. The ideal(2,1+sqrt(-5)) has I²=(2) and norm2, but a²+5b²=2 has no integer solution, so it is invertible and nonprincipal. Hom base change is used only after finite projectivity is established.'
        c['computation']['proof_or_check']=pr;c['present_status']='As of19November2026: '+pr
        events.append([c['id'],DATE,WHO,'independent re-proof','Proof audit replaced the abbreviated dual-basis inference by local splitting plus injectivity of evaluation.'])

# Correct an obsolete search-audit lead: the Bird PDF did not open.
for s in searches:
    if s['query'].startswith('accessible categories flexible bilimits'):
        s['opened']=[x for x in s['opened'] if 'BirdPhD' not in x['url']]
        s['opened'].append(dict(url='https://geoffroy.horel.org/Rigidification.pdf',locators='§2pp4–5',match='Exact unenriched locally presentable tensor construction, full text opened.'))
        s['limits']+=' Bird1984 thesis Chapter5 was an indexed lead only; two full-PDF routes failed503/502. Caviglia–Horel circulated2015 and appeared2016.'
    if s['query'].startswith('SGA4 IV geometric localization'):
        s['opened'][0]['locators']='IV1.2; IV9.1.2–9.1.7; IV9.2.1–9.2.6 and9.3.4–9.3.5; original printed433–435 visually checked'

links.extend([
 ['folder','161-1 scan13, K161-1-01:407–466; C-SA23-groupes-010–011','162-5 API pp8,38:302–325,985–1009; C-SA23-forms-041','The same self-commutor epsilon of an invertible object controls permutation signs and obstructs strict commutativity.','Both actual transcription endpoints read. The161-1 inverse-pairing question is distinct from the162-5 strictification claim; the latter retains deleted commutativity wording and Verdier objections.','Codex leads only; no indexed Pro entry'],
 ['folder','161-1 scan13, K161-1-01:407–442; C-SA23-groupes-010','68 scans54,56, Pro transcription:810–813,916–948; C-SA23-misc-034,037','The self-braiding scalar specializes to the Koszul commutor on graded determinant lines and the orientation block-permutation sign.','Both actual endpoints read. The source itself names the Koszul symmetry on scan56; no assertion of determinant uniqueness is added.','SA23-333; SA23-335; SA23-336; SA23-339–341'],
 ['folder','161-2 file05 scan79:332–336; C-SA23-groupes-084','161-2 file06 scan91:379','The finite-presentable-object condition is moved from the model functor to its left adjoint.','Both passages directly read; Groups→Set refutes the earlier wording and the Hom adjunction proves the later one.','No indexed entry'],
 ['folder','161-2 file06 scans94–95:428–473; C-SA23-groupes-098','161-2 file07 scan96:1–9','A canceled presheaf field-classifier assertion is replaced by the decomposition sheaf topos.','Both passages directly read; Caramello–Johnstone§1 matches the corrected topology.','No indexed entry'],
 ['folder','161-2 file01 scan4:5–47; C-SA23-groupes-023','161-2 file02 scan30:453–462','The first cardinal-size capture claim is repaired by a sufficiently large-cofinality index.','Both passages directly read; the singular-cardinal witness shows why cardinal inequality alone is insufficient.','No indexed entry'],
 ['folder','161-2 file05 scans66–69:1–83; C-SA23-groupes-075','161-2 file07 scan104:394–425','The later pointwise-model theorem inserts the missing preservation hypothesis on the target functor.','Both actual passages directly read, with the insertion at415 retained.','No indexed entry'],
 ['published work','161-2 file01 scan19:520–524; C-SA23-groupes-029','SGA4I, IV9.1.4 and9.1.6(b,c,d), printed433–435','Representable full faithfulness on all2-cells characterizes a geometric inclusion; base change exists.','Original printed pages rendered and read, not only a modern synopsis.','SGA4I1972'],
 ['published work','161-2 file06 scan81:40–45; C-SA23-groupes-086','SGA4I, IV Exercise7.6(a–g), printed414–417','Essential morphisms, sufficient essential points and Karoubi completion.','Exact retyped passage read here; original facsimile checked by spaces owner; attribution to Roos retained.','SGA4I1972'],
 ['published work','161-2 file07 scan112:687–712; C-SA23-groupes-107','SGA4I, IV9.1.6(d), printed435','The needed relative2-pullback existence theorem.','Original page read; the fixed-object universal property is independently reconstructed.','SGA4I1972'],
])

search('zbMATH Open Lazard Lois de groupes analyseurs; Benabou Structures algebriques categories; Gabriel Ulmer Lokal prasentierbare Kategorien',[22,25,83,85,88,91,104,108,111],[dict(url='https://www.numdam.org/item/SB_1954-1956__3__77_0/',locators='bibliography and linked Zbl0068.02702',match='Actual original Lazard source followed from bibliographic lead.'),dict(url='https://numdam.org/item/CTGDC_1968__10_1_1_0/',locators='bibliography and linked Zbl0162.32602',match='Bibliographic comparison lead only.')],limits='Both direct zbmath.org linked records returned403; domain-filtered title searches had no usable record. Proofs rely on opened original/author texts, not those blocked records. MathOverflow467326 was opened for the exact Gabriel–ZismanI.3.1 backward pointer and its local-smallness warning; no answer there was treated as a theorem.')
