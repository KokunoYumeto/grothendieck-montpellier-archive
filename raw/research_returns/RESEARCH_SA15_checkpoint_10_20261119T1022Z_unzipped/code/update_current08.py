"""Refresh checkpoint08 outcomes; retain all actual historical reviews."""
from pathlib import Path
import datetime,json,re
w=Path(__file__).resolve().parents[1]
rows=json.loads((w/'notes/item_status.json').read_text())
changes={
'A.1':('REFUTED (a),(b),(c), with exact counterexample degree ranges; (d) PROVED',
 'thm:OC-product-exact-degrees; thm:OC-exact-integral-injectivity-degrees; cor:OC-surface-exact-degrees; thm:A-all-degree-ranges; prop:A-transpose-u2',
 'The characteristic-two product has integral H2 injectivity in every positive degree, and both torsion-free cokernel and torsion identification exactly for d>=2. The separate explicit threefold has injectivity exactly for d>=3, with nonzero kernels in degrees1,2. The coherent surface example has injectivity exactly for d>=2. Thus all requested universal assertions and exact degrees for the counterexamples are settled. Additional examples exist at every prime, with saturation and torsion identification for d>=p²-p; their odd-prime intermediate degrees are an expressly additional refinement.'),
'A.4':('OPEN: fixed-product images now determined in every degree; arbitrary-X classification remains',
 'thm:product-char2-all-full-groups; thm:product-Hasse-irred; thm:product-full-group-if-hasse-irreducible; thm:effective-monodromy-matrices; thm:perfect-field-exact-monodromy-data',
 'All projective-space images and complete effective matrix constructions for arbitrary input are proved. For the fixed ordinary characteristic-two product E×E, both geometric and arithmetic groups are GL_(9d²-1)(F2) in odd degree and the full pointwise three-covector stabilizer 2^[3(9d²-4)]:GL_(9d²-4)(F2) in even degree, for every d>=1; irreducibility holds exactly in odd degree. The remaining main gate is uniform structural classification and irreducibility for arbitrary X. Extensions to every ordinary elliptic pair are under proof, not counted as completed.'),
'B.3':('OPEN only in higher dimension: exact elliptic range at every odd prime proved',
 'thm:B-RD26-wild; cor:B-RD27-exact-three; thm:B-RD12; cor:B-RD13; prop:B-RD24-finite-test; prop:B-RD25-basechange-obstruction',
 'Every elliptic level is classified, including all wild characteristic-three levels and exact defects3,6,12. For e=2u, s=v3(u), L=floor(log3u), the largest additive level at p3 is N=1+min(s,floor((L+1)/2),floor((L+s+1)/4)); among potentially good elliptic curves, the least full-torsion level forcing good reduction is N+1. The first full27 case e216 exists with defect12. A ramification-nine base change of the earlier e24 full9 curves cannot supply it, so a new equivariant trace-arc construction is used. Sharp potentially-good thresholds in higher dimension remain open; unrestricted multiplicative examples are already accounted for.')
}
for row in rows:
 if row['item'] in changes:row['status'],row['where'],row['gate']=changes[row['item']]
(w/'notes/item_status.json').write_text(json.dumps(rows,indent=2)+'\n')
root=json.loads((w/'notes/root_results.json').read_text())
for r in root:
 if r.get('label')=='open:A-small-degree':
  r.update(statement='Universal integral assertions refuted, with exact degrees for the explicit characteristic-two counterexamples',status='Proved: counterexamples and exact degree ranges',depends_on='thm:OC-product-exact-degrees; thm:OC-exact-integral-injectivity-degrees; cor:OC-surface-exact-degrees',notes='Product: injectivity all d>=1, saturation and torsion identification iff d>=2. Separate threefold: injectivity iff d>=3. Coherent surface: injectivity iff d>=2. Additional odd-prime counterexample intermediate degrees are a separate refinement.')
(w/'notes/root_results.json').write_text(json.dumps(root,indent=2)+'\n')
aux=(w/'RESEARCH_SA15_paper.aux').read_text() if (w/'RESEARCH_SA15_paper.aux').exists() else ''
nums=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux))
idmap={r['id']:r['label'] for r in root}
def location(text):
 return '; '.join(x+(f' (no. {nums[idmap.get(x,x)]})' if idmap.get(x,x) in nums else '') for x in text.split('; '))
table='| Item | Current outcome | Statement / location | Scope and remaining gate |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join([r['item'],r['status'],location(r['where']),r['gate']])+' |' for r in rows)+'\n'
(w/'notes/current_outcome_table.md').write_text(table)
p=w/'RESEARCH_SA15_report.md';old=p.read_text();body=old[old.index('# RESEARCH_SA15 research report'):]
marker='\n## Checkpoint 08: exact degrees, uniform product groups, and every elliptic wild level\n'
if marker in body:body=body.split(marker)[0]
new=marker+'''
The opening table gives the current outcomes; previous checkpoint sections are dated history. This checkpoint remains INCOMPLETE because the arbitrary-X A.3/A.4 structural questions and the sharp higher-dimensional B.3/B.4 thresholds remain. The narrower Noetherian-and-coherent refinement of E.2 remains separately visible. The mathematical changes below passed complete proof audits; computations check specified identities and finite ranges and do not replace those proofs.

### A.1: the required counterexamples now have exact degree ranges

For the fixed characteristic-two product Z=X×P1, B=A external tensor O(591·9^556+2), integral H2 restriction is injective for every smooth section of every positive degree. Its cokernel is torsion-free and its full torsion subgroups are identified exactly in degrees d>=2; both fail for every smooth degree-one section. Thus A.1(a),(b) are false as universal statements, with their requested counterexample degree conditions now exact.

The proof works with the relative de Rham kernel K^j=Omega_Z^j(logY)(-Y). Kunneth kills total degree one in every degree. Equal-rank first crystalline lattices therefore map isomorphically, and the first universal-coefficient diagram plus rational weak Lefschetz proves integral H2 injectivity. For the positive saturation range, a possibly nonzero H1(K1) is killed by its outgoing Hodge differential: composing that differential with residue gives ordinary restriction, by d(s eta)=ds wedge eta+s d eta. Two explicit negative-twist vanishings make that restriction injective. This yields H1 de Rham isomorphism and H2 de Rham injection. The full Tor sequence uses BOTH surjectivity on p-torsion and injection modulo p to prove torsion-free cokernel; neither unsafe shortcut is used. The same argument gives the additional all-prime bound d>=p²-p.

For the separate843-root characteristic-two threefold, integral H2 restriction is injective exactly in degrees d>=3. Its kernels killed by2 have dimensions at least361 in degree1 and at least1 in degree2. The corrected eigensheaf calculation gives h1(A^-d)=1203,1,0 for d1,d2,d>=3. The actual dual of a symmetric power is used; a proposed interchange with the symmetric power of the dual was rejected before integration. The split formula Sym²(V2)=V2 direct-sum L2^20 follows from the Frobenius-split extension. The logarithmic cotangent filtration determines the negatively twisted one-forms, and the base curve, Stein factorization, Riemann–Hurwitz and an odd-degree norm identify the first integral crystalline lattices. A closed-form conormal argument handles the borderline degrees3,4. All smooth sections in the specified degrees are covered.

The coherent surface example already has kernel dimension1 in degree1 and zero in every higher degree. Together these results settle the required counterexample degree ranges. The additional odd-prime product examples have a uniform positive bound; their intermediate degrees are not needed to complete these characteristic-two counterexamples and are retained as an extra refinement.

### A.4: all groups on the fixed ordinary product

For E/F2 given by Y²Z+XYZ+X³+Z³=0, X=E×E and the Segre polarization O(3O) external tensor O(3O), every degree is now determined. The local-system rank is r=9d²-1. In odd degree both geometric and arithmetic images are GL_r(F2). In even degree both are the entire pointwise stabilizer of the three independent invariant covectors, namely the group of matrices [A B;0 I3] with A in GL_(r-3)(F2) and arbitrary B. It has order 2^[3(r-3)] times the order of GL_(r-3)(F2). The representation is irreducible exactly in odd degree. The statement persists over every perfect characteristic-two base extension of this fixed model.

The new geometric step proves irreducibility of every product Hasse divisor in degrees at least4. A pointed Cartier calculation on a curve with one-dimensional Cartier kernel, evaluated at a point where its kernel differential is nonzero, controls a mixed tacnode with an ordinary curve. The full Hasse divisor is smooth at that tacnode. Restricting to a degree-three linear system plus a fixed ordinary complementary curve leaves only the degree-three Hasse components and the tangency divisor; the mixed tacnodes force all their containing global components to coincide. Jet interpolation and incidence dimensions are verified in the small complementary degree one, where the tensor tangent-space argument and the independent polar quadratics of the cubic supply the needed bounds. The proof handles restriction multiplicities explicitly. Combining this result with the previously audited conditional group theorem, the natural GL80 block and the complete translation subgroup removes its geometric hypothesis. This is the full fixed-product result; arbitrary-X structural classification remains open.

### B.3: sharp wild existence at every elliptic level

At p3, let e be positive and even, s=v3(e/2), and m one of3,6,12. Additive elliptic curves with full rational3^n-torsion and exact semistability defect m exist precisely when

    s >= n-1 and e >= (8/m)·3^max(2n-2,4n-4-s).

The construction has algebraically closed perfect residue field and exactly the specified absolute ramification index. If e=2u and L=floor(log3u), the largest additive level is

    N(e) = 1 + min(s, floor((L+1)/2), floor((L+s+1)/4)).

Consequently the least level forcing good reduction among potentially good elliptic curves is N(e)+1. In particular e216 admits full27-torsion with defect12. Combined with the previously proved tame criterion, this determines the elliptic existence question for every odd prime. The higher-dimensional sharp threshold is still open.

The proof constructs a stable arc in the regular universal Drinfeld-level deformation ring of Y²=X³+uX²-X. The odd parameter T=X^-1/2 has [3]_T3=4u. Full-level factorization puts u in the6·3^(2n-2) power of the maximal ideal. A weighted Cohen chart has x=pi^A Z, y=pi and3=pi^d V. Exact traces and norms under the order-three framing action give invariants I and U_y; imposing I=lambda U_y^(A/3) has simple residual equation1-lambda Z². The implicit-function argument therefore gives a complete DVR with the required ramification, preserving the marked full torsion and the faithful wild action. Appropriate congruences on A extend it to groups of orders6 or12. Descent concerns the generic marked elliptic curve; the good integral model is used for its faithful special-fibre inertia action. No averaging by3 or integral descent through a ramified quotient is assumed.

A separate complete obstruction proves that the earlier e24 full9 examples cannot reach e216 full27 merely by a ramification-nine base change. It computes ramification breaks80 and1052 and a norm-uniformizer contradiction. This explains why the new direct equivariant construction is necessary for that route. The earlier large finite elimination formula remains unevaluated as a computation; its first-case existence answer is now established by the new proof, not by claiming that elimination was run.

### Executed checks and source audit

| Certificate | Exact scope | Independent root run | Output |
|---|---|---|---|
| verify_product_tacnode_jets.py |441 flag pairs;288 admissible configurations;256 incidence identities; polar and Cartier identities |0.02306400400266284s |outputs/verify_product_tacnode_jets.json |
| A_injectivity_degree_checks.py |Actual symmetric-square transition;30 eigensheaf rows; negative bounds;1203/1/0; base Cartier kernel211 |0.18007099199894583s |outputs/root_A_injectivity_degree_checks.json |
| A_product_degree_checks.py |11 prime boundary cases;113 finite cyclic-module maps; three unsafe-shortcut counterexamples |0.06231393499911064s |outputs/root_A_product_degree_checks.json |
| verify_level27_basechange_obstruction.py |Exact torsion valuations, ramification breaks, norm terms and contradiction |0.033169171001645736s |outputs/root_verify_level27_basechange_obstruction.json |
| verify_wild_trace_arcs.py |66 exact equivariance identities; trace/norm and tripling identities;109727 constructed integer arcs through e50000,n8;25000 maximum-level comparisons |2.827041984997777s, final sign-expanded run |outputs/root_verify_wild_trace_arcs_with_sign.json |

Each program was read and independently executed. Author outputs were preserved; root outputs record their separate run times. The first three geometric arguments also passed reduction-descent independent audits. The wild construction's deformation, convergence and descent are proved in the text and are not represented as a computer-instantiated formal family.

Primary-source checks include Carter and Strauch(2021), Theorem2.1.2 p437 and Proposition2.2.3(i),(vi),(vii) p439 with proof throughp441; Katz(1981), Theorem1.2.1 p143, used on Artinian nilpotent deformation quotients; Brion and Kumar(2005), Theorem1.3.4 and Lemma1.3.6/Proposition1.3.7 pp24–27; and Stacks Theorem37.53.4(Tag03H0), section53.12 and Lemma53.12.2(Tags0C1B/0C1D), and Lemmas31.18.2/31.18.6(Tags0BCY/0BD2). The source census records exact access states. Searches for a general ambient-family monodromy theorem remain in the dated logs; no priority claim is made.
'''
log=w/'notes/ROOT_SEARCH_LOG_08.md'
if log.exists():new+='\n'+log.read_text()+'\n'
p.write_text('INCOMPLETE\n\n'+table+'\n'+body+new)
events=w/'notes/root_check_events.tsv';existing=events.read_text()
audits={
'A1-PRODUCT-EXACT-DEGREES-ROOT':('independent re-proof','Full proof PASS: actual symmetric-dual filtration, tame logarithmic cotangent line sequence, all Kunneth terms, relative deRham degree1 vanishing, first crystalline lattice isomorphism, outgoing Hodge differential detected by residue, conormal injectivity, both UCT diagrams and full Tor sequence. Product H2 injective all d; characteristic2 saturation and full torsion isomorphism iff d>=2. Additional all-prime bound d>=p²-p.'),
'A1-PRODUCT-DEGREES-EXACT-ROOT':('computation or formal certificate','Entire A_product_degree_checks.py read and independently executed; PASS0.06231393499911064s. Eleven prime boundary cases,113 finite cyclic-module homomorphisms and three unsafe shortcut counterexamples. outputs/root_A_product_degree_checks.json; author output preserved.'),
'B-WILD-ALL-LEVELS-ROOT':('independent re-proof','Full B26 proof and B27 consequence PASS: framed elliptic normalization; formal coefficient4u; Drinfeld regularity and prime-factorization order; weighted Cohen kernel and chart convergence; action extension before trace; exact trace/norm invariant and all error orders; simple-root DVR; tame branch congruences; generic marked descent and faithful special inertia; exact integer choice and maximum formula. CarterStrauch Theorem2.1.2p437, Prop2.2.3(i),(vi),(vii)p439/proofp441 and Katz Theorem1.2.1p143 reread. Every odd-prime elliptic level now determined; higher-dimensional thresholds remain.'),
'B-WILD-TRACE-EXACT-ROOT':('computation or formal certificate','Entire verify_wild_trace_arcs.py read and independently executed; PASS2.9114626570008113s. Exact symbolic identities,66 equivariance tests,109727 constructed integer arcs through e50000/n8,25000 exact maximum-level comparisons. outputs/root_verify_wild_trace_arcs.json; author output preserved. Formal deformation/descent is proved separately, not computationally instantiated.')
}
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with events.open('a') as f:
 for sid,(kind,desc) in audits.items():
  if sid+'\t' not in existing:f.write('\t'.join([sid,now,'GPT-6 Astra (OpenAI); /root; inherited effort',kind,desc])+'\n')
print('Checkpoint08 current outcomes refreshed; historical actual reviews preserved.')
